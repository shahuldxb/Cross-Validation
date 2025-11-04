# Trade Finance Document Analyzer

A Streamlit application for analyzing trade finance documents and identifying discrepancies between primary and secondary documents.

## Features

- **Two Text Input Areas**: 
  - Primary Document (Golden Truth) with document type selection
  - Secondary Documents for comparison
- **Document Type Dropdown**: 18 different trade finance document types
- **Automated Document Processing**: Splits secondary documents and saves them as individual files
- **Discrepancy Analysis**: Uses AI to identify inconsistencies between documents
- **Results Display**: Shows detailed reports and CSV summaries in large, readable windows

## Installation

1. Install required dependencies:
```bash
pip install streamlit pandas openpyxl
```

2. Ensure you have the following files in your directory:
   - `trade_finance_app.py` (main application)
   - `cross_new_csv.py` (discrepancy analysis script)
   - `document_name_cut.py` (document processing script)

## Usage

1. Start the application:
```bash
streamlit run trade_finance_app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. **Primary Document Section**:
   - Select the document type from the dropdown (ILC, ELC, SLC, etc.)
   - Paste your primary document content (Letter of Credit, etc.)

4. **Secondary Documents Section**:
   - Paste all secondary documents (invoices, bills of lading, certificates, etc.)
   - Separate documents with clear headings or double line breaks

5. Click **"🔍 Analyze Documents"** to process

6. View results in two tabs:
   - **Detailed Report**: Complete markdown analysis
   - **CSV Summary**: Tabular discrepancy data

## Document Types Supported

| Code | Description |
|------|-------------|
| ILC | Import Letter of Credit |
| ELC | Export Letter of Credit |
| SLC | Sight Letter of Credit |
| ULC | Usance Letter of Credit |
| RLC | Revolving Letter of Credit |
| TLC | Transferable Letter of Credit |
| BBLC | Back-to-Back Letter of Credit |
| SBLC | Standby Letter of Credit |
| RCLC | Red Clause Letter of Credit |
| GCLC | Green Clause Letter of Credit |
| IBC | Import Bills for Collection |
| EBC | Export Bills for Collection |
| BG | Bank Guarantee |
| SG | Shipping Guarantee |
| PG | Performance Guarantee |
| APG | Advance Payment Guarantee |
| BB | Bid Bond |
| RG | Retention Guarantee |

## File Structure

The application creates the following directories:
- `input/` - Stores processed document files
- `output/` - Contains analysis results (markdown and CSV files)

## Key Features

1. **Dynamic File Naming**: Primary document is saved as `{DocumentCode}.txt` (e.g., `ILC.txt`)
2. **Intelligent Document Splitting**: Automatically separates secondary documents
3. **Cross-Document Analysis**: Compares all secondary documents against the primary document
4. **Professional UI**: Clean, intuitive interface with helpful instructions
5. **Download Options**: Export both detailed reports and CSV summaries

## Notes

- The primary document serves as the "golden truth" for all comparisons
- Secondary documents are automatically split using various heuristics
- Analysis results include both detailed explanations and structured data
- All file operations are Windows-compatible
