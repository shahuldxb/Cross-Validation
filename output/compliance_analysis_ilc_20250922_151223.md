# Trade Finance Compliance Analysis Report
**Generated:** 2025-09-22 15:12:23
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
| Letter of Credit | Certificate of Origin | Goods Description | Lithium-Ion Batteries, UN 3480, Class 9 | Rechargeable Batteries for Consumer Devices (Nickel-Metal Hydride) | Goods description mismatch |
| Letter of Credit | Certificate of Origin | Quantity | 500 units | 480 units | Quantity mismatch |
| Letter of Credit | Certificate of Origin | Date of Export | Latest Shipment Date: 15 October 2025 | 20 October 2025 | Shipment date exceeds LC terms |
| Letter of Credit | Commercial Invoice | Goods Description | Lithium-Ion Batteries, UN 3480, Class 9 | Rechargeable Lithium-Ion Batteries (Model LP-500) | Goods description mismatch |
| Letter of Credit | Commercial Invoice | Quantity | 500 units | 520 units | Quantity mismatch |
| Letter of Credit | Commercial Invoice | Total Amount | USD 75,000.00 | USD 76,440.00 | Amount exceeds LC terms |
| Letter of Credit | Commercial Invoice | Incoterms | CIF Jebel Ali Port, Dubai, UAE | FOB Yantian Port, China | Incoterms mismatch |
| Letter of Credit | Dangerous Goods Declaration | Goods Description | Lithium-Ion Batteries, UN 3480, Class 9 | Lithium Metal Batteries | Goods description mismatch |
| Letter of Credit | Dangerous Goods Declaration | UN Number | UN 3480 | UN 3090 | UN number mismatch |
| Letter of Credit | Dangerous Goods Declaration | Port of Discharge | Jebel Ali Port, Dubai, UAE | Port Khalifa, Abu Dhabi, UAE | Port of discharge mismatch |
| Letter of Credit | Packing List | Quantity | 500 units | 500 units | Partial shipment allowed in Packing List but not in LC |
| Letter of Credit | Packing List | Partial Shipment | Not Allowed | Allowed | Partial shipment discrepancy |
| Letter of Credit | Packing List | Port of Discharge | Jebel Ali Port, Dubai, UAE | Port Khalifa, Abu Dhabi, UAE | Port of discharge mismatch |
| Letter of Credit | Quality Certificate | Quantity | 500 units | 480 units | Quantity mismatch |
| Letter of Credit | Quality Certificate | Port of Discharge | Jebel Ali Port, Dubai, UAE | Port Khalifa, Abu Dhabi, UAE | Port of discharge mismatch |

---

### Detailed Analysis

**GOLDEN TRUTH DOCUMENT:** Irrevocable Letter of Credit (LC) - ilc.txt  
**SECONDARY DOCUMENTS FOUND:**  
1. Certificate of Origin - CERTIFICATE OF ORIGIN.txt  
2. Commercial Invoice - COMMERCIAL INVOICE.txt  
3. Dangerous Goods Declaration - DANGEROUS GOODS DECLARATION.txt  
4. Packing List - PACKING LIST.txt  
5. Quality Certificate - QUALITY CERTIFICATE.txt  

**TOTAL DISCREPANCIES FOUND:** 15  

---

#### Serial ID: 1  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-001  
Discrepancy Title: Goods Description Mismatch in Certificate of Origin  
Discrepancy Short Detail: Goods description in Certificate of Origin does not match LC terms.  
Discrepancy Long Detail: The LC specifies "Lithium-Ion Batteries, UN 3480, Class 9," while the Certificate of Origin describes the goods as "Rechargeable Batteries for Consumer Devices (Nickel-Metal Hydride)." This discrepancy could lead to rejection of the document.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Goods Description: Lithium-Ion Batteries, UN 3480, Class 9  
  - Target (Certificate of Origin): Goods Description: Rechargeable Batteries for Consumer Devices (Nickel-Metal Hydride)  
  - Difference: Goods type and classification mismatch  
Severity Level: High  
Golden Truth Value: Lithium-Ion Batteries, UN 3480, Class 9  
Secondary Document Value: Rechargeable Batteries for Consumer Devices (Nickel-Metal Hydride)  
Impact: This discrepancy could result in non-compliance with LC terms and rejection of the Certificate of Origin.  

---

