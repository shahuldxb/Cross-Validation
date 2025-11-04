# Trade Finance Compliance Analysis Report
**Generated:** 2025-09-22 15:04:01
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
| Letter of Credit | Certificate of Origin | Goods Description | Lithium-Ion Batteries, UN 3480, Class 9 | Rechargeable Batteries for Consumer Devices (Nickel-Metal Hydride) | Mismatch in goods description. |
| Letter of Credit | Certificate of Origin | Quantity | 500 units | 480 units | Quantity mismatch. |
| Letter of Credit | Certificate of Origin | Date of Export | N/A | 20 October 2025 | Date of export exceeds latest shipment date. |
| Letter of Credit | Commercial Invoice | Goods Description | Lithium-Ion Batteries, UN 3480, Class 9 | Rechargeable Lithium-Ion Batteries (Model LP-500) | Mismatch in goods description. |
| Letter of Credit | Commercial Invoice | Quantity | 500 units | 520 units | Quantity mismatch. |
| Letter of Credit | Commercial Invoice | Total Amount | USD 75,000.00 | USD 76,440.00 | Amount mismatch. |
| Letter of Credit | Commercial Invoice | Incoterms | CIF Jebel Ali Port, Dubai, UAE | FOB Yantian Port, China | Incoterms mismatch. |
| Letter of Credit | Dangerous Goods Declaration | Goods Description | Lithium-Ion Batteries, UN 3480, Class 9 | Lithium Metal Batteries | Mismatch in goods description. |
| Letter of Credit | Dangerous Goods Declaration | UN Number | UN 3480 | UN 3090 | UN number mismatch. |
| Letter of Credit | Dangerous Goods Declaration | Port of Discharge | Jebel Ali Port, Dubai, UAE | Port Khalifa, Abu Dhabi, UAE | Port of discharge mismatch. |
| Letter of Credit | Packing List | Quantity | 500 units | 500 units | Partial shipment allowed in packing list but not in LC. |
| Letter of Credit | Packing List | Port of Discharge | Jebel Ali Port, Dubai, UAE | Port Khalifa, Abu Dhabi, UAE | Port of discharge mismatch. |
| Letter of Credit | Quality Certificate | Quantity | 500 units | 480 units | Quantity mismatch. |

---

### Detailed Analysis

**GOLDEN TRUTH DOCUMENT:** Letter of Credit (LC) - ilc.txt  
**SECONDARY DOCUMENTS FOUND:** Certificate of Origin, Commercial Invoice, Dangerous Goods Declaration, Packing List, Quality Certificate  
**TOTAL DISCREPANCIES FOUND:** 13  

---

#### Discrepancy 1
Serial ID: 1  
Type: Description Discrepancy  
Discrepancy ID: DESC-001  
Discrepancy Title: Goods Description Mismatch in Certificate of Origin  
Discrepancy Short Detail: Goods description differs between LC and Certificate of Origin.  
Discrepancy Long Detail: The LC specifies "Lithium-Ion Batteries, UN 3480, Class 9," while the Certificate of Origin lists "Rechargeable Batteries for Consumer Devices (Nickel-Metal Hydride)." This discrepancy could lead to rejection due to incorrect product identification.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Goods Description: Lithium-Ion Batteries, UN 3480, Class 9  
  - Target (Certificate of Origin): Goods Description: Rechargeable Batteries for Consumer Devices (Nickel-Metal Hydride)  
  - Difference: Mismatch in product type and classification.  
Severity Level: High  
Golden Truth Value: Lithium-Ion Batteries, UN 3480, Class 9  
Secondary Document Value: Rechargeable Batteries for Consumer Devices (Nickel-Metal Hydride)  
Impact: Risk of rejection due to non-compliance with LC terms.

---

#### Discrepancy 2
Serial ID: 2  
Type: Quantity Discrepancy  
Discrepancy ID: QTY-001  
Discrepancy Title: Quantity Mismatch in Certificate of Origin  
Discrepancy Short Detail: Quantity differs between LC and Certificate of Origin.  
Discrepancy Long Detail: The LC specifies 500 units, while the Certificate of Origin lists 480 units. This discrepancy could lead to rejection due to insufficient quantity.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Quantity: 500 units  
  - Target (Certificate of Origin): Quantity: 480 units  
  - Difference: Shortfall of 20 units.  
Severity Level: Medium  
Golden Truth Value: 500 units  
Secondary Document Value: 480 units  
Impact: Risk of rejection due to quantity shortfall.

---

