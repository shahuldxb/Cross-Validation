# Trade Finance Compliance Analysis Report
**Generated:** 2025-11-04 15:02:46
**Base Document (Golden Truth):** ilc.txt
**Secondary Documents Analyzed:** 5 files

## Documents Processed:
- **Golden Truth:** ilc.txt
- **Secondary 1:** BILL OF LADING.txt
- **Secondary 2:** COMMERCIAL INVOICE.txt
- **Secondary 3:** INSURANCE CERTIFICATE.txt
- **Secondary 4:** PACKING LIST.txt
- **Secondary 5:** QUALITY CERTIFICATE.txt

---

## Compliance Analysis Results:

### Markdown Table of Discrepancies

| Base Document | Target Document | Field(s) | Base Value | Target Value | Issue |
|---------------|-----------------|----------|------------|--------------|-------|
| Letter of Credit | Bill of Lading | Net Weight | 4,000.00 kg | 3,998.00 kg | Net weight discrepancy. |
| Letter of Credit | Bill of Lading | Latest Shipment Date | 25-Sep-2025 | 26-Sep-2025 | Shipment date exceeds the latest shipment date allowed by LC. |
| Letter of Credit | Commercial Invoice | Goods Description | 100% cotton | 97% cotton / 3% elastane | Goods description does not match LC requirements. |
| Letter of Credit | Commercial Invoice | Quantity | 400 cartons | 350 cartons | Quantity discrepancy. |
| Letter of Credit | Packing List | Quantity | 400 cartons | 349 cartons | Quantity discrepancy in packing list. |
| Letter of Credit | Packing List | Gross Weight | 4,200.00 kg | 4,198.00 kg | Gross weight discrepancy. |
| Letter of Credit | Packing List | Net Weight | 4,000.00 kg | 3,998.00 kg | Net weight discrepancy. |
| Letter of Credit | Insurance Certificate | Coverage Clauses | Institute Cargo Clauses (C) | Institute Cargo Clauses (A) | Coverage clause mismatch. |
| Letter of Credit | Insurance Certificate | Claims Payable | Vietnam | Dubai, United Arab Emirates | Claims payable location does not match LC requirements. |
| Letter of Credit | Quality Certificate | Buyer Specification | VGE/KT-2025-09 | VGE/KT-2025-09 (Rev A) | Buyer specification revision mismatch. |
---

### Detailed Analysis

**GOLDEN TRUTH DOCUMENT:** Irrevocable Letter of Credit (LC) - ilc.txt  
**SECONDARY DOCUMENTS FOUND:**  
1. Bill of Lading (BOL) - BILL OF LADING.txt
2. Commercial Invoice (INV) - COMMERCIAL INVOICE.txt
3. Insurance Certificate (INS) - INSURANCE CERTIFICATE.txt
4. Packing List (PL) - PACKING LIST.txt
5. Quality Certificate (QC) - QUALITY CERTIFICATE.txt  

**TOTAL DISCREPANCIES FOUND:** 10  

---

#### Serial ID: 1  
Type: Quantity Discrepancy  
Discrepancy ID: QT-001  
Discrepancy Title: Net Weight Mismatch Between LC and Bill of Lading  
Discrepancy Short Detail: Net weight in LC differs from Bill of Lading by 2.00 kg.  
Discrepancy Long Detail: The Letter of Credit specifies a net weight of 4,000.00 kg, while the Bill of Lading indicates 3,998.00 kg. This discrepancy may lead to compliance issues or rejection by the issuing bank due to non-conformance with LC terms.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Net Weight: 4,000.00 kg  
  - Target (Bill of Lading): Net Weight: 3,998.00 kg  
  - Difference: Net weight is short by 2.00 kg in the Bill of Lading compared to the LC.  
