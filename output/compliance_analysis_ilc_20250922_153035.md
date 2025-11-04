# Trade Finance Compliance Analysis Report
**Generated:** 2025-09-22 15:30:35
**Base Document (Golden Truth):** ilc.txt
**Secondary Documents Analyzed:** 5 files

## Documents Processed:
- **Golden Truth:** ilc.txt
- **Secondary 1:** CERTIFICATE OF ORIGIN.txt
- **Secondary 2:** COMMERCIAL INVOICE.txt
- **Secondary 3:** DANGEROUS GOODS DECLARATION.txt
- **Secondary 4:** PACKING LIST.txt
- **Secondary 5:** QUALITY CERTIFICATE.txt

---

## Compliance Analysis Results:

### Markdown Table of Discrepancies

| Base Document | Target Document | Field(s) | Base Value | Target Value | Issue |
|---------------|-----------------|----------|------------|--------------|-------|
| Letter of Credit (LC) | Certificate of Origin | Goods Description | Lithium-Ion Batteries, UN 3480, Class 9 | Rechargeable Batteries for Consumer Devices (Nickel-Metal Hydride) | Goods description mismatch |
| Letter of Credit (LC) | Certificate of Origin | Quantity | 500 units | 480 units | Quantity mismatch |
| Letter of Credit (LC) | Certificate of Origin | Date of Export | Latest Shipment Date: 15 October 2025 | 20 October 2025 | Shipment date exceeds LC's latest shipment date |
| Letter of Credit (LC) | Commercial Invoice | Goods Description | Lithium-Ion Batteries, UN 3480, Class 9 | Rechargeable Lithium-Ion Batteries (Model LP-500) | Goods description mismatch |
| Letter of Credit (LC) | Commercial Invoice | Quantity | 500 units | 520 units | Quantity mismatch |
| Letter of Credit (LC) | Commercial Invoice | Total Amount | USD 75,000.00 | USD 76,440.00 | Amount mismatch |
| Letter of Credit (LC) | Commercial Invoice | Incoterms | CIF Jebel Ali Port, Dubai, UAE | FOB Yantian Port, China | Incoterms mismatch |
| Letter of Credit (LC) | Commercial Invoice | Port of Discharge | Jebel Ali Port, Dubai, UAE | Port Khalifa, Abu Dhabi, UAE | Port of discharge mismatch |
| Letter of Credit (LC) | Dangerous Goods Declaration | Goods Description | Lithium-Ion Batteries, UN 3480, Class 9 | LITHIUM METAL BATTERIES | Goods description mismatch |
| Letter of Credit (LC) | Dangerous Goods Declaration | UN Number | UN 3480 | UN 3090 | UN number mismatch |
| Letter of Credit (LC) | Dangerous Goods Declaration | Number of Packages | Not specified | 50 cartons | Missing information in LC |
| Letter of Credit (LC) | Dangerous Goods Declaration | Net Quantity of Dangerous Goods | Not specified | 920 kg | Missing information in LC |
| Letter of Credit (LC) | Packing List | Goods Description | Lithium-Ion Batteries, UN 3480, Class 9 | Lithium-Ion Batteries (Model LP-500) | Goods description mismatch |
| Letter of Credit (LC) | Packing List | Quantity | 500 units | 500 units | No discrepancy |
| Letter of Credit (LC) | Packing List | Partial Shipment | Not Allowed | Allowed | Partial shipment allowance mismatch |
| Letter of Credit (LC) | Packing List | Port of Discharge | Jebel Ali Port, Dubai, UAE | Port Khalifa, Abu Dhabi, UAE | Port of discharge mismatch |
| Letter of Credit (LC) | Packing List | Date of Shipment | Latest Shipment Date: 15 October 2025 | 18 October 2025 | Shipment date exceeds LC's latest shipment date |
| Letter of Credit (LC) | Quality Certificate | Goods Description | Lithium-Ion Batteries, UN 3480, Class 9 | Rechargeable Lithium-Ion Batteries (Model LP-500) | Goods description mismatch |
| Letter of Credit (LC) | Quality Certificate | Quantity | 500 units | 480 units | Quantity mismatch |
| Letter of Credit (LC) | Quality Certificate | Port of Discharge | Jebel Ali Port, Dubai, UAE | Port Khalifa, Abu Dhabi, UAE | Port of discharge mismatch |
---

