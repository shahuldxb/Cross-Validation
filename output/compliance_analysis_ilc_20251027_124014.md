# Trade Finance Compliance Analysis Report
**Generated:** 2025-10-27 12:40:14
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
| Letter of Credit (LC) | Commercial Invoice (INV) | Goods Description | Knitted cotton T‑shirts, 100% cotton | Knitted T‑shirts, 97% cotton / 3% elastane | Fiber content discrepancy |
| Letter of Credit (LC) | Commercial Invoice (INV) | Net Weight | 4,000.00 kg | 3,998.00 kg | Net weight discrepancy |
| Letter of Credit (LC) | Insurance Certificate (INS) | Coverage | Institute Cargo Clauses (C), Institute War Clauses (Cargo), Institute Strikes, Riots and Civil Commotions (Cargo) | Institute Cargo Clauses (A), Institute War Clauses (Cargo), Institute Strikes, Riots & Civil Commotions (Cargo) | Coverage clause discrepancy |
| Letter of Credit (LC) | Insurance Certificate (INS) | Claims Payable | Vietnam | Dubai, United Arab Emirates | Claims payable location discrepancy |
| Letter of Credit (LC) | Insurance Certificate (INS) | Sum Insured | USD 141,295.00 (110% of USD 128,450.00) | AED 471,000.00 | Currency mismatch and incorrect sum insured |
| Letter of Credit (LC) | Bill of Lading (BOL) | Port of Discharge | Cat Lai Terminal, Ho Chi Minh City, Vietnam | Ho Chi Minh City, Vietnam | Port of discharge mismatch |
| Letter of Credit (LC) | Bill of Lading (BOL) | Place of Delivery | Not specified | Cat Lai CY, Ho Chi Minh City, Vietnam | Extra information provided |
| Letter of Credit (LC) | Bill of Lading (BOL) | On Board Notation Date | Not later than 25-Sep-2025 | 26-Sep-2025 | Late shipment date |
| Letter of Credit (LC) | Packing List (PL) | Gross Weight | 4,200.00 kg | 4,198.00 kg | Gross weight discrepancy |
| Letter of Credit (LC) | Packing List (PL) | Net Weight | 4,000.00 kg | 3,998.00 kg | Net weight discrepancy |
| Letter of Credit (LC) | Packing List (PL) | Cartons per Pallet | 50 pieces per carton | Pallet 7 has 49 cartons | Quantity discrepancy |
| Letter of Credit (LC) | Quality Certificate (QC) | Buyer Specification | VGE/KT-2025-09 | VGE/KT-2025-09 (Rev A) | Specification revision mismatch |
---

### Detailed Analysis

**GOLDEN TRUTH DOCUMENT:** Irrevocable Letter of Credit (LC) - ilc.txt  
**SECONDARY DOCUMENTS FOUND:**  
1. Commercial Invoice (INV) - COMMERCIAL INVOICE.txt
2. Insurance Certificate (INS) - INSURANCE CERTIFICATE POLICY.txt
3. Bill of Lading (BOL) - OCEAN BILL OF.txt
4. Packing List (PL) - PACKING LIST.txt
5. Quality Certificate (QC) - QUALITY CERTIFICATE.txt  

**TOTAL DISCREPANCIES FOUND:** 12  

---

#### Serial ID: 1  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-001  
Discrepancy Title: Fiber Content Mismatch in Goods Description  
Discrepancy Short Detail: Fiber content differs between LC and Commercial Invoice.  
Discrepancy Long Detail: The Letter of Credit specifies the goods as "Knitted cotton T‑shirts, 100% cotton," while the Commercial Invoice describes them as "Knitted T‑shirts, 97% cotton / 3% elastane." This discrepancy in fiber content may lead to non-compliance with the LC terms and potential rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Goods Description: Knitted cotton T‑shirts, 100% cotton  
  - Target (Commercial Invoice (INV)): Goods Description: Knitted T‑shirts, 97% cotton / 3% elastane  
  - Difference: Fiber content is mismatched; LC specifies 100% cotton, while the invoice includes 3% elastane.  