Severity Level: Medium  
Golden Truth Value: 4,000.00 kg  
Secondary Document Value: 3,998.00 kg  
Impact: The discrepancy could result in payment delays or rejection of documents, potentially affecting shipment release and trade terms compliance.
---
#### Serial ID: 2  
Type: Shipment Date Discrepancy  
Discrepancy ID: SD-002  
Discrepancy Title: Shipment Date Exceeds LC Allowance  
Discrepancy Short Detail: Shipment date on Bill of Lading exceeds LC's latest shipment date.  
Discrepancy Long Detail: The Letter of Credit specifies the latest shipment date as 25-Sep-2025, but the Bill of Lading indicates a shipment date of 26-Sep-2025. This discrepancy violates the LC terms and may lead to non-compliance, risking rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Latest Shipment Date: 25-Sep-2025  
  - Target (Bill of Lading): Latest Shipment Date: 26-Sep-2025  
  - Difference: Shipment date on the Bill of Lading is one day later than the LC's allowed date.  
Severity Level: High  
Golden Truth Value: 25-Sep-2025  
Secondary Document Value: 26-Sep-2025  
Impact: The discrepancy may result in refusal of payment under the LC, causing financial and operational delays.
---
#### Serial ID: 3  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-003  
Discrepancy Title: Mismatch in Goods Description Between LC and Invoice  
Discrepancy Short Detail: Goods description in the invoice does not match the LC requirements.  
Discrepancy Long Detail: The Letter of Credit specifies the goods as "100% cotton," while the Commercial Invoice describes them as "97% cotton / 3% elastane." This discrepancy indicates non-compliance with the LC terms, which may lead to rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Goods Description: 100% cotton  
  - Target (Commercial Invoice): Goods Description: 97% cotton / 3% elastane  
  - Difference: The goods description in the invoice includes a blend of materials (cotton and elastane), which does not conform to the LC requirement of 100% cotton.  
Severity Level: High  
Golden Truth Value: 100% cotton  
Secondary Document Value: 97% cotton / 3% elastane  
Impact: The discrepancy may result in the issuing bank refusing to honor the payment under the LC, causing delays or financial loss.
---
#### Serial ID: 4  
Type: Quantity Discrepancy  
Discrepancy ID: QT-004  
Discrepancy Title: Mismatch in Quantity of Cartons  
Discrepancy Short Detail: Quantity in LC is 400 cartons, but invoice states 350 cartons.  
Discrepancy Long Detail: The Letter of Credit specifies a shipment quantity of 400 cartons, while the Commercial Invoice lists only 350 cartons. This discrepancy may lead to non-compliance with LC terms and potential rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Quantity: 400 cartons  
  - Target (Commercial Invoice): Quantity: 350 cartons  
  - Difference: 50 cartons shortfall in the invoice compared to LC.  
Severity Level: Medium  
Golden Truth Value: 400 cartons  
Secondary Document Value: 350 cartons  
Impact: The discrepancy could result in payment delays or refusal by the bank, requiring clarification or amendment to resolve.
---
#### Serial ID: 5  
Type: Quantity Discrepancy  
Discrepancy ID: QT-005  
Discrepancy Title: Mismatch in Carton Quantity Between LC and Packing List  
Discrepancy Short Detail: Packing list shows 349 cartons, while LC specifies 400 cartons.  
Discrepancy Long Detail: The Letter of Credit indicates a shipment quantity of 400 cartons, but the packing list reflects only 349 cartons. This discrepancy may lead to non-compliance with LC terms and potential rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Quantity: 400 cartons  
  - Target (Packing List): Quantity: 349 cartons  
  - Difference: 51 cartons shortfall in the packing list compared to LC.  
Severity Level: Medium  
Golden Truth Value: 400 cartons  
Secondary Document Value: 349 cartons  
Impact: The discrepancy could result in payment delays or refusal by the issuing bank, affecting shipment acceptance and financial settlement.
---
#### Serial ID: 6  
Type: Quantity Discrepancy  
Discrepancy ID: QT-006  
Discrepancy Title: Gross Weight Mismatch Between LC and Packing List  
Discrepancy Short Detail: Gross weight differs by 2.00 kg between LC and Packing List.  
Discrepancy Long Detail: The Letter of Credit specifies a gross weight of 4,200.00 kg, while the Packing List indicates 4,198.00 kg. This discrepancy may lead to compliance issues or rejection by the issuing bank due to non-conformance with LC terms.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Gross Weight: 4,200.00 kg  
  - Target (Packing List): Gross Weight: 4,198.00 kg  
  - Difference: Gross weight mismatch of 2.00 kg.  
