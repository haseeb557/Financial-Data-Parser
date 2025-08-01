import pandas as pd
from src.core.type_detector import DataTypeDetector

def test_analyze_column_types():
    detector = DataTypeDetector()

    # String
    string_series = pd.Series(["Account A", "Account B", "Account C"])
    assert detector.analyze_column(string_series) == "String"

    # Date
    date_series = pd.Series(["2023-12-31", "2023-01-01", "2023-06-15"])
    assert detector.analyze_column(date_series) == "Date"

    # Number
    number_series = pd.Series(["1000.00", "250.50", "5000"])
    assert detector.analyze_column(number_series) == "Number"
