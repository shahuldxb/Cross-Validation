# Trade Finance Compliance Analysis Report
**Generated:** 2025-11-04 14:59:05
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
| Letter of Credit | Bill of Lading | Net Weight | 4,000.00 kg | 3,998.00 kg | Net weight discrepancy between LC and BOL. |
| Letter of Credit | Bill of Lading | On Board Notation Date | Not later than 25-Sep-2025 | 26-Sep-2025 | Shipment date exceeds the latest shipment date specified in LC. |
| Letter of Credit | Commercial Invoice | Goods Description | 100% cotton | 97% cotton / 3% elastane | Goods description does not match LC requirements. |
| Letter of Credit | Commercial Invoice | Net Weight | 4,000.00 kg | 3,998.00 kg | Net weight discrepancy between LC and Invoice. |
| Letter of Credit | Insurance Certificate | Coverage Clauses | Institute Cargo Clauses (C), Institute War Clauses (Cargo), Institute Strikes, Riots and Civil Commotions (Cargo) | Institute Cargo Clauses (A), Institute War Clauses (Cargo), Institute Strikes, Riots & Civil Commotions (Cargo) | Coverage clause mismatch between LC and Insurance Certificate. |
| Letter of Credit | Insurance Certificate | Claims Payable | Vietnam | Dubai, United Arab Emirates | Claims payable location does not match LC requirements. |
| Letter of Credit | Insurance Certificate | Sum Insured | 110% of invoice value in USD | AED 471,000.00 | Currency mismatch for sum insured. |
| Letter of Credit | Packing List | Gross Weight | 4,200.00 kg | 4,198.00 kg | Gross weight discrepancy between LC and Packing List. |
| Letter of Credit | Packing List | Net Weight | 4,000.00 kg | 3,998.00 kg | Net weight discrepancy between LC and Packing List. |
| Letter of Credit | Packing List | Total Cartons | 350 cartons | 349 cartons | Total cartons discrepancy between LC and Packing List. |
| Letter of Credit | Quality Certificate | Buyer Specification | VGE/KT-2025-09 | VGE/KT-2025-09 (Rev A) | Buyer specification revision mismatch between LC and Quality Certificate. |
---

### Detailed Analysis

**GOLDEN TRUTH DOCUMENT:** Irrevocable Letter of Credit (LC) - ilc.txt  
**SECONDARY DOCUMENTS FOUND:**  
1. Bill of Lading (BOL) - BILL OF LADING.txt
2. Commercial Invoice (INV) - COMMERCIAL INVOICE.txt
3. Insurance Certificate (INS) - INSURANCE CERTIFICATE.txt
4. Packing List (PL) - PACKING LIST.txt
5. Quality Certificate (QC) - QUALITY CERTIFICATE.txt  

**TOTAL DISCREPANCIES FOUND:** 11  

---

#### Serial ID: 1  
Type: Quantity Discrepancy  
Discrepancy ID: QT-001  
Discrepancy Title: Net Weight Mismatch Between LC and BOL  
Discrepancy Short Detail: Net weight in LC and BOL differs by 2.00 kg.  
Discrepancy Long Detail: The Letter of Credit specifies a net weight of 4,000.00 kg, while the Bill of Lading indicates 3,998.00 kg. This discrepancy may lead to compliance issues or rejection by the issuing bank due to non-conformance with the LC terms.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Net Weight: 4,000.00 kg  
  - Target (Bill of Lading): Net Weight: 3,998.00 kg  
  - Difference: A shortfall of 2.00 kg in the net weight stated in the Bill of Lading compared to the Letter of Credit.  
Severity Level: Medium  
Golden Truth Value: 4,000.00 kg  
Secondary Document Value: 3,998.00 kg  
Impact: This discrepancy could result in the issuing bank rejecting the documents, causing delays in payment or shipment clearance.
---
#### Serial ID: 2  
Type: Shipment Date Discrepancy  
Discrepancy ID: SD-002  
Discrepancy Title: Shipment Date Exceeds Latest Allowed Date  
Discrepancy Short Detail: Shipment date on Bill of Lading is later than the LC-specified latest shipment date.  
Discrepancy Long Detail: The Letter of Credit specifies that the shipment must occur not later than 25-Sep-2025, but the Bill of Lading indicates an on-board notation date of 26-Sep-2025. This discrepancy violates the LC terms and may lead to non-compliance, risking rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): On Board Notation Date: Not later than 25-Sep-2025  
  - Target (Bill of Lading): On Board Notation Date: 26-Sep-2025  
  - Difference: The shipment date exceeds the LC-specified latest shipment date by one day.  
