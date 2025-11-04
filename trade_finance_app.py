import streamlit as st
import pandas as pd
import json
import re
import os
import sys
import subprocess
import logging
from pathlib import Path
from datetime import datetime
from openai import AzureOpenAI
from dotenv import load_dotenv


def first_n_words(text: str, n: int = 3) -> str:
    text = (text or "").strip()
    # Use word characters; keep unicode word chars
    words = re.findall(r"\w+", text, flags=re.UNICODE)
    return " ".join(words[:n]) if words else "document"

def sanitize_filename(name: str, max_len: int = 80) -> str:
    name = (name or "").strip()
    # Normalize common dashes and separators to hyphen
    name = name.replace("—", "-").replace("–", "-").replace("/", "-").replace("\\", "-")
    # Remove illegal Windows filename chars and control chars
    name = re.sub(r'[<>:"/\\|?*\x00-\x1F]', "", name)
    # Collapse whitespace
    name = re.sub(r"\s+", " ", name).strip()
    # Trim length
    return name[:max_len] if len(name) > max_len else name

# Load environment variables
load_dotenv()

# Document options from the Excel file
DOCUMENT_OPTIONS = [
    ("ILC", "Import Letter of Credit"),
    ("ELC", "Export Letter of Credit"),
    ("SLC", "Sight Letter of Credit"),
    ("ULC", "Usance Letter of Credit"),
    ("RLC", "Revolving Letter of Credit"),
    ("TLC", "Transferable Letter of Credit"),
    ("BBLC", "Back-to-Back Letter of Credit"),
    ("SBLC", "Standby Letter of Credit"),
    ("RCLC", "Red Clause Letter of Credit"),
    ("GCLC", "Green Clause Letter of Credit"),
    ("IBC", "Import Bills for Collection"),
    ("EBC", "Export Bills for Collection"),
    ("BG", "Bank Guarantee"),
    ("SG", "Shipping Guarantee"),
    ("PG", "Performance Guarantee"),
    ("APG", "Advance Payment Guarantee"),
    ("BB", "Bid Bond"),
    ("RG", "Retention Guarantee")
]

# Global logger
logger = None

def setup_audit_logging():
    """Setup comprehensive audit logging"""
    global logger
    
    # Create logs directory
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    # Create timestamped log file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = logs_dir / f"audit_{timestamp}.log"
    
    # Setup logger
    logger = logging.getLogger("trade_finance_audit")
    logger.setLevel(logging.DEBUG)
    
    # Clear any existing handlers
    logger.handlers.clear()
    
    # File handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    logger.info("=== AUDIT LOG STARTED ===")
    logger.info(f"Log file: {log_file}")
    
    return log_file

def validate_azure_config():
    """Validate Azure OpenAI configuration"""
    logger.info("Starting Azure OpenAI configuration validation")
    
    required_vars = [
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_API_KEY", 
        "AZURE_OPENAI_API_VERSION",
        "AZURE_OPENAI_CHAT_DEPLOYMENT"
    ]
    
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if not value:
            missing_vars.append(var)
            logger.error(f"Environment variable {var}: MISSING")
        else:
            logger.info(f"Environment variable {var}: SET")
    
    if missing_vars:
        error_msg = f"Missing required environment variables: {', '.join(missing_vars)}"
        logger.error(error_msg)
        return False, error_msg
    
    logger.info("Azure OpenAI configuration validation completed successfully")
    return True, "Configuration valid"

def create_directories():
    """Create required directories"""
    logger.info("Creating required directories")
    
    directories = ["input", "output"]
    for dir_name in directories:
        Path(dir_name).mkdir(exist_ok=True)
    
    logger.info(f"Directories created successfully: {', '.join([d + '/' for d in directories])}")

def clean_input_directory():
    """Clean the input directory before processing"""
    logger.info("Cleaning input directory")
    
    input_dir = Path("input")
    deleted_files = []
    
    if input_dir.exists():
        for file_path in input_dir.glob("*.txt"):
            try:
                file_path.unlink()
                deleted_files.append(file_path.name)
                logger.debug(f"Deleted file: {file_path.name}")
            except Exception as e:
                error_msg = f"Error deleting {file_path.name}: {e}"
                logger.warning(error_msg)
                st.warning(error_msg)
    
    logger.info(f"Cleaned input directory. Deleted {len(deleted_files)} files: {deleted_files}")