Severity Level: Medium  
Golden Truth Value: Knitted cotton T‑shirts, 100% cotton  
Secondary Document Value: Knitted T‑shirts, 97% cotton / 3% elastane  
Impact: This discrepancy may result in rejection of the documents by the issuing bank, causing delays or financial loss.
---
#### Serial ID: 2  
Type: Quantity Discrepancy  
Discrepancy ID: QT-002  
Discrepancy Title: Net Weight Mismatch Between LC and Invoice  
Discrepancy Short Detail: Net weight in LC and invoice differs by 2.00 kg.  
Discrepancy Long Detail: The net weight specified in the Letter of Credit (4,000.00 kg) does not match the net weight stated in the Commercial Invoice (3,998.00 kg). This discrepancy may lead to compliance issues or rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Net Weight: 4,000.00 kg  
  - Target (Commercial Invoice (INV)): Net Weight: 3,998.00 kg  
  - Difference: Net weight is short by 2.00 kg in the Commercial Invoice compared to the Letter of Credit.  
Severity Level: Medium  
Golden Truth Value: 4,000.00 kg  
Secondary Document Value: 3,998.00 kg  
Impact: The discrepancy could result in payment delays or rejection of documents by the issuing bank, potentially affecting the transaction's completion.
---
#### Serial ID: 3  
Type: Coverage Discrepancy  
Discrepancy ID: CV-003  
Discrepancy Title: Coverage Clause Mismatch Between LC and Insurance Certificate  
Discrepancy Short Detail: Coverage clauses differ between LC and Insurance Certificate.  
Discrepancy Long Detail: The Letter of Credit specifies coverage under Institute Cargo Clauses (C), while the Insurance Certificate provides coverage under Institute Cargo Clauses (A). This mismatch may lead to non-compliance with LC terms, potentially causing rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Coverage: Institute Cargo Clauses (C), Institute War Clauses (Cargo), Institute Strikes, Riots and Civil Commotions (Cargo)  
  - Target (Insurance Certificate (INS)): Coverage: Institute Cargo Clauses (A), Institute War Clauses (Cargo), Institute Strikes, Riots & Civil Commotions (Cargo)  
  - Difference: Institute Cargo Clauses (C) in LC vs Institute Cargo Clauses (A) in Insurance Certificate.  
Severity Level: Medium  
Golden Truth Value: Institute Cargo Clauses (C), Institute War Clauses (Cargo), Institute Strikes, Riots and Civil Commotions (Cargo)  
Secondary Document Value: Institute Cargo Clauses (A), Institute War Clauses (Cargo), Institute Strikes, Riots & Civil Commotions (Cargo)  
Impact: The discrepancy may result in the issuing bank rejecting the insurance certificate, delaying payment and shipment processing.
---
#### Serial ID: 4  
Type: Claims Payable Location Discrepancy  
Discrepancy ID: CP-004  
Discrepancy Title: Mismatch in Claims Payable Location  
Discrepancy Short Detail: Claims payable location differs between LC and Insurance Certificate.  
Discrepancy Long Detail: The Letter of Credit specifies Vietnam as the claims payable location, while the Insurance Certificate lists Dubai, United Arab Emirates. This discrepancy may lead to compliance issues and potential rejection of documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Claims Payable: Vietnam  
  - Target (Insurance Certificate (INS)): Claims Payable: Dubai, United Arab Emirates  
  - Difference: The claims payable location in the LC does not match the location stated in the Insurance Certificate.  