Severity Level: High  
Golden Truth Value: Not later than 25-Sep-2025  
Secondary Document Value: 26-Sep-2025  
Impact: The discrepancy may result in the issuing bank rejecting the documents, causing delays in payment and potential financial loss for the beneficiary.
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
  - Difference: The goods description in the invoice includes an additional material (3% elastane) not permitted by the LC.  
Severity Level: High  
Golden Truth Value: 100% cotton  
Secondary Document Value: 97% cotton / 3% elastane  
Impact: The discrepancy may result in the issuing bank refusing to honor the payment under the LC, causing delays or financial loss.  
---
#### Serial ID: 4  
Type: Quantity Discrepancy  
Discrepancy ID: QT-004  
Discrepancy Title: Net Weight Mismatch Between LC and Invoice  
Discrepancy Short Detail: Net weight in LC differs from invoice by 2.00 kg.  
Discrepancy Long Detail: The Letter of Credit specifies a net weight of 4,000.00 kg, while the Commercial Invoice states 3,998.00 kg. This discrepancy may lead to compliance issues or rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Net Weight: 4,000.00 kg  
  - Target (Commercial Invoice): Net Weight: 3,998.00 kg  
  - Difference: Net weight is short by 2.00 kg in the invoice compared to the LC.  
Severity Level: Medium  
Golden Truth Value: 4,000.00 kg  
Secondary Document Value: 3,998.00 kg  
Impact: The mismatch could result in payment delays or refusal by the issuing bank, requiring clarification or amendment to resolve.
---
#### Serial ID: 5  
Type: Coverage Clause Discrepancy  
Discrepancy ID: CC-005  
Discrepancy Title: Coverage Clause Mismatch Between LC and Insurance Certificate  
Discrepancy Short Detail: Coverage clauses differ between LC and Insurance Certificate.  
Discrepancy Long Detail: The Letter of Credit specifies Institute Cargo Clauses (C), while the Insurance Certificate lists Institute Cargo Clauses (A). This mismatch may lead to non-compliance with LC terms, potentially causing rejection of documents.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Coverage Clauses: Institute Cargo Clauses (C), Institute War Clauses (Cargo), Institute Strikes, Riots and Civil Commotions (Cargo)  
  - Target (Insurance Certificate): Coverage Clauses: Institute Cargo Clauses (A), Institute War Clauses (Cargo), Institute Strikes, Riots & Civil Commotions (Cargo)  
  - Difference: Institute Cargo Clauses (C) in LC vs Institute Cargo Clauses (A) in Insurance Certificate.  
Severity Level: Medium  
Golden Truth Value: Institute Cargo Clauses (C), Institute War Clauses (Cargo), Institute Strikes, Riots and Civil Commotions (Cargo)  
Secondary Document Value: Institute Cargo Clauses (A), Institute War Clauses (Cargo), Institute Strikes, Riots & Civil Commotions (Cargo)  
Impact: The discrepancy may result in the issuing bank rejecting the documents due to non-compliance with LC terms, delaying payment or shipment processing.
---
#### Serial ID: 6  
Type: Claims Payable Location Discrepancy  
Discrepancy ID: CP-006  
Discrepancy Title: Mismatch in Claims Payable Location  
Discrepancy Short Detail: Claims payable location differs between LC and insurance certificate.  
Discrepancy Long Detail: The Letter of Credit specifies Vietnam as the claims payable location, while the insurance certificate lists Dubai, United Arab Emirates. This mismatch violates LC requirements and may lead to non-compliance with trade terms.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Claims Payable: Vietnam  
  - Target (Insurance Certificate): Claims Payable: Dubai, United Arab Emirates  
  - Difference: The claims payable location in the insurance certificate does not align with the LC's stipulated location.  