### Detailed Analysis

**GOLDEN TRUTH DOCUMENT:** Irrevocable Letter of Credit (LC) - ilc.txt  
**SECONDARY DOCUMENTS FOUND:**  
1. Insurance Certificate (INS) - CERTIFICATE OF ORIGIN.txt
2. Commercial Invoice (INV) - COMMERCIAL INVOICE.txt
3. Trade Document (DANGEROUS GOODS DECLARATION.txt) - DANGEROUS GOODS DECLARATION.txt
4. Packing List (PL) - PACKING LIST.txt
5. Insurance Certificate (INS) - QUALITY CERTIFICATE.txt  

**TOTAL DISCREPANCIES FOUND:** 20  

---

#### Serial ID: 1  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-001  
Discrepancy Title: Mismatch in Goods Description Between LC and Certificate of Origin  
Discrepancy Short Detail: Goods description in LC and Certificate of Origin do not match.  
Discrepancy Long Detail: The Letter of Credit specifies the goods as "Lithium-Ion Batteries, UN 3480, Class 9," while the Certificate of Origin describes them as "Rechargeable Batteries for Consumer Devices (Nickel-Metal Hydride)." This discrepancy indicates a potential misalignment in the type of goods shipped versus those stipulated in the LC, which could lead to non-compliance with LC terms and possible rejection of the documents.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Goods Description: Lithium-Ion Batteries, UN 3480, Class 9  
  - Target (Certificate of Origin): Goods Description: Rechargeable Batteries for Consumer Devices (Nickel-Metal Hydride)  
  - Difference: The goods description differs in both type (Lithium-Ion vs. Nickel-Metal Hydride) and classification details.  
Severity Level: High  
Golden Truth Value: Lithium-Ion Batteries, UN 3480, Class 9  
Secondary Document Value: Rechargeable Batteries for Consumer Devices (Nickel-Metal Hydride)  
Impact: This discrepancy may result in the issuing bank rejecting the documents, delaying payment, and potentially causing financial and reputational risks for the beneficiary.  
---
#### Serial ID: 2  
Type: Quantity Discrepancy  
Discrepancy ID: QT-002  
Discrepancy Title: Quantity Mismatch Between LC and Certificate of Origin  
Discrepancy Short Detail: Quantity in LC is 500 units, but Certificate of Origin shows 480 units.  
Discrepancy Long Detail: The Letter of Credit specifies a quantity of 500 units, while the Certificate of Origin indicates only 480 units. This mismatch may lead to non-compliance with LC terms, potentially causing rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Quantity: 500 units  
  - Target (Certificate of Origin): Quantity: 480 units  
  - Difference: The Certificate of Origin reflects 20 fewer units than the LC.  
Severity Level: High  
Golden Truth Value: 500 units  
Secondary Document Value: 480 units  
Impact: This discrepancy could result in the issuing bank refusing to honor the LC, leading to delays or financial loss for the beneficiary.
---
#### Serial ID: 3  
Type: Shipment Date Discrepancy  
Discrepancy ID: SD-003  
Discrepancy Title: Shipment Date Exceeds LC's Latest Shipment Date  
Discrepancy Short Detail: Shipment date in Certificate of Origin exceeds LC's latest shipment date by 5 days.  
Discrepancy Long Detail: The Letter of Credit specifies the latest shipment date as 15 October 2025, while the Certificate of Origin lists the shipment date as 20 October 2025. This discrepancy violates the LC terms and may lead to non-compliance, risking rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Date of Export: Latest Shipment Date: 15 October 2025  
  - Target (Certificate of Origin): Date of Export: 20 October 2025  
  - Difference: Shipment date in the Certificate of Origin exceeds the LC's latest shipment date by 5 days.  
Severity Level: High  
Golden Truth Value: Latest Shipment Date: 15 October 2025  
Secondary Document Value: 20 October 2025  
Impact: The discrepancy may result in refusal of payment under the LC, causing financial and operational risks for the beneficiary.
---
#### Serial ID: 4  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-004  
Discrepancy Title: Goods Description Mismatch Between LC and Commercial Invoice  
Discrepancy Short Detail: Goods description in the LC and invoice do not match.  
Discrepancy Long Detail: The LC specifies "Lithium-Ion Batteries, UN 3480, Class 9," while the invoice describes "Rechargeable Lithium-Ion Batteries (Model LP-500)." This mismatch may lead to non-compliance with LC terms, potentially causing rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Goods Description: Lithium-Ion Batteries, UN 3480, Class 9  
  - Target (Commercial Invoice): Goods Description: Rechargeable Lithium-Ion Batteries (Model LP-500)  
  - Difference: The LC specifies a general description with UN classification, while the invoice provides a specific model name without UN classification.  