Severity Level: Medium  
Golden Truth Value: Vietnam  
Secondary Document Value: Dubai, United Arab Emirates  
Impact: This discrepancy could result in delays or rejection of the transaction due to non-compliance with the LC terms.
---
#### Serial ID: 5  
Type: Sum Insured Discrepancy  
Discrepancy ID: SI-005  
Discrepancy Title: Currency Mismatch and Incorrect Sum Insured  
Discrepancy Short Detail: Sum insured differs in currency and amount between LC and Insurance Certificate.  
Discrepancy Long Detail: The sum insured in the Letter of Credit (USD 141,295.00) does not match the Insurance Certificate (AED 471,000.00). This discrepancy involves both a currency mismatch and an incorrect insured amount, which may lead to non-compliance with LC terms and potential rejection of documents.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Sum Insured: USD 141,295.00 (110% of USD 128,450.00)  
  - Target (Insurance Certificate (INS)): Sum Insured: AED 471,000.00  
  - Difference: Currency mismatch (USD vs AED) and incorrect sum insured amount.  
Severity Level: High  
Golden Truth Value: USD 141,295.00 (110% of USD 128,450.00)  
Secondary Document Value: AED 471,000.00  
Impact: This discrepancy risks rejection of the Insurance Certificate by the issuing bank, potentially delaying payment and shipment processing.
---
#### Serial ID: 6  
Type: Port of Discharge Discrepancy  
Discrepancy ID: PD-006  
Discrepancy Title: Port of Discharge Mismatch  
Discrepancy Short Detail: Port of discharge differs between LC and BOL.  
Discrepancy Long Detail: The Letter of Credit specifies "Cat Lai Terminal, Ho Chi Minh City, Vietnam" as the port of discharge, while the Bill of Lading mentions only "Ho Chi Minh City, Vietnam." This discrepancy may lead to confusion or rejection due to non-compliance with the LC terms.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Port of Discharge: Cat Lai Terminal, Ho Chi Minh City, Vietnam  
  - Target (Bill of Lading (BOL)): Port of Discharge: Ho Chi Minh City, Vietnam  
  - Difference: The LC specifies a terminal within the city, while the BOL provides only the city name, omitting the terminal detail.  
Severity Level: Medium  
Golden Truth Value: Cat Lai Terminal, Ho Chi Minh City, Vietnam  
Secondary Document Value: Ho Chi Minh City, Vietnam  
Impact: This mismatch may result in delays or rejection of the documents by the issuing bank, as the LC terms are not fully met.
---
#### Serial ID: 7  
Type: Place of Delivery Discrepancy  
Discrepancy ID: PD-007  
Discrepancy Title: Extra Information in Place of Delivery Field  
Discrepancy Short Detail: Target document specifies delivery location not mentioned in base document.  
Discrepancy Long Detail: The Bill of Lading provides additional details for the place of delivery, "Cat Lai CY, Ho Chi Minh City, Vietnam," which is absent in the Letter of Credit. This discrepancy may lead to compliance issues as the LC does not authorize or specify this delivery location.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Place of Delivery: Not specified  
  - Target (Bill of Lading (BOL)): Place of Delivery: Cat Lai CY, Ho Chi Minh City, Vietnam  
  - Difference: Extra information provided in the target document that is not referenced in the base document.  
Severity Level: Medium  
Golden Truth Value: Not specified  
Secondary Document Value: Cat Lai CY, Ho Chi Minh City, Vietnam  
Impact: The discrepancy may result in rejection of the documents by the issuing bank due to non-compliance with LC terms.
---
#### Serial ID: 8  
Type: Shipment Date Discrepancy  
Discrepancy ID: SD-008  
Discrepancy Title: Late Shipment Date on Bill of Lading  
Discrepancy Short Detail: Shipment date exceeds the LC requirement by one day.  
Discrepancy Long Detail: The Letter of Credit specifies that the shipment must be on board not later than 25-Sep-2025. However, the Bill of Lading indicates an on-board notation date of 26-Sep-2025, which is non-compliant with the LC terms. This discrepancy may lead to rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): On Board Notation Date: Not later than 25-Sep-2025  
  - Target (Bill of Lading (BOL)): On Board Notation Date: 26-Sep-2025  
  - Difference: Shipment date is one day later than the LC requirement.  