def save_primary_document(content, document_code):
    """Save the primary document with filename that cross_new_csv.py can detect as LC"""
    logger.info(f"Saving primary document with code: {document_code}")
    
    if not content.strip():
        logger.warning("Primary document content is empty")
        return None
    
    # Use lowercase filename that cross_new_csv.py can detect as LC
    filename = f"{document_code.lower()}.txt"
    filepath = Path("input") / filename
    
    # Get the document description for the heading
    doc_description = next((desc for code, desc in DOCUMENT_OPTIONS if code == document_code), document_code)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            # Write the file heading that cross_new_csv.py expects for the LC (golden truth)
            f.write(f"### Letter of Credit (LC) - GOLDEN TRUTH DOCUMENT: {filename}\n\n")
            f.write(content.strip())
        
        logger.info(f"Primary document saved successfully: {filepath}")
        logger.debug(f"Primary document size: {len(content)} characters")
        logger.info(f"Added LC heading for cross_new_csv.py compatibility")
        logger.info(f"Using lowercase filename {filename} for LC detection")
        return filepath
    except Exception as e:
        error_msg = f"Error saving primary document: {e}"
        logger.error(error_msg)
        st.error(error_msg)
        return None

def split_secondary_documents(content):
    """Split secondary documents using AI-based approach from the working document_name_cut.py"""
    logger.info("Starting AI-based secondary document splitting")
    
    if not content.strip():
        logger.warning("Secondary document content is empty")
        return []
    
    logger.debug(f"Secondary content size: {len(content)} characters")
    
    # Document list for AI classification (matching the working document_name_cut.py format)
    document_list = "\n".join([
        f"- {desc}: {desc}" for code, desc in DOCUMENT_OPTIONS
    ])
    
    # Add specific document types that are commonly found
    additional_docs = [
        "- Insurance Certificate: Insurance Certificate",
        "- Bill of Lading: Bill of Lading", 
        "- Commercial Invoice: Commercial Invoice",
        "- Packing List: Packing List",
        "- Certificate of Origin: Certificate of Origin",
        "- Quality Certificate: Quality Certificate",
    ]
    document_list += "\n" + "\n".join(additional_docs)
    
    # Improved prompt for semantic detection
    prompt = f"""You are a trade finance document classifier.

Here is a list of document types and their descriptions:
{document_list}

The input text is:
{content}

Parse the text into individual document snippets. If there are bold headings like **Heading**, use them to separate and use the heading as the 'heading' (without **). If not, separate based on content where each document starts with specific fields like 'Invoice No:' or 'LC No:' etc., and generate headings like 'Document 1', 'Document 2', etc.

If no match, use "Unknown".

Output only a JSON array of objects: [{{"heading": "the heading", "content": "the snippet text", "identified_name": "the name"}} , ...]
"""

    try:
        logger.info("Sending content to Azure OpenAI for document splitting")
        
        # Initialize Azure OpenAI client
        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        )
        
        chat_deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT", "gpt-4o")
        
        response = client.chat.completions.create(
            model=chat_deployment,
            messages=[
                {"role": "system", "content": "You are a careful assistant. Output ONLY valid JSON. No commentary."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        result = response.choices[0].message.content
        
        # Parse JSON response
        try:
            documents = json.loads(result)
            logger.info(f"Successfully parsed JSON response with {len(documents)} documents")
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse AI response as JSON: {e}")
            logger.debug(f"Raw response: {result}")
            return []
        
        # Normalize names first-pass
        def normalize_name(name):
            n = (name or "").lower()
            if "lading" in n or "b/l" in n or "ocean" in n:
                return "Bill of Lading"
            if "insurance" in n or "policy" in n or "cargo" in n:
                return "Insurance Certificate"
            if "invoice" in n:
                return "Commercial Invoice"
            if "packing" in n or "weight" in n:
                return "Packing List"
            if "origin" in n or "coo" in n:
                return "Certificate of Origin"
            if "quality" in n or "inspection" in n:
                return "Quality Certificate"
            if "credit" in n or "lc" in n:
                return "Letter of Credit"
            return name
        
        for d in documents:
            d["identified_name"] = normalize_name(d.get("identified_name"))
        
        # Log identified documents
        for i, doc in enumerate(documents, 1):
            heading = doc.get('heading', 'Unknown')
            identified_name = doc.get('identified_name', 'Unknown')
            content_length = len(doc.get('content', ''))
            logger.debug(f"AI identified document: {heading} -> {identified_name}")
        
        logger.info(f"AI-based document splitting completed. Found {len(documents)} documents")
        for i, doc in enumerate(documents, 1):
            heading = doc.get('heading', 'Unknown')
            identified_name = doc.get('identified_name', 'Unknown')
            content_length = len(doc.get('content', ''))
            logger.info(f"Document {i}: {heading} ({identified_name}) - {content_length} chars")
        
        return documents
        
    except Exception as e:
        error_msg = f"Error in AI-based document splitting: {e}"
        logger.error(error_msg, exc_info=True)
        st.error(error_msg)
        return []

def ai_verify_and_correct_document_names(documents):
    """
    Recheck AI-identified document names using a verification LLM call.
    Ensures semantic correction for Bill of Lading, Insurance, Invoice, etc.
    """
    logger.info("Starting AI-based verification of document names")
    
    if not documents:
        logger.warning("No documents to verify")
        return documents

    # Build a short prompt for each document
    verified_docs = []
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    )
    chat_deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT", "gpt-4o-mini")

    for i, doc in enumerate(documents, 1):
        heading = doc.get("heading", f"Document {i}")
        snippet = doc.get("content", "")[:1000]  # Limit context
        old_name = doc.get("identified_name", "Unknown")

        prompt = f'''
You are an AI trade finance document verifier.

The following text is an excerpt from a trade finance document.

Snippet:
"""{snippet}"""

The system initially identified it as: "{old_name}"

Your task:
- Verify if the name is correct.
- If it's wrong, correct it based on actual content clues.
- Only choose from these document types:
  ["Letter of Credit", "Commercial Invoice", "Packing List", "Bill of Lading", "Insurance Certificate", "Certificate of Origin", "Quality Certificate", "Inspection Certificate", "Other/Unknown"]

Respond ONLY in this JSON format:
{{"verified_name": "<best matching document name>"}}
'''

        try:
            response = client.chat.completions.create(
                model=chat_deployment,
                messages=[
                    {"role": "system", "content": "You are a careful AI verifier. Output only JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0
            )

            result = response.choices[0].message.content.strip()
            try:
                verified_json = json.loads(result)
                verified_name = verified_json.get("verified_name", old_name)
            except json.JSONDecodeError:
                logger.warning(f"Could not parse verification response for {heading}. Using old name.")
                verified_name = old_name

            # Normalize to standard trade names
            name_lower = (verified_name or "").lower()
            if "lading" in name_lower or "b/l" in name_lower or "ocean" in name_lower:
                verified_name = "Bill of Lading"
            elif "insurance" in name_lower or "policy" in name_lower or "cargo" in name_lower:
                verified_name = "Insurance Certificate"
            elif "invoice" in name_lower:
                verified_name = "Commercial Invoice"
            elif "packing" in name_lower or "weight" in name_lower:
                verified_name = "Packing List"
            elif "origin" in name_lower or "coo" in name_lower:
                verified_name = "Certificate of Origin"
            elif "quality" in name_lower or "inspection" in name_lower:
                verified_name = "Quality Certificate"
            elif "credit" in name_lower or "lc" in name_lower:
                verified_name = "Letter of Credit"

            doc["verified_name"] = verified_name
            verified_docs.append(doc)
            logger.info(f"✅ Verified {heading}: {old_name} → {verified_name}")

        except Exception as e:
            logger.error(f"Verification error for {heading}: {e}")
            doc["verified_name"] = old_name
            verified_docs.append(doc)

    logger.info(f"Verification completed for {len(verified_docs)} documents")
    return verified_docs


def save_secondary_documents(documents):
    """Save secondary documents as separate files with proper headings for cross_new_csv.py"""
    logger.info(f"Saving {len(documents)} secondary documents")
    saved_files = []

    for i, doc in enumerate(documents, 1):
        # Prefer verified name if present
        identified_name = doc.get("verified_name") or doc.get("identified_name", "Unknown")
        heading = doc.get("heading", f"Document {i}")

        # Build safe filename from the FIRST THREE WORDS of the heading
        base_name = first_n_words(heading, 3)
        safe_base = sanitize_filename(base_name)
        if not safe_base:
            # Fallback to identified name
            safe_base = sanitize_filename(first_n_words(identified_name, 3)) or f"document_{i:02d}"
        filename = f"{safe_base}.txt"
        filepath = Path("input") / filename

        # Ensure uniqueness if a file with same name already exists
        counter = 2
        while filepath.exists():
            filename = f"{safe_base}_{counter}.txt"
            filepath = Path("input") / filename
            counter += 1

        # Determine document type for proper heading (matching cross_new_csv.py logic)
        doc_type = determine_document_type_for_heading(identified_name, filename)

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                # Write the file heading that cross_new_csv.py expects
                
                f.write(f"### {doc_type}: {filename}\n\n")

                f.write(doc.get("content", ""))

            saved_files.append({
                "filename": filename,
                "heading": heading,
                "identified_name": identified_name,
                "document_type": doc_type,
                "filepath": filepath
            })

            logger.info(f"Saved secondary document: {filename} ({identified_name}) with heading: {doc_type}")

        except Exception as e:
            error_msg = f"Error saving secondary document {i}: {e}"
            logger.error(error_msg)
            st.error(error_msg)

    logger.info(f"Successfully saved {len(saved_files)} secondary documents")
    return saved_files

def determine_document_type_for_heading(identified_name, filename):
    """Determine document type heading format that cross_new_csv.py expects"""
    identified_lower = identified_name.lower()
    filename_lower = filename.lower()

    # Bill of Lading — cover all variants like "Ocean Bill", "B/L"
    if any(x in identified_lower for x in ['ocean bill of lading', 'bill of lading', 'b/l', 'bol', 'lading', 'ocean']):
        return "Bill of Lading (BOL)"

    # Insurance — detect certificates, cargo, or policy
    elif any(x in identified_lower for x in ['insurance', 'ins', 'policy', 'cargo']):
        return "Insurance Certificate (INS)"

    # Invoices
    elif any(x in identified_lower for x in ['commercial invoice', 'invoice', 'inv']):
        return "Commercial Invoice (INV)"

    # Packing
    elif any(x in identified_lower for x in ['packing list', 'packing', 'pack', 'list']):
        return "Packing List (PL)"

    # Quality / Inspection
    elif any(x in identified_lower for x in ['quality', 'inspection']):
        return "Quality Certificate (QC)"

    # Certificates of Origin — strictly match COO terms only
    elif any(x in identified_lower for x in ['certificate of origin', 'coo', 'origin certificate']):
        return "Certificate of Origin (COO)"

    # Letters of Credit
    elif any(x in identified_lower for x in ['letter of credit', 'credit', 'lc']):
        return "Letter of Credit (LC)"

    else:
        return f"Trade Document ({identified_name})"

def run_discrepancy_analysis():
    """Run the cross_new_csv.py script for discrepancy analysis"""
    logger.info("Starting discrepancy analysis")
    
    try:
        # Check if the analysis script exists
        script_path = Path("cross_new_csv.py")
        logger.info(f"Checking for analysis script: {script_path}")
        
        if not script_path.exists():
            error_msg = f"Analysis script not found: {script_path}"
            logger.error(error_msg)
            st.error(error_msg)
            return None, None
        
        logger.info("Analysis script found, preparing to execute")
        
        # List input files for logging
        input_files = list(Path("input").glob("*.txt"))
        input_filenames = [f.name for f in input_files]
        logger.info(f"Input files for analysis: {input_filenames}")
        
        # Execute the script
        logger.info("Executing cross_new_csv.py script")
        result = subprocess.run(
            [sys.executable, "cross_new_csv.py"],
            capture_output=True,
            text=True,
            cwd=Path.cwd()
        )
        
        logger.info(f"Script execution completed with return code: {result.returncode}")
        
        if result.stdout:
            logger.info(f"Script stdout: {result.stdout}")
        if result.stderr:
            logger.warning(f"Script stderr: {result.stderr}")
        
        # Look for output files even if return code is not 0
        output_dir = Path("output")
        md_files = list(output_dir.glob("compliance_analysis_*.md"))
        csv_files = list(output_dir.glob("compliance_analysis_*.csv"))
        
        md_file = None
        csv_file = None
        
        if md_files:
            md_file = max(md_files, key=os.path.getctime)
            logger.info(f"Found analysis report: {md_file}")
        
        if csv_files:
            csv_file = max(csv_files, key=os.path.getctime)
            logger.info(f"Found analysis CSV: {csv_file}")
        
        if result.returncode != 0:
            logger.error(f"Error running analysis script (return code {result.returncode}): {result.stderr}")
            # Still return files if they exist
            return md_file, csv_file
        
        logger.info("Discrepancy analysis completed successfully")
        return md_file, csv_file
        
    except Exception as e:
        error_msg = f"Exception during analysis execution: {e}"
        logger.error(error_msg, exc_info=True)
        st.error(error_msg)
        return None, None

def display_file_content(filepath, file_type="text"):
    """Display file content in Streamlit with proper error handling"""
    try:
        logger.info(f"Displaying file content: {filepath} (type: {file_type})")
        
        if file_type == "csv":
            # Display CSV as a dataframe
            df = pd.read_csv(filepath, encoding='utf-8')
            st.dataframe(df, use_container_width=True)
            logger.info(f"Successfully displayed CSV with {len(df)} rows")
        else:
            # Display text content with fallback encoding
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                # Fallback to different encoding if UTF-8 fails
                with open(filepath, 'r', encoding='latin-1') as f:
                    content = f.read()
                logger.warning(f"Used latin-1 encoding for {filepath}")
            
            st.markdown(content)
            logger.info(f"Successfully displayed text content ({len(content)} characters)")
            
    except Exception as e:
        error_msg = f"Error reading file {filepath}: {e}"
        logger.error(error_msg)
        st.error(error_msg)

# Main application
def main():
    """Main Streamlit application"""
    # Setup logging
    current_log_file = setup_audit_logging()
    logger.info("=== STARTING MAIN APPLICATION ===")
    
    # Create directories
    create_directories()
    
    # Validate configuration
    config_valid, config_msg = validate_azure_config()
    if not config_valid:
        st.error(f"❌ Configuration Error: {config_msg}")
        st.stop()
    
    logger.info("Application initialization completed")
    
    # Page configuration
    st.set_page_config(
        page_title="Trade Finance Document Analyzer",
        page_icon="📊",
        layout="wide"
    )
    
    # Header
    st.title("📊 Trade Finance Document Analyzer")
    st.markdown("Automated discrepancy analysis for trade finance documents using AI")
    
    # Sidebar configuration
    with st.sidebar:
        st.header("🔧 Configuration")
        
        # Azure OpenAI status
        if config_valid:
            st.success("✅ Azure OpenAI Connected")
            endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "")
            if endpoint:
                domain = endpoint.split("//")[-1].split("/")[0]
                st.info(f"**Model:** {os.getenv('AZURE_OPENAI_CHAT_DEPLOYMENT', 'gpt-4o')}")
                st.info(f"**Version:** {os.getenv('AZURE_OPENAI_API_VERSION', '2024-02-01')}")
                st.info(f"**Endpoint:** {domain}")
        
        st.markdown("---")
        
        # Audit log section
        st.header("📋 Audit Log")
        st.info(f"**Current Log:** {current_log_file.name}")
        
        # Download current log
        try:
            with open(current_log_file, 'r', encoding='utf-8') as f:
                log_content = f.read()
            st.download_button(
                label="📥 Download Current Log",
                data=log_content,
                file_name=current_log_file.name,
                mime="text/plain"
            )
        except Exception as e:
            st.warning(f"Could not read log file: {e}")
    
    # Main content
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("📄 Primary Document (Golden Truth)")
        st.markdown("Select the document type and paste the primary document content.")
        
        # Document type dropdown
        document_code = st.selectbox(
            "Document Type",
            options=[code for code, desc in DOCUMENT_OPTIONS],
            format_func=lambda x: f"{x} - {next(desc for code, desc in DOCUMENT_OPTIONS if code == x)}",
            help="Select the type of primary document (Letter of Credit, etc.)"
        )
        
        # Primary document text area
        primary_content = st.text_area(
            "Primary Document Content",
            height=300,
            placeholder="Paste your primary document content here...",
            help="This document will serve as the golden truth for comparison"
        )
    
    with col2:
        st.header("📋 Secondary Documents")
        st.markdown("Paste multiple secondary documents that will be compared against the primary document.")
        
        # Secondary documents text area
        secondary_content = st.text_area(
            "Secondary Documents Content",
            height=300,
            placeholder="Paste your secondary documents here (insurance certificate, bill of lading, etc.)...",
            help="Multiple documents will be automatically separated and analyzed"
        )
        
        # Preview section
        if secondary_content.strip():
            with st.expander("📋 Preview Document Splitting"):
                with st.spinner("Analyzing documents..."):
                    preview_docs = split_secondary_documents(secondary_content)
                    
                    if preview_docs:
                        # Verify names in preview as well for accuracy
                        preview_verified = ai_verify_and_correct_document_names(preview_docs)
                        st.success(f"✅ Found {len(preview_verified)} documents (verified)")
                        for i, doc in enumerate(preview_verified, 1):
                            st.write(f"**Document {i}:** {doc['heading']}")
                            st.write(f"**Identified as:** {doc.get('verified_name') or doc.get('identified_name', 'Unknown')}")
                            st.write(f"**Content preview:** {doc['content'][:100]}...")
                            st.write("---")
                    else:
                        st.warning("⚠️ No documents detected. Try adding clear headings or separators.")
    
    # Analysis section
    st.markdown("---")
    
    if st.button("🔍 Analyze Documents", type="primary", use_container_width=True):
        if not primary_content.strip():
            st.error("❌ Please provide primary document content")
            return
        
        if not secondary_content.strip():
            st.error("❌ Please provide secondary document content")
            return
        
        # Clean previous files
        clean_input_directory()
        
        # Save primary document
        primary_file = save_primary_document(primary_content, document_code)
        if not primary_file:
            st.error("❌ Failed to save primary document")
            return
        
        # Split and VERIFY secondary documents
        secondary_docs = split_secondary_documents(secondary_content)
        if not secondary_docs:
            st.error("❌ Failed to split secondary documents")
            return

        with st.spinner("Verifying document classifications..."):
            verified_docs = ai_verify_and_correct_document_names(secondary_docs)
            if verified_docs:
                st.success(f"✅ Verified document names for {len(verified_docs)} items")
            else:
                verified_docs = secondary_docs
                st.warning("⚠️ Verification fallback used")
        
        saved_secondary = save_secondary_documents(verified_docs)
        if not saved_secondary:
            st.error("❌ Failed to save secondary documents")
            return
        
        # Show processing summary
        st.success(f"✅ Processed {len(saved_secondary)} secondary documents")
        
        with st.expander("📁 Files Created"):
            st.write(f"**Primary:** {primary_file.name}")
            st.write(f"   📄 Letter of Credit (LC) - GOLDEN TRUTH DOCUMENT")
            st.write("---")
            for file_info in saved_secondary:
                identified = file_info.get('identified_name', 'Unknown')
                doc_type = file_info.get('document_type', 'Unknown')
                st.write(f"**Secondary:** {file_info['filename']}")
                st.write(f"   📄 {file_info['heading']}")
                st.write(f"   🏷️ Identified as: {identified}")
                st.write(f"   📋 File heading: {doc_type}")
                st.write("---")
        
        # Run analysis
        with st.spinner("Running discrepancy analysis..."):
            md_file, csv_file = run_discrepancy_analysis()
            
            # Check if analysis files were created even if there was an error
            output_dir = Path("output")
            if not md_file or not csv_file:
                # Look for any analysis files that might have been created
                md_files = list(output_dir.glob("compliance_analysis_*.md"))
                csv_files = list(output_dir.glob("compliance_analysis_*.csv"))
                
                if md_files:
                    md_file = max(md_files, key=os.path.getctime)
                    logger.info(f"Found analysis MD file despite error: {md_file}")
                
                if csv_files:
                    csv_file = max(csv_files, key=os.path.getctime)
                    logger.info(f"Found analysis CSV: {csv_file}")
            
            if md_file and md_file.exists():
                st.success("✅ Analysis completed successfully!")
                
                # Display results in tabs
                tab1, tab2 = st.tabs(["📄 Detailed Report", "📊 CSV Summary"])
                
                with tab1:
                    st.header("Discrepancy Analysis Report")
                    display_file_content(md_file, "text")
                    
                    # Download button for markdown
                    try:
                        with open(md_file, 'r', encoding='utf-8') as f:
                            md_content = f.read()
                        st.download_button(
                            label="📥 Download Report (MD)",
                            data=md_content,
                            file_name=md_file.name,
                            mime="text/markdown"
                        )
                    except Exception as e:
                        logger.warning(f"Could not create download button for MD: {e}")
                
                with tab2:
                    st.header("Discrepancy Summary Table")
                    if csv_file and csv_file.exists():
                        display_file_content(csv_file, "csv")
                        
                        # Download button for CSV
                        try:
                            with open(csv_file, 'rb') as f:
                                csv_content = f.read()
                            st.download_button(
                                label="📥 Download CSV",
                                data=csv_content,
                                file_name=csv_file.name,
                                mime="text/csv"
                            )
                        except Exception as e:
                            logger.warning(f"Could not create download button for CSV: {e}")
                    else:
                        st.info("CSV summary not available for this analysis.")
            else:
                st.error("❌ Analysis failed. Please check your documents and try again.")
                st.info("💡 Check the audit log for detailed error information.")

if __name__ == "__main__":
    main()
