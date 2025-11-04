# Trade Finance Compliance Analysis Report
**Generated:** 2025-10-27 12:33:13
**Base Document (Golden Truth):** ilc.txt
**Secondary Documents Analyzed:** 5 files

## Documents Processed:
- **Golden Truth:** ilc.txt
- **Secondary 1:** COMMERCIAL INVOICE.txt
- **Secondary 2:** INSURANCE CERTIFICATE POLICY.txt
- **Secondary 3:** OCEAN BILL OF.txt
- **Secondary 4:** PACKING LIST.txt
- **Secondary 5:** QUALITY CERTIFICATE.txt

---

## Compliance Analysis Results:

### Markdown Table of Discrepancies

| Base Document | Target Document | Field(s) | Base Value | Target Value | Issue |
|---------------|-----------------|----------|------------|--------------|-------|
| Letter of Credit | Commercial Invoice | Goods Description | Knitted cotton T‑shirts, 100% cotton | Knitted T‑shirts, 97% cotton / 3% elastane (short sleeve, crew neck) | Fiber content discrepancy; LC requires 100% cotton. |
| Letter of Credit | Commercial Invoice | Net Weight | 4,000.00 kg | 3,998.00 kg | Net weight discrepancy; LC specifies 4,000.00 kg. |
| Letter of Credit | Insurance Certificate | Coverage | Institute Cargo Clauses (C) | Institute Cargo Clauses (A) | Coverage discrepancy; LC requires Institute Cargo Clauses (C). |
| Letter of Credit | Insurance Certificate | Claims Payable | Vietnam | Dubai, United Arab Emirates | Claims payable location discrepancy; LC requires claims payable in Vietnam. |
| Letter of Credit | Bill of Lading | Shipped on Board Date | Not later than 25-Sep-2025 | 26-Sep-2025 | Shipped on board date exceeds the latest shipment date specified in the LC. |
| Letter of Credit | Packing List | Gross Weight | 4,200.00 kg | 4,198.00 kg | Gross weight discrepancy; LC specifies 4,200.00 kg. |
| Letter of Credit | Packing List | Cartons per Pallet | 50 pieces per carton | Pallet 7 contains 49 cartons | Quantity discrepancy; LC requires 50 pieces per carton for all pallets. |
| Letter of Credit | Certificate of Origin | Buyer Specification | VGE/KT-2025-09 | VGE/KT-2025-09 (Rev A) | Buyer specification discrepancy; LC specifies VGE/KT-2025-09 without "Rev A". |
---

### Detailed Analysis

**GOLDEN TRUTH DOCUMENT:** Irrevocable Letter of Credit (LC) - ilc.txt  
**SECONDARY DOCUMENTS FOUND:**  
1. Commercial Invoice (INV) - COMMERCIAL INVOICE.txt
2. Insurance Certificate (INS) - INSURANCE CERTIFICATE POLICY.txt
3. Bill of Lading (BOL) - OCEAN BILL OF.txt
4. Packing List (PL) - PACKING LIST.txt
5. Certificate of Origin (COO) - QUALITY CERTIFICATE.txt  

**TOTAL DISCREPANCIES FOUND:** 8  

---

#### Serial ID: 1  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-001  
Discrepancy Title: Fiber Content Mismatch in Goods Description  
Discrepancy Short Detail: Fiber content differs; LC specifies 100% cotton, invoice states 97% cotton / 3% elastane.  
Discrepancy Long Detail: The Letter of Credit mandates the goods to be 100% cotton, while the commercial invoice describes the goods as containing 97% cotton and 3% elastane. This deviation violates the LC terms and may lead to non-compliance or rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Goods Description: Knitted cotton T‑shirts, 100% cotton  
  - Target (Commercial Invoice): Goods Description: Knitted T‑shirts, 97% cotton / 3% elastane (short sleeve, crew neck)  
  - Difference: Fiber content mismatch; LC requires 100% cotton, invoice specifies a blend of cotton and elastane.  
Severity Level: High  
Golden Truth Value: Knitted cotton T‑shirts, 100% cotton  
Secondary Document Value: Knitted T‑shirts, 97% cotton / 3% elastane (short sleeve, crew neck)  
Impact: The discrepancy risks rejection of the documents by the issuing bank, potentially delaying payment and shipment processing.
---
#### Serial ID: 2  
Type: Quantity Discrepancy  
Discrepancy ID: QT-002  
Discrepancy Title: Net Weight Mismatch Between LC and Invoice  
Discrepancy Short Detail: Net weight discrepancy; LC specifies 4,000.00 kg, invoice shows 3,998.00 kg.  
Discrepancy Long Detail: The Letter of Credit stipulates a net weight of 4,000.00 kg, while the Commercial Invoice indicates 3,998.00 kg. This mismatch may lead to non-compliance with LC terms and potential rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Net Weight: 4,000.00 kg  
  - Target (Commercial Invoice): Net Weight: 3,998.00 kg  
  - Difference: Net weight is short by 2.00 kg in the invoice compared to the LC.  
