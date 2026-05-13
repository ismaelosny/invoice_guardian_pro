# 🛡️ Invoice Guardian Pro: Intelligent Multi-Layout PDF Extractor

**Invoice Guardian Pro** is a robust Python-based automation tool designed to solve a common bottleneck in accounting and finance departments: manual data entry from inconsistent invoice layouts. 

Using advanced **Regular Expressions (Regex)** and the **pdfplumber** library, this tool identifies and extracts critical fiscal data (CNPJ, Invoice Number, Issue Date, and Total Value) regardless of where they are positioned in the document.

---

## 🚀 Key Features

* **Layout Agnostic:** Successfully extracts data from traditional, modern, and complex/unstructured PDF layouts.
* **Regex-Powered Intelligence:** Uses smart pattern matching to find fiscal data hidden within dense text blocks.
* **Automated Consolidation:** Processes multiple files in a batch and consolidates them into a single, clean Excel (.xlsx) report.
* **Data Cleaning:** Automatically handles currency formatting and date normalization for professional use.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Libraries:** * `pdfplumber` (PDF text and table extraction)
    * `pandas` (Data manipulation and structuring)
    * `re` (Advanced Regular Expressions)
    * `openpyxl` (Excel engine)

## 📁 Project Structure

* `src/`: Core logic (Extractor, Exporter, and Main orchestrator).
* `raw_invoices/`: Input folder for PDF documents.
* `data/`: Output folder for the generated Excel reports.
* `requirements.txt`: Project dependencies for easy setup.

## ⚙️ How to Run

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Place your PDF invoices in the `raw_invoices/` folder.
4.  Run the main script:
    ```bash
    python src/main.py
    ```

---

## 📊 Sample Output (Terminal Preview)

| FILE | CNPJ | DATE | INVOICE # | TOTAL |
| :--- | :--- | :--- | :--- | :--- |
| fatura_modelo_A.pdf | 12.345.678/0001-90 | 15/04/2026 | 2026-001 | R$ 650,00 |
| fatura_modelo_C.pdf | 55.444.333/0002-22 | 12/05/2026 | NF-5544 | R$ 4.890,50 |

---
**Developed by Ismael Osny Schmitz** *Focused on Finance Automation and Data Intelligence.*
