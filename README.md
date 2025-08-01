# Financial Data Parser

A Python system for parsing, analyzing, and storing structured financial data from Excel files. Built for extensibility, data intelligence, and clean reporting — ideal for banking, ledger management, and financial audits.

---

## Project Overview

This project is built in **4 phases**, each responsible for handling a different stage of the data pipeline:

| Phase | Description |
|-------|-------------|
| **Phase 1** | Read and explore Excel sheets from different bank or ledger sources |
| **Phase 2** | Detect and classify column data types intelligently (dates, numbers, strings) |
| **Phase 3** | Normalize diverse financial formats (currencies, date strings, Excel serials) |
| **Phase 4** | Store and query data efficiently with support for filtering and aggregation |

---

## Project Structure

```bash
financial-data-parser/
├── config
├── scripts
├── examples
├── data/ # Sample Excel files
├── src/
│ └── core/
│ ├── excel_processor.py # Phase 1: Excel reading & info
│ ├── type_detector.py # Phase 2: Data type classification
│ ├── format_parser.py # Phase 3: Format parsing (amounts, dates)
│ └── data_storage.py # Phase 4: Storage & querying
├── tests/ # Pytest test files
├── main.py # Runs the entire pipeline
├── requirements.txt # Python dependencies
└── setup.py # Optional setup for editable install
```

---

## Technologies Used

- Python 3.10+
- `pandas` & `openpyxl` for Excel reading
- `sqlite3` for in-memory storage
- `re`, `locale`, `decimal` for parsing logic
- `pytest` for unit testing

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/financial-data-parser.git
cd financial-data-parser

# 2. Create and activate virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate

# 3. Install Requirements
pip install -r requirements.txt

# 4. (Optional): Editable Install for Modular Reuse
pip install -e .

# 5. Install test dependencies
pip install pytest
```

---

## Running the Parser

```bash
# After setup, simply run:
python main.py
```

What It Does:
- Loads Excel files from the /data/sample/ folder
- Analyzes and displays:
- Sheet structures
- Column data types
- Preview of raw and parsed data
- Parses different currency and date formats
- Stores results in SQLite memory
- Shows aggregation sample output

---

## Running tests

```bash
# We use pytest to validate all phases of the system:
pytest tests/
```
