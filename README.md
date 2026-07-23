# Python Automation Toolkit

A Python-based automation project containing practical tools for **PDF data extraction** and **browser automation**.

The project demonstrates how Python can automate repetitive tasks such as extracting structured invoice data into Excel and testing website login/logout workflows using Selenium.

---

## 🚀 Features

### 📄 PDF Invoice to Excel

- Extracts text from PDF invoices
- Uses Regex to identify structured invoice information
- Extracts invoice details such as:
  - Invoice Number
  - Invoice Date
  - Customer ID
  - Shipment
  - Client NTN
  - Due Date
  - Shipper & Consignee
  - Origin & Destination
  - ETD & ETA
  - Weight & Volume
  - Package information
  - Bill of Lading details
  - Container information
  - Subtotal, VAT & Total
- Extracts individual invoice charges
- Automatically generates an Excel workbook
- Creates separate `Summary` and `Charges` worksheets

### 🌐 Selenium Browser Automation

- Automates Chrome using Selenium
- Opens the target website automatically
- Navigates to the login page
- Enters login credentials
- Validates successful login
- Checks whether the Logout button is displayed
- Automatically performs logout
- Validates successful logout
- Uses explicit waits for reliable element interaction
- Automatically closes the browser after execution

---

## 🛠️ Tech Stack

- Python
- Selenium
- Undetected ChromeDriver
- PDFPlumber
- Pandas
- OpenPyXL
- Regular Expressions (Regex)

---

## 📂 Project Structure

```text
Python-Automation/
│
├── main.py
├── pdf_to_excel.py
├── requirements.txt
├── README.md
│
├── INVOICE.PDF
└── final_invoice.xlsx
```

> File names can be adjusted according to your actual project structure.

---

# 📄 PDF to Excel Automation

## How It Works

The PDF automation follows this workflow:

```text
PDF Invoice
     │
     ▼
Extract Text
     │
     ▼
Regex Data Extraction
     │
     ├── Invoice Summary
     │
     └── Charges
     │
     ▼
Pandas DataFrames
     │
     ▼
Excel Workbook
     │
     ├── Summary Sheet
     └── Charges Sheet
```

---

## Configuration

Set the input PDF and output Excel file:

```python
PDF_PATH = r"INVOICE.PDF"
OUTPUT_EXCEL = "final_invoice.xlsx"
```

Replace `INVOICE.PDF` with the path to your invoice.

Example:

```python
PDF_PATH = r"C:\Invoices\invoice.pdf"
```

---

## Excel Output

After processing the PDF, the application generates:

```text
final_invoice.xlsx
```

The workbook contains two worksheets.

### Summary

Contains general invoice information such as:

| Invoice Number | Invoice Date | Customer ID | Due Date | Total PKR |
|---|---|---|---|---|

### Charges

Contains individual invoice charges:

| Description | Amount | Currency |
|---|---:|---|
| Example Charge | 5000.00 | PKR |

---

# 🌐 Selenium Browser Automation

The browser automation script demonstrates automated testing of a login and logout workflow.

It uses:

```text
the-internet.herokuapp.com
```

as the demonstration website.

---

## Automation Workflow

```text
Launch Chrome
     │
     ▼
Open Website
     │
     ▼
Navigate to Login
     │
     ▼
Enter Credentials
     │
     ▼
Login
     │
     ▼
Validate Login
     │
     ▼
Logout
     │
     ▼
Validate Logout
     │
     ▼
Close Browser
```

---

## Login Validation

After submitting the credentials, the script checks:

- Successful login message
- Visibility of the Logout button

Successful execution prints:

```text
✅ Login successful & Logout button visible
```

---

## Logout Validation

After logging out, the script checks:

- Successful logout message
- Username field is displayed again
- Password field is displayed again

Successful execution prints:

```text
✅ Logout successful & Login page displayed again
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_REPOSITORY_NAME>
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Main dependencies include:

```text
selenium
undetected-chromedriver
pdfplumber
pandas
openpyxl
```

---

# ▶️ Running the Project

## Run PDF to Excel Automation

```bash
python pdf_to_excel.py
```

After successful execution:

```text
✅ Excel created: final_invoice.xlsx
```

---

## Run Selenium Automation

```bash
python main.py
```

Chrome will automatically open and execute the complete login/logout workflow.

---

# 💡 What This Project Demonstrates

This project demonstrates practical experience with:

- Python automation
- Browser automation
- Selenium WebDriver
- Web element interaction
- Automated workflow validation
- PDF text extraction
- Regular expressions
- Data parsing and transformation
- Pandas data processing
- Excel file generation
- Exception handling

---

# 🔮 Future Improvements

- Move configuration to `.env` files
- Remove hardcoded credentials
- Add Pytest automated test cases
- Add structured logging
- Support multiple invoice formats
- Process multiple PDFs in bulk
- Improve Regex extraction accuracy
- Add OCR support for scanned PDFs
- Add Selenium Page Object Model (POM)
- Generate automated test reports
- Add Docker support
- Add CI/CD workflow

---

# 👨‍💻 Author

**Syed Muhammad Jawwad Irshad**

Python Backend Engineer

GitHub: `JawwadIrshad`
