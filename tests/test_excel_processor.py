import os
from src.core.excel_processor import ExcelProcessor


def test_load_and_preview():
    processor = ExcelProcessor()
    sample_file = os.path.join(os.path.dirname(__file__), "../data/sample/KH_Bank.XLSX")
    sample_file = os.path.abspath(sample_file)
    processor.load_files([sample_file])

    assert sample_file in processor.files_data
    info = processor.get_sheet_info()
    assert isinstance(info, dict)

    # Test preview
    sheet_name = list(info[sample_file].keys())[0]
    preview = processor.preview_data(sample_file, sheet_name, rows=3)
    assert not preview.empty
    assert len(preview) == 3