Severity Level: Medium  
Golden Truth Value: Lithium-Ion Batteries, UN 3480, Class 9  
Secondary Document Value: Rechargeable Lithium-Ion Batteries (Model LP-500)  
Impact: This discrepancy may result in the issuing bank rejecting the documents, delaying payment, and requiring amendments or reissuance of the invoice.
---
#### Serial ID: 5  
Type: Quantity Discrepancy  
Discrepancy ID: QT-005  
Discrepancy Title: Quantity Mismatch Between LC and Commercial Invoice  
Discrepancy Short Detail: Quantity in LC is 500 units, but Commercial Invoice shows 520 units.  
Discrepancy Long Detail: The Letter of Credit specifies a quantity of 500 units, while the Commercial Invoice indicates 520 units. This mismatch may lead to non-compliance with LC terms, risking rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Quantity: 500 units  
  - Target (Commercial Invoice): Quantity: 520 units  
  - Difference: Target document exceeds base document by 20 units.  
Severity Level: Medium  
Golden Truth Value: 500 units  
Secondary Document Value: 520 units  
Impact: The discrepancy could result in the issuing bank refusing to honor the LC, causing delays or financial loss.
---
#### Serial ID: 6  
Type: Amount Discrepancy  
Discrepancy ID: AMT-006  
Discrepancy Title: Total Amount Mismatch Between LC and Commercial Invoice  
Discrepancy Short Detail: Total amount in LC and Commercial Invoice differs by USD 1,440.00.  
Discrepancy Long Detail: The total amount stated in the Letter of Credit (USD 75,000.00) does not match the total amount in the Commercial Invoice (USD 76,440.00). This discrepancy may lead to non-compliance with the LC terms, potentially resulting in rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Total Amount: USD 75,000.00  
  - Target (Commercial Invoice): Total Amount: USD 76,440.00  
  - Difference: The Commercial Invoice exceeds the LC amount by USD 1,440.00.  
Severity Level: High  
Golden Truth Value: USD 75,000.00  
Secondary Document Value: USD 76,440.00  
Impact: This discrepancy could result in the issuing bank refusing to honor the payment under the LC, causing delays and financial risks for the beneficiary.  
---
#### Serial ID: 7  
Type: Incoterms Discrepancy  
Discrepancy ID: IT-007  
Discrepancy Title: Incoterms Mismatch Between LC and Commercial Invoice  
Discrepancy Short Detail: Incoterms differ between LC and Commercial Invoice.  
Discrepancy Long Detail: The Letter of Credit specifies Incoterms as CIF Jebel Ali Port, Dubai, UAE, while the Commercial Invoice lists FOB Yantian Port, China. This discrepancy affects the allocation of costs and risks, potentially leading to non-compliance with the LC terms.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Incoterms: CIF Jebel Ali Port, Dubai, UAE  
  - Target (Commercial Invoice): Incoterms: FOB Yantian Port, China  
  - Difference: The LC requires CIF terms to Dubai, but the invoice uses FOB terms to China, altering the delivery obligations and cost responsibilities.  
Severity Level: High  
Golden Truth Value: CIF Jebel Ali Port, Dubai, UAE  
Secondary Document Value: FOB Yantian Port, China  
Impact: This discrepancy may result in the issuing bank rejecting the documents, delaying payment, and causing potential financial and operational risks for the beneficiary.  
---
#### Serial ID: 8  
Type: Port of Discharge Discrepancy  
Discrepancy ID: PD-008  
Discrepancy Title: Port of Discharge Mismatch  
Discrepancy Short Detail: Port of discharge differs between LC and commercial invoice.  
Discrepancy Long Detail: The Letter of Credit specifies Jebel Ali Port, Dubai, UAE as the port of discharge, while the commercial invoice lists Port Khalifa, Abu Dhabi, UAE. This discrepancy may lead to non-compliance with the LC terms, potentially resulting in rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Port of Discharge: Jebel Ali Port, Dubai, UAE  
  - Target (Commercial Invoice): Port of Discharge: Port Khalifa, Abu Dhabi, UAE  
  - Difference: The port of discharge specified in the LC does not match the port listed in the commercial invoice.  