Severity Level: Medium  
Golden Truth Value: 4,000.00 kg  
Secondary Document Value: 3,998.00 kg  
Impact: The discrepancy could result in payment delays or rejection of the documents, requiring clarification or amendment to resolve.
---
#### Serial ID: 3  
Type: Coverage Discrepancy  
Discrepancy ID: CV-003  
Discrepancy Title: Coverage Clause Mismatch  
Discrepancy Short Detail: Insurance coverage does not comply with LC requirements.  
Discrepancy Long Detail: The Letter of Credit specifies Institute Cargo Clauses (C) for coverage, but the Insurance Certificate lists Institute Cargo Clauses (A). This mismatch may lead to non-compliance with LC terms and potential rejection of documents.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Coverage: Institute Cargo Clauses (C)  
  - Target (Insurance Certificate): Coverage: Institute Cargo Clauses (A)  
  - Difference: The LC requires Institute Cargo Clauses (C), but the Insurance Certificate provides broader coverage under Institute Cargo Clauses (A), which does not align with LC stipulations.  
Severity Level: Medium  
Golden Truth Value: Institute Cargo Clauses (C)  
Secondary Document Value: Institute Cargo Clauses (A)  
Impact: The discrepancy may result in refusal of the insurance document by the issuing bank, potentially delaying payment or shipment processing.
---
#### Serial ID: 4  
Type: Claims Payable Location Discrepancy  
Discrepancy ID: CP-004  
Discrepancy Title: Claims Payable Location Mismatch  
Discrepancy Short Detail: Insurance certificate lists claims payable in Dubai instead of Vietnam as required by LC.  
Discrepancy Long Detail: The Letter of Credit specifies that claims must be payable in Vietnam, but the insurance certificate indicates Dubai, United Arab Emirates. This discrepancy violates the LC terms and may lead to non-compliance, risking rejection of the documents.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Claims Payable: Vietnam  
  - Target (Insurance Certificate): Claims Payable: Dubai, United Arab Emirates  
  - Difference: Location mismatch; LC mandates Vietnam, but insurance certificate states Dubai.  
Severity Level: High  
Golden Truth Value: Vietnam  
Secondary Document Value: Dubai, United Arab Emirates  
Impact: The discrepancy may result in refusal of payment under the LC, as the claims payable location does not align with the LC requirements.
---
#### Serial ID: 5  
Type: Shipment Date Discrepancy  
Discrepancy ID: SD-005  
Discrepancy Title: Shipped on Board Date Exceeds Latest Shipment Date  
Discrepancy Short Detail: Shipped on board date is later than the LC's specified latest shipment date.  
Discrepancy Long Detail: The Letter of Credit specifies that the shipment must occur not later than 25-Sep-2025, but the Bill of Lading indicates a shipped on board date of 26-Sep-2025. This discrepancy violates the LC terms and may lead to non-compliance, risking rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Shipped on Board Date: Not later than 25-Sep-2025  
  - Target (Bill of Lading): Shipped on Board Date: 26-Sep-2025  
  - Difference: The shipped on board date in the Bill of Lading exceeds the LC's latest shipment date by one day.  
Severity Level: High  
Golden Truth Value: Not later than 25-Sep-2025  
Secondary Document Value: 26-Sep-2025  
Impact: This discrepancy may result in the issuing bank rejecting the documents, causing delays or financial loss for the beneficiary.
---
#### Serial ID: 6  
Type: Quantity Discrepancy  
Discrepancy ID: QT-006  
Discrepancy Title: Gross Weight Mismatch Between LC and Packing List  
Discrepancy Short Detail: Gross weight in LC differs from packing list by 2.00 kg.  
Discrepancy Long Detail: The Letter of Credit specifies a gross weight of 4,200.00 kg, while the packing list indicates 4,198.00 kg. This discrepancy may lead to compliance issues or rejection by the issuing bank.  
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
Discrepancy Title: Carton Quantity Mismatch for Pallet 7  
Discrepancy Short Detail: Pallet 7 contains 49 cartons instead of the required 50.  
Discrepancy Long Detail: The Letter of Credit specifies that each pallet must contain 50 cartons, but the Packing List indicates Pallet 7 contains only 49 cartons. This deviation may lead to non-compliance with LC terms and potential rejection of the shipment.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Cartons per Pallet: 50 pieces per carton  
  - Target (Packing List): Cartons per Pallet: Pallet 7 contains 49 cartons  
  - Difference: Pallet 7 is short by 1 carton compared to the LC requirement.  
Severity Level: Medium  
Golden Truth Value: 50 pieces per carton  
Secondary Document Value: Pallet 7 contains 49 cartons  
Impact: The discrepancy risks shipment rejection or payment delays due to non-compliance with LC terms.
---
#### Serial ID: 8  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-008  
Discrepancy Title: Buyer Specification Mismatch in Certificate of Origin  
Discrepancy Short Detail: LC specifies VGE/KT-2025-09, but Certificate of Origin includes "Rev A".  
Discrepancy Long Detail: The Letter of Credit (LC) lists the buyer specification as VGE/KT-2025-09, while the Certificate of Origin adds "Rev A" to the specification. This discrepancy may lead to non-compliance with LC terms, potentially causing delays or rejection of the document.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Buyer Specification: VGE/KT-2025-09  
  - Target (Certificate of Origin): Buyer Specification: VGE/KT-2025-09 (Rev A)  
  - Difference: The Certificate of Origin includes an additional revision identifier "Rev A" not mentioned in the LC.  
Severity Level: Medium  
Golden Truth Value: VGE/KT-2025-09  
Secondary Document Value: VGE/KT-2025-09 (Rev A)  
Impact: This discrepancy may result in the issuing bank rejecting the Certificate of Origin, causing delays in payment or shipment processing.
