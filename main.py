import random
from src.core.excel_processor import ExcelProcessor
from src.core.type_detector import DataTypeDetector
from src.core.format_parser import FormatParser
from src.core.data_storage import DataStorage

def main():
    print("🔍 Starting Financial Data Parser...")

    files = [
        "data/sample/KH_Bank.XLSX",
        "data/sample/Customer_Ledger_Entries_FULL.xlsx"
    ]

    # PHASE 1: Load and inspect Excel files
    processor = ExcelProcessor()
    processor.load_files(files)
    info = processor.get_sheet_info()
    print("\n📄 Phase 1: Basic Excel Processing:")
    for file, sheets in info.items():
        print(f"\nFile: {file}")
        for sheet, meta in sheets.items():
            print(f"  Sheet: {sheet} → Rows: {meta['rows']}, Columns: {meta['columns']}")
            print(f"    Columns: {meta['column_names']}")

    sample_sheet = list(info[files[0]].keys())[0]

    # PHASE 2: Type Detection
    detector = DataTypeDetector()
    df = processor.extract_data(files[0], sample_sheet)
    print("\n Phase 2: Data Type Detection:")
    for col in df.columns:
        col_type = detector.analyze_column(df[col])
        print(f"  {col}: {col_type}")

    # PHASE 3: Format Parsing
    parser = FormatParser()
    test_amounts = ["$1,234.56", "(2,500.00)", "€1.234,56", "1.5M", "₹1,23,456"]
    test_dates = ["12/31/2023", "2023-12-31", "Q4 2023", "Dec-23", "44927"]

    print("\n Phase 3: Format Parsing Challenges:")

    print("\n💰 Parsed Amounts:")
    for val in test_amounts:
        print(f"  {val} → {parser.parse_amount(val)}")

    print("\n📅 Parsed Dates:")
    for val in test_dates:
        print(f"  {val} → {parser.parse_date(val)}")

    # PHASE 4: Data Storage
    storage = DataStorage()
    storage.store_data(df, "financial_data")
    storage.create_indexes("financial_data", df.columns[:2])  # Sample indexing
    print("\n Phase 4: Data Structure Implementation:")
    print("\n📦 Aggregated Sample Data:")
    # Dynamically find a usable numeric and string column for aggregation
    numeric_cols = [
        col for col in df.select_dtypes(include='number').columns
        if "Date" not in col and "Time" not in col
    ]
    string_cols = df.select_dtypes(include='object').columns.tolist()

    if numeric_cols and string_cols:
        group_col = string_cols[0]
        measure_col = numeric_cols[0]

        print(f"\n Sample Data (Grouped by '{group_col}', Measuring '{measure_col}'):")
        result = storage.aggregate_data("financial_data", group_by=group_col, measures=measure_col)
        print(result.head(10))  # Show top 10 rows
    else:
        print("\n📦 Aggregated Sample Data: No valid numeric and string columns found for aggregation.")


if __name__ == "__main__":
    main()