Severity Level: High  
Golden Truth Value: Jebel Ali Port, Dubai, UAE  
Secondary Document Value: Port Khalifa, Abu Dhabi, UAE  
Impact: This discrepancy could result in the issuing bank refusing to honor the LC, causing delays and financial risks for the beneficiary.
---
#### Serial ID: 9  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-009  
Discrepancy Title: Mismatch in Goods Description Between LC and Dangerous Goods Declaration  
Discrepancy Short Detail: Goods description in LC and Dangerous Goods Declaration do not match.  
Discrepancy Long Detail: The Letter of Credit specifies the goods as "Lithium-Ion Batteries, UN 3480, Class 9," while the Dangerous Goods Declaration lists them as "LITHIUM METAL BATTERIES." This discrepancy could lead to compliance issues, as the goods description is a critical element for trade and transport documentation.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Goods Description: Lithium-Ion Batteries, UN 3480, Class 9  
  - Target (Dangerous Goods Declaration): Goods Description: LITHIUM METAL BATTERIES  
  - Difference: The base document specifies Lithium-Ion Batteries, while the target document specifies Lithium Metal Batteries, which are distinct types of goods.  
Severity Level: High  
Golden Truth Value: Lithium-Ion Batteries, UN 3480, Class 9  
Secondary Document Value: LITHIUM METAL BATTERIES  
Impact: This discrepancy may result in the rejection of the shipping documents, delays in shipment, or refusal of payment under the LC due to non-compliance.
---
#### Serial ID: 10  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-010  
Discrepancy Title: UN Number Mismatch Between LC and Dangerous Goods Declaration  
Discrepancy Short Detail: UN number in LC and Dangerous Goods Declaration do not match.  
Discrepancy Long Detail: The UN number specified in the Letter of Credit (UN 3480) differs from the UN number in the Dangerous Goods Declaration (UN 3090). This discrepancy indicates a potential misclassification of the goods, which could lead to regulatory non-compliance and shipment delays.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): UN Number: UN 3480  
  - Target (Dangerous Goods Declaration): UN Number: UN 3090  
  - Difference: The UN number in the LC specifies UN 3480, while the Dangerous Goods Declaration specifies UN 3090, indicating a mismatch in the classification of the goods.  
Severity Level: High  
Golden Truth Value: UN 3480  
Secondary Document Value: UN 3090  
Impact: This discrepancy may result in the rejection of the shipping documents, regulatory penalties, or refusal of the shipment by the issuing bank or customs authorities.
---
#### Serial ID: 11  
Type: Quantity Discrepancy  
Discrepancy ID: QT-011  
Discrepancy Title: Missing Number of Packages in LC  
Discrepancy Short Detail: LC does not specify the number of packages, while the Dangerous Goods Declaration lists 50 cartons.  
Discrepancy Long Detail: The Letter of Credit fails to provide the required information regarding the number of packages, which is explicitly stated as 50 cartons in the Dangerous Goods Declaration. This omission creates a compliance gap and may lead to rejection or delays in processing the transaction.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Number of Packages: Not specified  
  - Target (Dangerous Goods Declaration): Number of Packages: 50 cartons  
  - Difference: Missing information in LC compared to specified value in Dangerous Goods Declaration.  
Severity Level: Medium  
Golden Truth Value: Not specified  
Secondary Document Value: 50 cartons  
Impact: The discrepancy may result in refusal or rejection of the documents by the issuing bank, potentially delaying the transaction and increasing operational risks.  
---
#### Serial ID: 12  
Type: Quantity Discrepancy  
Discrepancy ID: QT-012  
Discrepancy Title: Missing Net Quantity of Dangerous Goods in LC  
Discrepancy Short Detail: LC does not specify the net quantity of dangerous goods, while the declaration states 920 kg.  
Discrepancy Long Detail: The Letter of Credit (LC) lacks the specified net quantity of dangerous goods, whereas the Dangerous Goods Declaration lists it as 920 kg. This omission may lead to compliance issues, as the LC does not align with the supporting document, potentially causing delays or rejection of the transaction.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Net Quantity of Dangerous Goods: Not specified  
  - Target (Dangerous Goods Declaration): Net Quantity of Dangerous Goods: 920 kg  
  - Difference: The LC omits the net quantity, creating a mismatch with the declaration's stated 920 kg.  