Severity Level: Medium  
Golden Truth Value: 4,200.00 kg  
Secondary Document Value: 4,198.00 kg  
Impact: The discrepancy could result in payment delays or refusal by the issuing bank, requiring clarification or amendment to resolve.
---
#### Serial ID: 7  
Type: Quantity Discrepancy  
Discrepancy ID: QT-007  
Discrepancy Title: Net Weight Mismatch Between LC and Packing List  
Discrepancy Short Detail: Net weight in LC and Packing List differs by 2.00 kg.  
Discrepancy Long Detail: The Letter of Credit specifies a net weight of 4,000.00 kg, while the Packing List indicates 3,998.00 kg. This discrepancy may lead to compliance issues or rejection by the issuing bank due to non-conformance with LC terms.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Net Weight: 4,000.00 kg  
  - Target (Packing List): Net Weight: 3,998.00 kg  
  - Difference: Net weight is 2.00 kg less in the Packing List compared to the LC.  
Severity Level: Medium  
Golden Truth Value: 4,000.00 kg  
Secondary Document Value: 3,998.00 kg  
Impact: This discrepancy could result in delays or rejection of the documents by the issuing bank, potentially affecting payment processing.
---
#### Serial ID: 8  
Type: Coverage Clause Discrepancy  
Discrepancy ID: CC-008  
Discrepancy Title: Coverage Clause Mismatch Between LC and Insurance Certificate  
Discrepancy Short Detail: Coverage clauses differ between LC and insurance certificate.  
Discrepancy Long Detail: The Letter of Credit specifies Institute Cargo Clauses (C), while the Insurance Certificate lists Institute Cargo Clauses (A). This mismatch may lead to non-compliance with LC terms and potential rejection of documents.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Coverage Clauses: Institute Cargo Clauses (C)  
  - Target (Insurance Certificate): Coverage Clauses: Institute Cargo Clauses (A)  
  - Difference: The LC requires a more restrictive coverage clause (C), while the insurance certificate provides broader coverage (A), creating a compliance gap.  
Severity Level: Medium  
Golden Truth Value: Institute Cargo Clauses (C)  
Secondary Document Value: Institute Cargo Clauses (A)  
Impact: The discrepancy may result in refusal of the insurance certificate by the issuing bank, delaying payment and shipment processing.
---
#### Serial ID: 9  
Type: Claims Payable Location Discrepancy  
Discrepancy ID: CP-009  
Discrepancy Title: Mismatch in Claims Payable Location  
Discrepancy Short Detail: Claims payable location differs between LC and insurance certificate.  
Discrepancy Long Detail: The Letter of Credit specifies Vietnam as the claims payable location, while the insurance certificate lists Dubai, United Arab Emirates. This mismatch violates LC requirements and may lead to non-compliance issues.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Claims Payable: Vietnam  
  - Target (Insurance Certificate): Claims Payable: Dubai, United Arab Emirates  
  - Difference: The claims payable location in the insurance certificate does not align with the LC's stipulated location.  
Severity Level: Medium  
Golden Truth Value: Vietnam  
Secondary Document Value: Dubai, United Arab Emirates  
Impact: This discrepancy may result in rejection of the documents by the issuing bank, delaying payment and potentially causing financial and operational risks.  
---
#### Serial ID: 10  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-010  
Discrepancy Title: Buyer Specification Revision Mismatch  
Discrepancy Short Detail: Buyer specification in LC differs from Quality Certificate revision.  
Discrepancy Long Detail: The Letter of Credit specifies "VGE/KT-2025-09," while the Quality Certificate lists "VGE/KT-2025-09 (Rev A)." This indicates a revision mismatch in buyer specification, which may lead to compliance issues or rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Buyer Specification: VGE/KT-2025-09  
  - Target (Quality Certificate): Buyer Specification: VGE/KT-2025-09 (Rev A)  
  - Difference: The target document includes a revision identifier "(Rev A)" not present in the base document.  
Severity Level: Medium  
Golden Truth Value: VGE/KT-2025-09  
Secondary Document Value: VGE/KT-2025-09 (Rev A)  
Impact: The mismatch may result in delays or rejection of the Quality Certificate, as the issuing bank could deem the revision unauthorized or non-compliant.