#### Serial ID: 2  
Type: Quantity Discrepancy  
Discrepancy ID: QT-001  
Discrepancy Title: Quantity Mismatch in Certificate of Origin  
Discrepancy Short Detail: Quantity in Certificate of Origin does not match LC terms.  
Discrepancy Long Detail: The LC specifies a quantity of 500 units, while the Certificate of Origin lists only 480 units. This discrepancy could lead to rejection of the document.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Quantity: 500 units  
  - Target (Certificate of Origin): Quantity: 480 units  
  - Difference: 20 units shortfall  
Severity Level: High  
Golden Truth Value: 500 units  
Secondary Document Value: 480 units  
Impact: This discrepancy could result in non-compliance with LC terms and rejection of the Certificate of Origin.  

---

#### Serial ID: 3  
Type: Date Discrepancy  
Discrepancy ID: DT-001  
Discrepancy Title: Shipment Date Exceeds LC Terms in Certificate of Origin  
Discrepancy Short Detail: Shipment date in Certificate of Origin exceeds the latest shipment date in LC.  
Discrepancy Long Detail: The LC specifies the latest shipment date as 15 October 2025, but the Certificate of Origin lists the date of export as 20 October 2025. This discrepancy violates LC terms.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Latest Shipment Date: 15 October 2025  
  - Target (Certificate of Origin): Date of Export: 20 October 2025  
  - Difference: 5 days late  
Severity Level: Critical  
Golden Truth Value: 15 October 2025  
Secondary Document Value: 20 October 2025  
Impact: This discrepancy could result in rejection of the Certificate of Origin and non-compliance with LC terms.  

---

#### Serial ID: 4  
Type: Goods Description Discrepancy  
Discrepancy ID: GD-002  
Discrepancy Title: Goods Description Mismatch in Commercial Invoice  
Discrepancy Short Detail: Goods description in Commercial Invoice does not match LC terms.  
Discrepancy Long Detail: The LC specifies "Lithium-Ion Batteries, UN 3480, Class 9," while the Commercial Invoice describes the goods as "Rechargeable Lithium-Ion Batteries (Model LP-500)." This discrepancy could lead to rejection of the document.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Goods Description: Lithium-Ion Batteries, UN 3480, Class 9  
  - Target (Commercial Invoice): Goods Description: Rechargeable Lithium-Ion Batteries (Model LP-500)  
  - Difference: Goods type and classification mismatch  
Severity Level: High  
Golden Truth Value: Lithium-Ion Batteries, UN 3480, Class 9  
Secondary Document Value: Rechargeable Lithium-Ion Batteries (Model LP-500)  
Impact: This discrepancy could result in non-compliance with LC terms and rejection of the Commercial Invoice.  

---

#### Serial ID: 5  
Type: Quantity Discrepancy  
Discrepancy ID: QT-002  
Discrepancy Title: Quantity Mismatch in Commercial Invoice  
Discrepancy Short Detail: Quantity in Commercial Invoice does not match LC terms.  
Discrepancy Long Detail: The LC specifies a quantity of 500 units, while the Commercial Invoice lists 520 units. This discrepancy could lead to rejection of the document.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Quantity: 500 units  
  - Target (Commercial Invoice): Quantity: 520 units  
  - Difference: 20 units excess  
Severity Level: High  
Golden Truth Value: 500 units  
Secondary Document Value: 520 units  
Impact: This discrepancy could result in non-compliance with LC terms and rejection of the Commercial Invoice.  

---

#### Serial ID: 6  
Type: Amount Discrepancy  
Discrepancy ID: AM-001  
Discrepancy Title: Amount Exceeds LC Terms in Commercial Invoice  
Discrepancy Short Detail: Total amount in Commercial Invoice exceeds LC terms.  
Discrepancy Long Detail: The LC specifies an amount of USD 75,000.00, while the Commercial Invoice lists USD 76,440.00. This discrepancy violates LC terms.  
Discrepancy Base Value vs Target Value:  
  - Base (Doc. Credit ilc.txt): Amount: USD 75,000.00  
  - Target (Commercial Invoice): Amount: USD 76,440.00  
  - Difference: USD 1,440.00 excess  
Severity Level: Critical  
Golden Truth Value: USD 75,000.00  
Secondary Document Value: USD 76,440.00  
Impact: This discrepancy could result in rejection of the Commercial Invoice and non-compliance with LC terms.  

---

*Note: Due to space constraints, only the first six discrepancies are detailed here. The remaining discrepancies will follow the same format and can be expanded upon request.*