Severity Level: Medium  
Golden Truth Value: Not specified  
Secondary Document Value: 920 kg  
Impact: The discrepancy may result in the issuing bank or involved parties rejecting the documents due to incomplete information, delaying the transaction or requiring amendments.  
---
#### Serial ID: 13  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-013  
Discrepancy Title: Goods Description Mismatch Between LC and Packing List  
Discrepancy Short Detail: Goods description in LC and Packing List do not match.  
Discrepancy Long Detail: The LC specifies "Lithium-Ion Batteries, UN 3480, Class 9," while the Packing List describes "Lithium-Ion Batteries (Model LP-500)." This mismatch may lead to compliance issues or rejection by the issuing bank due to non-conformance with LC terms.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Goods Description: Lithium-Ion Batteries, UN 3480, Class 9  
  - Target (Packing List): Goods Description: Lithium-Ion Batteries (Model LP-500)  
  - Difference: The LC includes regulatory classification (UN 3480, Class 9), which is absent in the Packing List, and the Packing List specifies a model number not mentioned in the LC.  
Severity Level: Medium  
Golden Truth Value: Lithium-Ion Batteries, UN 3480, Class 9  
Secondary Document Value: Lithium-Ion Batteries (Model LP-500)  
Impact: This discrepancy may result in shipment delays or rejection by the issuing bank, as the goods description does not fully align with LC requirements.
---
#### Serial ID: 14  
Type: Quantity Discrepancy  
Discrepancy ID: QT-014  
Discrepancy Title: No Discrepancy in Quantity  
Discrepancy Short Detail: The quantity matches between the LC and the Packing List.  
Discrepancy Long Detail: Upon review, the quantity specified in the Letter of Credit (500 units) aligns perfectly with the quantity stated in the Packing List (500 units). There is no compliance impact as no discrepancy exists.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Quantity: 500 units  
  - Target (Packing List): Quantity: 500 units  
  - Difference: None; values are identical.  
Severity Level: Low  
Golden Truth Value: 500 units  
Secondary Document Value: 500 units  
Impact: No risk of refusal or rejection as the documents are consistent.
---
#### Serial ID: 15  
Type: Shipment Terms Discrepancy  
Discrepancy ID: ST-015  
Discrepancy Title: Partial Shipment Allowance Mismatch  
Discrepancy Short Detail: Partial shipment terms differ between LC and Packing List.  
Discrepancy Long Detail: The Letter of Credit explicitly states that partial shipments are not allowed, while the Packing List indicates that partial shipments are allowed. This discrepancy creates a compliance conflict, potentially leading to rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Partial Shipment: Not Allowed  
  - Target (Packing List): Partial Shipment: Allowed  
  - Difference: The LC prohibits partial shipments, but the Packing List permits them, creating a direct contradiction.  
Severity Level: High  
Golden Truth Value: Not Allowed  
Secondary Document Value: Allowed  
Impact: This discrepancy may result in the issuing bank refusing to honor the LC, causing delays and financial risks for the beneficiary.
---
#### Serial ID: 16  
Type: Port Discrepancy  
Discrepancy ID: PD-016  
Discrepancy Title: Port of Discharge Mismatch  
Discrepancy Short Detail: Port of discharge differs between LC and packing list.  
Discrepancy Long Detail: The Letter of Credit specifies the port of discharge as Jebel Ali Port, Dubai, UAE, while the packing list indicates Port Khalifa, Abu Dhabi, UAE. This discrepancy may lead to non-compliance with the LC terms, potentially resulting in rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Port of Discharge: Jebel Ali Port, Dubai, UAE  
  - Target (Packing List): Port of Discharge: Port Khalifa, Abu Dhabi, UAE  
  - Difference: The port of discharge specified in the packing list does not match the port stated in the LC.  