Severity Level: High  
Golden Truth Value: Not later than 25-Sep-2025  
Secondary Document Value: 26-Sep-2025  
Impact: The discrepancy risks refusal of payment by the issuing bank, potentially causing financial loss and delays in the transaction.
---
#### Serial ID: 9  
Type: Quantity Discrepancy  
Discrepancy ID: QT-009  
Discrepancy Title: Gross Weight Mismatch Between LC and Packing List  
Discrepancy Short Detail: Gross weight in LC and Packing List differs by 2.00 kg.  
Discrepancy Long Detail: The gross weight specified in the Letter of Credit (4,200.00 kg) does not match the Packing List (4,198.00 kg). This discrepancy may lead to compliance issues and potential rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Gross Weight: 4,200.00 kg  
  - Target (Packing List (PL)): Gross Weight: 4,198.00 kg  
  - Difference: 2.00 kg discrepancy in gross weight.  
Severity Level: Medium  
Golden Truth Value: 4,200.00 kg  
Secondary Document Value: 4,198.00 kg  
Impact: The mismatch could result in delays or refusal of payment under the Letter of Credit terms, requiring clarification or amendment.
---
#### Serial ID: 10  
Type: Quantity Discrepancy  
Discrepancy ID: QT-010  
Discrepancy Title: Net Weight Mismatch Between LC and Packing List  
Discrepancy Short Detail: Net weight in LC differs from Packing List by 2.00 kg.  
Discrepancy Long Detail: The Letter of Credit specifies a net weight of 4,000.00 kg, while the Packing List indicates 3,998.00 kg. This discrepancy may lead to compliance issues or rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Net Weight: 4,000.00 kg  
  - Target (Packing List (PL)): Net Weight: 3,998.00 kg  
  - Difference: Net weight is short by 2.00 kg in the Packing List compared to the LC.  
Severity Level: Medium  
Golden Truth Value: 4,000.00 kg  
Secondary Document Value: 3,998.00 kg  
Impact: The discrepancy could result in shipment rejection or payment delays due to non-compliance with LC terms.
---
#### Serial ID: 11  
Type: Quantity Discrepancy  
Discrepancy ID: QT-011  
Discrepancy Title: Mismatch in Cartons per Pallet Quantity  
Discrepancy Short Detail: Pallet 7 contains 49 cartons instead of 50 as per LC.  
Discrepancy Long Detail: The Letter of Credit specifies 50 cartons per pallet, but the Packing List indicates that Pallet 7 contains only 49 cartons. This discrepancy may lead to compliance issues and potential rejection by the buyer or bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Cartons per Pallet: 50 pieces per carton  
  - Target (Packing List (PL)): Cartons per Pallet: Pallet 7 has 49 cartons  
  - Difference: Pallet 7 is short by 1 carton compared to the LC requirement.  
Severity Level: Medium  
Golden Truth Value: 50 pieces per carton  
Secondary Document Value: Pallet 7 has 49 cartons  
Impact: This discrepancy could result in delays or rejection of the shipment, affecting payment under the LC terms.
---
#### Serial ID: 12  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-012  
Discrepancy Title: Buyer Specification Revision Mismatch  
Discrepancy Short Detail: Buyer specification in QC includes an unapproved revision.  
Discrepancy Long Detail: The Quality Certificate lists the buyer specification as "VGE/KT-2025-09 (Rev A)," which differs from the Letter of Credit's "VGE/KT-2025-09." This revision is not authorized under the LC terms, potentially leading to non-compliance and rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Buyer Specification: VGE/KT-2025-09  
  - Target (Quality Certificate (QC)): Buyer Specification: VGE/KT-2025-09 (Rev A)  
  - Difference: The target document includes an additional revision ("Rev A") not present in the base document.  
Severity Level: Medium  
Golden Truth Value: VGE/KT-2025-09  
Secondary Document Value: VGE/KT-2025-09 (Rev A)  
Impact: The mismatch may result in rejection of the Quality Certificate by the issuing bank, delaying payment and shipment processing.