Severity Level: Medium  
Golden Truth Value: Vietnam  
Secondary Document Value: Dubai, United Arab Emirates  
Impact: This discrepancy may result in rejection of the documents by the issuing bank, delaying payment and shipment processing.
---
#### Serial ID: 7  
Type: Currency Discrepancy  
Discrepancy ID: CD-007  
Discrepancy Title: Currency Mismatch in Sum Insured  
Discrepancy Short Detail: Sum insured currency differs between LC and Insurance Certificate.  
Discrepancy Long Detail: The Letter of Credit specifies the sum insured as 110% of the invoice value in USD, while the Insurance Certificate lists it as AED 471,000.00. This discrepancy in currency creates a compliance issue and may lead to rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Sum Insured: 110% of invoice value in USD  
  - Target (Insurance Certificate): Sum Insured: AED 471,000.00  
  - Difference: Currency mismatch between USD and AED for the sum insured.  
Severity Level: High  
Golden Truth Value: 110% of invoice value in USD  
Secondary Document Value: AED 471,000.00  
Impact: The discrepancy may result in non-compliance with LC terms, leading to potential rejection of the documents and delayed payment.
---
#### Serial ID: 8  
Type: Quantity Discrepancy  
Discrepancy ID: QT-008  
Discrepancy Title: Gross Weight Mismatch Between LC and Packing List  
Discrepancy Short Detail: Gross weight differs by 2.00 kg between LC and Packing List.  
Discrepancy Long Detail: The Letter of Credit specifies a gross weight of 4,200.00 kg, while the Packing List indicates 4,198.00 kg. This discrepancy may lead to compliance issues or rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Gross Weight: 4,200.00 kg  
  - Target (Packing List): Gross Weight: 4,198.00 kg  
  - Difference: Gross weight mismatch of 2.00 kg.  
Severity Level: Medium  
Golden Truth Value: 4,200.00 kg  
Secondary Document Value: 4,198.00 kg  
Impact: The discrepancy could result in payment delays or refusal by the issuing bank due to non-conformance with LC terms.
---
#### Serial ID: 9  
Type: Quantity Discrepancy  
Discrepancy ID: QT-009  
Discrepancy Title: Net Weight Mismatch Between LC and Packing List  
Discrepancy Short Detail: Net weight in LC and Packing List differs by 2.00 kg.  
Discrepancy Long Detail: The Letter of Credit specifies a net weight of 4,000.00 kg, while the Packing List indicates 3,998.00 kg. This discrepancy may lead to compliance issues or rejection by the issuing bank due to non-conformance with LC terms.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Net Weight: 4,000.00 kg  
  - Target (Packing List): Net Weight: 3,998.00 kg  
  - Difference: A mismatch of 2.00 kg in net weight.  
Severity Level: Medium  
Golden Truth Value: 4,000.00 kg  
Secondary Document Value: 3,998.00 kg  
Impact: The discrepancy could result in delays or rejection of the documents, potentially affecting payment under the LC terms.
---
#### Serial ID: 10  
Type: Quantity Discrepancy  
Discrepancy ID: QT-010  
Discrepancy Title: Total Cartons Mismatch Between LC and Packing List  
Discrepancy Short Detail: Total cartons in LC and Packing List differ by 1 carton.  
Discrepancy Long Detail: The Letter of Credit specifies a total of 350 cartons, while the Packing List indicates 349 cartons. This discrepancy may lead to non-compliance with LC terms, risking rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Total Cartons: 350 cartons  
  - Target (Packing List): Total Cartons: 349 cartons  
  - Difference: 1 carton less in the Packing List compared to the LC  
Severity Level: Medium  
Golden Truth Value: 350 cartons  
Secondary Document Value: 349 cartons  
Impact: This discrepancy could result in payment delays or rejection of documents by the issuing bank, potentially affecting shipment acceptance.  
---
#### Serial ID: 11  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-011  
Discrepancy Title: Buyer Specification Revision Mismatch  
Discrepancy Short Detail: Buyer specification in LC differs from Quality Certificate revision.  
Discrepancy Long Detail: The Letter of Credit specifies "VGE/KT-2025-09," while the Quality Certificate lists "VGE/KT-2025-09 (Rev A)." This revision mismatch may lead to compliance issues and potential rejection by the buyer.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Buyer Specification: VGE/KT-2025-09  
  - Target (Quality Certificate): Buyer Specification: VGE/KT-2025-09 (Rev A)  
  - Difference: The Quality Certificate includes a revision identifier "(Rev A)" not present in the LC.  
Severity Level: Medium  
Golden Truth Value: VGE/KT-2025-09  
Secondary Document Value: VGE/KT-2025-09 (Rev A)  
Impact: The mismatch may result in shipment delays or rejection due to non-compliance with the buyer's specified terms in the LC.