Severity Level: High  
Golden Truth Value: Jebel Ali Port, Dubai, UAE  
Secondary Document Value: Port Khalifa, Abu Dhabi, UAE  
Impact: This discrepancy could result in the issuing bank refusing to honor the LC, causing delays and financial risks for the beneficiary.
---
#### Serial ID: 17  
Type: Date Discrepancy  
Discrepancy ID: DT-017  
Discrepancy Title: Shipment Date Exceeds LC's Latest Shipment Date  
Discrepancy Short Detail: Shipment date in Packing List exceeds the LC's latest shipment date.  
Discrepancy Long Detail: The Packing List indicates a shipment date of 18 October 2025, which is later than the LC's stipulated latest shipment date of 15 October 2025. This discrepancy violates the terms of the LC and may lead to non-compliance or rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Date of Shipment: Latest Shipment Date: 15 October 2025  
  - Target (Packing List): Date of Shipment: 18 October 2025  
  - Difference: Shipment date in the Packing List exceeds the LC's latest permissible shipment date by 3 days.  
Severity Level: High  
Golden Truth Value: Latest Shipment Date: 15 October 2025  
Secondary Document Value: 18 October 2025  
Impact: The discrepancy may result in the issuing bank rejecting the documents, causing delays in payment and potential financial loss for the beneficiary.
---
#### Serial ID: 18  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-018  
Discrepancy Title: Mismatch in Goods Description Between LC and Quality Certificate  
Discrepancy Short Detail: Goods description differs between LC and Quality Certificate.  
Discrepancy Long Detail: The LC specifies "Lithium-Ion Batteries, UN 3480, Class 9," while the Quality Certificate describes "Rechargeable Lithium-Ion Batteries (Model LP-500)." This mismatch may lead to compliance issues and potential rejection by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Goods Description: Lithium-Ion Batteries, UN 3480, Class 9  
  - Target (Quality Certificate): Goods Description: Rechargeable Lithium-Ion Batteries (Model LP-500)  
  - Difference: The LC describes the goods using UN classification and hazard class, while the Quality Certificate uses a model-specific description without UN classification.  
Severity Level: Medium  
Golden Truth Value: Lithium-Ion Batteries, UN 3480, Class 9  
Secondary Document Value: Rechargeable Lithium-Ion Batteries (Model LP-500)  
Impact: This discrepancy may result in the issuing bank refusing payment due to non-conformance with LC terms, causing delays or financial loss.  
---
#### Serial ID: 19  
Type: Quantity Discrepancy  
Discrepancy ID: QT-019  
Discrepancy Title: Quantity Mismatch Between LC and Quality Certificate  
Discrepancy Short Detail: Quantity in LC is 500 units, but Quality Certificate shows 480 units.  
Discrepancy Long Detail: The Letter of Credit specifies a quantity of 500 units, while the Quality Certificate indicates only 480 units. This mismatch may lead to non-compliance with LC terms, risking rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Quantity: 500 units  
  - Target (Quality Certificate): Quantity: 480 units  
  - Difference: Quantity shortfall of 20 units in the Quality Certificate.  
Severity Level: Medium  
Golden Truth Value: 500 units  
Secondary Document Value: 480 units  
Impact: This discrepancy could result in the issuing bank refusing to honor the LC, potentially delaying payment and shipment acceptance.
---
#### Serial ID: 20  
Type: Port of Discharge Discrepancy  
Discrepancy ID: PD-020  
Discrepancy Title: Port of Discharge Mismatch  
Discrepancy Short Detail: Port of discharge differs between LC and Quality Certificate.  
Discrepancy Long Detail: The Letter of Credit specifies the port of discharge as Jebel Ali Port, Dubai, UAE, while the Quality Certificate lists it as Port Khalifa, Abu Dhabi, UAE. This discrepancy may lead to non-compliance with the LC terms, potentially resulting in rejection of the documents by the issuing bank.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Port of Discharge: Jebel Ali Port, Dubai, UAE  
  - Target (Quality Certificate): Port of Discharge: Port Khalifa, Abu Dhabi, UAE  
  - Difference: The specified ports of discharge do not match, indicating a deviation from the LC terms.  
Severity Level: High  
Golden Truth Value: Jebel Ali Port, Dubai, UAE  
Secondary Document Value: Port Khalifa, Abu Dhabi, UAE  
Impact: This discrepancy could result in the issuing bank refusing to honor the LC, causing delays and financial risks for the beneficiary.
