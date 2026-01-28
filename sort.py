import pdfplumber
import pandas as pd
import re

PDF_PATH = r"INVOICE.PDF"
OUTPUT_EXCEL = "final_invoice.xlsx"


# ---------------------------
# Extract text from PDF
# ---------------------------
def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text


# ---------------------------
# Extract structured fields
# ---------------------------
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
        "Order Numbers": r"ORDER NUMBERS.*\n([^\n]+)",
        "Total PKR": r"TOTAL PKR\s+([\d,\.]+)"
    }

    data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        data[key] = match.group(1).strip() if match else ""

    return data


# ---------------------------
# Extract charges table
# ---------------------------
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


# ---------------------------
# Save Excel
# ---------------------------
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