#### Discrepancy 3
Serial ID: 3  
Type: Date Discrepancy  
Discrepancy ID: DATE-001  
Discrepancy Title: Date of Export Exceeds Latest Shipment Date  
Discrepancy Short Detail: Export date in Certificate of Origin exceeds LC's latest shipment date.  
Discrepancy Long Detail: The LC specifies a latest shipment date of 15 October 2025, but the Certificate of Origin lists an export date of 20 October 2025. This discrepancy violates LC terms and could lead to rejection.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Latest Shipment Date: 15 October 2025  
  - Target (Certificate of Origin): Date of Export: 20 October 2025  
  - Difference: Export date exceeds LC terms by 5 days.  
Severity Level: Critical  
Golden Truth Value: 15 October 2025  
Secondary Document Value: 20 October 2025  
Impact: Risk of rejection due to non-compliance with shipment deadline.

---

#### Discrepancy 4
Serial ID: 4  
Type: Description Discrepancy  
Discrepancy ID: DESC-002  
Discrepancy Title: Goods Description Mismatch in Commercial Invoice  
Discrepancy Short Detail: Goods description differs between LC and Commercial Invoice.  
Discrepancy Long Detail: The LC specifies "Lithium-Ion Batteries, UN 3480, Class 9," while the Commercial Invoice lists "Rechargeable Lithium-Ion Batteries (Model LP-500)." This discrepancy could lead to rejection due to incorrect product identification.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Goods Description: Lithium-Ion Batteries, UN 3480, Class 9  
  - Target (Commercial Invoice): Goods Description: Rechargeable Lithium-Ion Batteries (Model LP-500)  
  - Difference: Mismatch in product type and classification.  
Severity Level: High  
Golden Truth Value: Lithium-Ion Batteries, UN 3480, Class 9  
Secondary Document Value: Rechargeable Lithium-Ion Batteries (Model LP-500)  
Impact: Risk of rejection due to non-compliance with LC terms.

---

#### Discrepancy 5
Serial ID: 5  
Type: Quantity Discrepancy  
Discrepancy ID: QTY-002  
Discrepancy Title: Quantity Mismatch in Commercial Invoice  
Discrepancy Short Detail: Quantity differs between LC and Commercial Invoice.  
Discrepancy Long Detail: The LC specifies 500 units, while the Commercial Invoice lists 520 units. This discrepancy could lead to rejection due to excess quantity.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Quantity: 500 units  
  - Target (Commercial Invoice): Quantity: 520 units  
  - Difference: Excess of 20 units.  
Severity Level: Medium  
Golden Truth Value: 500 units  
Secondary Document Value: 520 units  
Impact: Risk of rejection due to excess quantity.

---

#### Discrepancy 6
Serial ID: 6  
Type: Amount Discrepancy  
Discrepancy ID: AMT-001  
Discrepancy Title: Amount Mismatch in Commercial Invoice  
Discrepancy Short Detail: Total amount differs between LC and Commercial Invoice.  
Discrepancy Long Detail: The LC specifies USD 75,000.00, while the Commercial Invoice lists USD 76,440.00. This discrepancy could lead to rejection due to incorrect payment terms.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Total Amount: USD 75,000.00  
  - Target (Commercial Invoice): Total Amount: USD 76,440.00  
  - Difference: Excess of USD 1,440.00.  
Severity Level: High  
Golden Truth Value: USD 75,000.00  
Secondary Document Value: USD 76,440.00  
Impact: Risk of rejection due to incorrect payment terms.

---

#### Discrepancy 7
Serial ID: 7  
Type: Incoterms Discrepancy  
Discrepancy ID: INC-001  
Discrepancy Title: Incoterms Mismatch in Commercial Invoice  
Discrepancy Short Detail: Incoterms differ between LC and Commercial Invoice.  
Discrepancy Long Detail: The LC specifies "CIF Jebel Ali Port, Dubai, UAE," while the Commercial Invoice lists "FOB Yantian Port, China." This discrepancy could lead to rejection due to incorrect shipping terms.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Incoterms: CIF Jebel Ali Port, Dubai, UAE  
  - Target (Commercial Invoice): Incoterms: FOB Yantian Port, China  
  - Difference: Mismatch in shipping terms.  
Severity Level: High  
Golden Truth Value: CIF Jebel Ali Port, Dubai, UAE  
Secondary Document Value: FOB Yantian Port, China  
Impact: Risk of rejection due to non-compliance with LC terms.

---

#### Discrepancy 8
Serial ID: 8  
Type: Description Discrepancy  
Discrepancy ID: DESC-003  
Discrepancy Title: Goods Description Mismatch in Dangerous Goods Declaration  
Discrepancy Short Detail: Goods description differs between LC and Dangerous Goods Declaration.  
Discrepancy Long Detail: The LC specifies "Lithium-Ion Batteries, UN 3480, Class 9," while the Dangerous Goods Declaration lists "Lithium Metal Batteries." This discrepancy could lead to rejection due to incorrect product identification.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Goods Description: Lithium-Ion Batteries, UN 3480, Class 9  
  - Target (Dangerous Goods Declaration): Goods Description: Lithium Metal Batteries  
  - Difference: Mismatch in product type and classification.  
