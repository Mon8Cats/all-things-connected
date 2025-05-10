# HL7

## Segments

1. MSH* (Message Header)
2. PIP* (Patient Identification)
3. PV1 (Patient Visit) - for each doctor
4. OBR (Observation Request) - for each test
5. OBX (Observation/Result)
6. AL1 (Allergy Information)
7. DG1 (Diagnosis)
8. PR1 (Procedures) - for each procedure
9. IN1 (Insurance) - for each plan
10. NK1 (Next of Kin)
11. ORC (Common Order)
12. RXA (Pharmacy/Treatment Administration) - for each treatment
13. RXR (Pharmacy/Treatment Route) for each treatment

```bash
MSH|^~\&|SendingApp|SendingFacility|ReceivingApp|ReceivingFacility|202105061200||ADT^A01|123456|P|2.5
PID|1||123456^^^Hospital^MR||Doe^John||19800101|M|||123 Main St^^Anytown^TX^12345||(123)456-7890|||M|123456789|987654321
PV1|1|I|2000^2012^01||||12345^Smith^John|12345^Smith^John|||||||||||1234567890
PV1|2|I|2000^2012^01||||67890^Jones^Alice|67890^Jones^Alice|||||||||||1234567890
PR1|1|A1234^Appendectomy||20210506
PR1|2|B5678^Cholecystectomy||20210506



MSH|^~\&|SendingApp|SendingFacility|ReceivingApp|ReceivingFacility|202105061200||ADT^A01|123456|P|2.5
PID|1||123456^^^Hospital^MR||Doe^John||19800101|M|||123 Main St^^Anytown^TX^12345||(123)456-7890|||M|123456789|987654321
PV1|1|I|2000^2012^01||||12345^Smith^John|12345^Smith^John|||||||||||1234567890
PV1|2|I|2000^2012^01||||67890^Jones^Alice|67890^Jones^Alice|||||||||||1234567890
PR1|1|A1234^Appendectomy||20210506
PR1|2|B5678^Cholecystectomy||20210506
OBR|1|123456|123456|CBC^Complete Blood Count|||202105061200
OBX|1|NM|1234-5^Hemoglobin||13.5|g/dL|12.0-16.0|N|||F
AL1|1|DA|^Penicillin||Hives
DG1|1||A1234^Hypertension||20210506
IN1|1|12345|Blue Cross|123 Main St^^Anytown^TX^12345||(123)456-7890|Doe^John
NK1|1|Doe^Jane|SPO||(123)456-7890
RXA|0|1|202105061200|202105061230|123456^Aspirin|500|mg
RXR|PO^Oral


```