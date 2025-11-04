import streamlit as st
import pandas as pd
import os
import json
import re
from datetime import datetime
from dotenv import load_dotenv
from openai import AzureOpenAI

# -----------------------------
# Load env vars from .env only
# -----------------------------
load_dotenv()  # expects a .env in the working dir

def get_env(name: str, required=True, default=None):
    v = os.getenv(name, default)
    if required and not v:
        st.error(f"Missing env var: {name}")
        st.stop()
    return v

AZURE_OPENAI_ENDPOINT = get_env("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = get_env("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = get_env("AZURE_OPENAI_API_VERSION", required=False, default="2024-02-01")
AZURE_OPENAI_CHAT_DEPLOYMENT = get_env("AZURE_OPENAI_CHAT_DEPLOYMENT")

client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
)

# -----------------------------
# Paths
# -----------------------------
DOCS_DIR = "./"
EXCEL_FILE = os.path.join(DOCS_DIR, "trade_finance_documents.xlsx")
OUT_DIR = "./out"

# -----------------------------
# Utilities
# -----------------------------
def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def slugify(text: str, max_len: int = 60) -> str:
    text = (text or "").strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    text = re.sub(r"^-+|-+$", "", text)
    return text[:max_len] if text else "untitled"

def safe_json_loads(s: str):
    s = (s or "").strip()
    if s.startswith("```json"):
        s = s[7:].strip()
    if s.endswith("```"):
        s = s[:-3].strip()
    obj = json.loads(s)
    if isinstance(obj, dict):
        obj = [obj]
    if not isinstance(obj, list):
        raise ValueError("Model did not return a JSON array.")
    return obj

# -----------------------------
# Load master document list
# -----------------------------
try:
    master_df = pd.read_excel(EXCEL_FILE)
except FileNotFoundError:
    st.error(f"Excel file not found at {EXCEL_FILE}. Please ensure the file exists.")
    st.stop()
except Exception as e:
    st.error(f"Error loading Excel file: {e}")
    st.stop()

required_cols = {"DocumentName", "Description"}
missing = required_cols - set(master_df.columns)
if missing:
    st.error(f"Excel is missing columns: {', '.join(missing)}")
    st.stop()

# Optional column for codes
has_code_col = "DocumentCode" in master_df.columns

# Build name->code map (case-insensitive)
name_to_code = {}
if has_code_col:
    for _, r in master_df.iterrows():
        dn = str(r["DocumentName"]).strip().lower()
        dc = str(r["DocumentCode"]).strip() if pd.notna(r["DocumentCode"]) else ""
        if dn:
            name_to_code[dn] = dc or "UNK"

document_list = "\n".join(
    f"- {row['DocumentName']}: {row['Description']}" for _, row in master_df.iterrows()
)

# -----------------------------
# UI
# -----------------------------
st.title("Trade Finance Document Analyzer")
st.caption("Splits pasted text into document snippets, classifies them, and saves each snippet under ./out/<DocumentCode>-<IdentifiedName>/")

input_text = st.text_area("Input Text (paste the document snippets here)", height=300)

colA, colB = st.columns(2)
with colA:
    write_files = st.checkbox("Write snippets to ./out", value=True)
with colB:
    export_manifest = st.checkbox("Export manifest (CSV + JSON) to ./out", value=True)

if st.button("Analyze"):
    if not input_text.strip():
        st.info("Please paste some text.")
        st.stop()

    prompt = f"""You are a trade finance document classifier.

Here is a list of document types and their descriptions:
{document_list}

The input text is:
{input_text}

Parse the text into individual document snippets. If there are bold headings like **Heading**, use them to separate and use the heading as the 'heading' (without **). If not, separate based on content where each document starts with specific fields like 'Invoice No:' or 'LC No:' etc., and generate headings like 'Document 1', 'Document 2', etc.

For each snippet, identify the document name from the list that best matches the content.
If no match, use "Unknown".

Output only a JSON array of objects: [{{"heading": "the heading", "content": "the snippet text", "identified_name": "the name"}} , ...]
"""

    try:
        with st.spinner("Asking model…"):
            response = client.chat.completions.create(
                model=AZURE_OPENAI_CHAT_DEPLOYMENT,
                messages=[
                    {"role": "system", "content": "You are a careful assistant. Output ONLY valid JSON. No commentary."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0
            )

        data = safe_json_loads(response.choices[0].message.content)

        if not data:
            st.info("No document snippets identified.")
            st.stop()

        results_df = pd.DataFrame(data)
        st.subheader("Detected snippets")
        st.dataframe(results_df, use_container_width=True)

        # -----------------------------
        # Write snippets to ./out using <DocumentCode>-<Name> folder
        # -----------------------------
        written_files = []
        manifest_rows = []
        if write_files:
            ensure_dir(OUT_DIR)

            for idx, item in enumerate(data, start=1):
                heading = (item.get("heading") or f"Document {idx}").strip()
                content = (item.get("content") or "").strip()
                identified = (item.get("identified_name") or "Unknown").strip() or "Unknown"

                # Find document code from Excel mapping (case-insensitive match)
                code = "UNK"
                if has_code_col and identified:
                    code = name_to_code.get(identified.lower(), "UNK")

                # Folder name: <DocumentCode>-<IdentifiedNameSlug>
                folder_name = f"{code}-{slugify(identified)}"
                folder_path = os.path.join(OUT_DIR, folder_name)
                ensure_dir(folder_path)

                # File name inside folder (keep your existing pattern)
                file_name = f"{idx:02d}_{slugify(identified)}_{slugify(heading)}.txt"
                fpath = os.path.join(folder_path, file_name)

                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)

                written_files.append(fpath)
                manifest_rows.append({
                    "index": idx,
                    "heading": heading,
                    "identified_name": identified,
                    "document_code": code,
                    "folder": os.path.abspath(folder_path),
                    "file_path": os.path.abspath(fpath)
                })

            st.success(f"Wrote {len(written_files)} snippet file(s) into ./out/<DocumentCode>-<IdentifiedName>/ folders.")
            with st.expander("Show written files"):
                for p in written_files:
                    st.write(p)

        # -----------------------------
        # Export manifest
        # -----------------------------
        if export_manifest:
            ensure_dir(OUT_DIR)
            manifest_df = pd.DataFrame(manifest_rows) if manifest_rows else results_df.copy()
            csv_path = os.path.join(OUT_DIR, "manifest.csv")
            json_path = os.path.join(OUT_DIR, "manifest.json")

            manifest_df.to_csv(csv_path, index=False, encoding="utf-8")
            with open(json_path, "w", encoding="utf-8") as jf:
                json.dump(data, jf, ensure_ascii=False, indent=2)

            st.info(f"Manifest saved: {csv_path} and {json_path}")

    except json.JSONDecodeError:
        st.error("Error parsing JSON from model. Ensure the model outputs ONLY valid JSON.")
    except Exception as e:
        st.error(f"Error processing: {e}")

# -----------------------------
# Notes
# -----------------------------
# Files are saved to: ./out/<DocumentCode>-<IdentifiedNameSlug>/<01_identified_heading>.txt
# - DocumentCode is taken from the Excel column 'DocumentCode' if present, else 'UNK'.
# - IdentifiedNameSlug is a slugified version of the model's identified_name.