Severity Level: High  
Golden Truth Value: Lithium-Ion Batteries, UN 3480, Class 9  
Secondary Document Value: Lithium Metal Batteries  
Impact: Risk of rejection due to non-compliance with LC terms.

---

#### Discrepancy 9
Serial ID: 9  
Type: UN Number Discrepancy  
Discrepancy ID: UN-001  
Discrepancy Title: UN Number Mismatch in Dangerous Goods Declaration  
Discrepancy Short Detail: UN number differs between LC and Dangerous Goods Declaration.  
Discrepancy Long Detail: The LC specifies UN 3480, while the Dangerous Goods Declaration lists UN 3090. This discrepancy could lead to rejection due to incorrect classification.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): UN Number: UN 3480  
  - Target (Dangerous Goods Declaration): UN Number: UN 3090  
  - Difference: Mismatch in UN classification.  
Severity Level: High  
Golden Truth Value: UN 3480  
Secondary Document Value: UN 3090  
Impact: Risk of rejection due to non-compliance with LC terms.

---

#### Discrepancy 10
Serial ID: 10  
Type: Port Discrepancy  
Discrepancy ID: PORT-001  
Discrepancy Title: Port of Discharge Mismatch in Dangerous Goods Declaration  
Discrepancy Short Detail: Port of discharge differs between LC and Dangerous Goods Declaration.  
Discrepancy Long Detail: The LC specifies "Jebel Ali Port, Dubai, UAE," while the Dangerous Goods Declaration lists "Port Khalifa, Abu Dhabi, UAE." This discrepancy could lead to rejection due to incorrect shipping destination.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Port of Discharge: Jebel Ali Port, Dubai, UAE  
  - Target (Dangerous Goods Declaration): Port of Discharge: Port Khalifa, Abu Dhabi, UAE  
  - Difference: Mismatch in shipping destination.  
Severity Level: High  
Golden Truth Value: Jebel Ali Port, Dubai, UAE  
Secondary Document Value: Port Khalifa, Abu Dhabi, UAE  
Impact: Risk of rejection due to non-compliance with LC terms.

---

#### Discrepancy 11
Serial ID: 11  
Type: Shipment Terms Discrepancy  
Discrepancy ID: SHIP-001  
Discrepancy Title: Partial Shipment Allowed in Packing List  
Discrepancy Short Detail: Partial shipment allowed in Packing List but not in LC.  
Discrepancy Long Detail: The LC specifies "Partial Shipments: Not Allowed," while the Packing List indicates partial shipment is allowed. This discrepancy could lead to rejection due to non-compliance with LC terms.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Partial Shipments: Not Allowed  
  - Target (Packing List): Partial Shipments: Allowed  
  - Difference: Mismatch in shipment terms.  
Severity Level: High  
Golden Truth Value: Not Allowed  
Secondary Document Value: Allowed  
Impact: Risk of rejection due to non-compliance with LC terms.

---

#### Discrepancy 12
Serial ID: 12  
Type: Port Discrepancy  
Discrepancy ID: PORT-002  
Discrepancy Title: Port of Discharge Mismatch in Packing List  
Discrepancy Short Detail: Port of discharge differs between LC and Packing List.  
Discrepancy Long Detail: The LC specifies "Jebel Ali Port, Dubai, UAE," while the Packing List lists "Port Khalifa, Abu Dhabi, UAE." This discrepancy could lead to rejection due to incorrect shipping destination.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Port of Discharge: Jebel Ali Port, Dubai, UAE  
  - Target (Packing List): Port of Discharge: Port Khalifa, Abu Dhabi, UAE  
  - Difference: Mismatch in shipping destination.  
Severity Level: High  
Golden Truth Value: Jebel Ali Port, Dubai, UAE  
Secondary Document Value: Port Khalifa, Abu Dhabi, UAE  
Impact: Risk of rejection due to non-compliance with LC terms.

---

#### Discrepancy 13
Serial ID: 13  
Type: Quantity Discrepancy  
Discrepancy ID: QTY-003  
Discrepancy Title: Quantity Mismatch in Quality Certificate  
Discrepancy Short Detail: Quantity differs between LC and Quality Certificate.  
Discrepancy Long Detail: The LC specifies 500 units, while the Quality Certificate lists 480 units. This discrepancy could lead to rejection due to insufficient quantity.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Quantity: 500 units  
  - Target (Quality Certificate): Quantity: 480 units  
  - Difference: Shortfall of 20 units.  
Severity Level: Medium  
Golden Truth Value: 500 units  
Secondary Document Value: 480 units  
Impact: Risk of rejection due to quantity shortfall.

--- 

This exhaustive analysis ensures all discrepancies are identified and documented for compliance review.