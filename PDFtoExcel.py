#PDFtoExcel File
import pdfplumber
import pandas as pd
import re

import data

PDF_PATH = r"INVOICE.PDF"
OUTPUT_EXCEL = "final_invoice.xlsx"

def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text

def extract_summary(text):
    patterns = {
        "Invoice Number": r"INVOICE\s+([A-Z0-9]+)",
        "Invoice Date": r"INVOICE DATE\s+([^\n]+)",
        "Customer ID": r"CUSTOMER ID\s+([^\n]+)",
        "Shipment": r"SHIPMENT\s+([^\n]+)",
        "Client NTN": r"CLIENT NTN\s+#\s+([^\n]+)",
        "Due Date": r"DUE DATE\s+([^\n]+)",
        "Terms": r"TERMS\s+([^\n]+)",

        "Shipper": r"SHIPPER\s*\n([^\n]+)",
        "Consignee": r"CONSIGNEE\s*\n([^\n]+)",

        "Origin": r"(PK[A-Z]{3}\s*=\s*[^0-9\n]+)",
        "ETD": r"\b(\d{2}-[A-Za-z]{3}-\d{2})\b",
        "Destination": r"(CZ[A-Z]{3}\s*=\s*[^0-9\n]+)",
        "ETA": r"\b\d{2}-[A-Za-z]{3}-\d{2}\s+\b(\d{2}-[A-Za-z]{3}-\d{2})\b",

        "Weight (KG)": r"([\d\.]+)\s+KG",
        "Volume (M3)": r"KG\s+([\d\.]+)\s+M3",
        "Chargeable Volume (M3)": r"M3\s+([\d\.]+)\s+M3",
        "Packages": r"(\d+)\s+CTN",

        "Ocean BL": r"(HLCU[A-Z0-9]+)",
        "House BL": r"(KHI[0-9A-Z]+)",

        "Container": r"UETU[0-9A-Z\- ]+",

        "Subtotal PKR": r"SUBTOTAL\s+([\d,\.]+)",
        "VAT PKR": r"ADD VAT\s+([\d,\.]+)",
        "Total PKR": r"TOTAL PKR\s+([\d,\.]+)"
    }

    data = {}
    for field, regex in patterns.items():
        match = re.search(regex, text)
        if match:
            if match.groups():
                data[field] = match.group(1).strip()
            else:
                data[field] = match.group(0).strip()
        else:
            data[field] = ""

    return data

def extract_charges(text):
    lines = text.splitlines()
    rows = []
    capture = False

    for line in lines:
        if "CHARGES" in line:
            capture = True
            continue

        if capture:
            if "TOTAL" in line or "SUBTOTAL" in line:
                break

            match = re.search(r"(.+?)\s+([\d,]+\.\d{2})$", line)
            if match:
                rows.append({
                    "Description": match.group(1).strip(),
                    "Amount": float(match.group(2).replace(",", "")),
                    "Currency": "PKR"
                })

    return rows


def save_excel(summary, charges, output):
    df_summary = pd.DataFrame([summary])
    df_charges = pd.DataFrame(charges)

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df_summary.to_excel(writer, sheet_name="Summary", index=False)
        df_charges.to_excel(writer, sheet_name="Charges", index=False)


# ---------------------------
# Run
# ---------------------------
if __name__ == "__main__":
    text = extract_text(PDF_PATH)

    summary = extract_summary(text)
    charges = extract_charges(text)

    save_excel(summary, charges, OUTPUT_EXCEL)

    print("✅ Excel created:", OUTPUT_EXCEL)
