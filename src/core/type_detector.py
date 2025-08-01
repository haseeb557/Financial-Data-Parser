import pandas as pd
import re
from datetime import datetime

class DataTypeDetector:
    def __init__(self):
        pass

    def analyze_column(self, column_data):
        column_data = column_data.dropna().astype(str)
        if column_data.empty:
            return 'Unknown'

        if self.detect_date_format(column_data):
            return 'Date'
        elif self.detect_number_format(column_data):
            return 'Number'
        else:
            return self.classify_string_type(column_data)

    def detect_date_format(self, values):
        date_patterns = [
            r"\d{1,2}/\d{1,2}/\d{4}", r"\d{4}-\d{2}-\d{2}", r"\d{1,2}-[A-Za-z]{3}-\d{2,4}",
            r"Q[1-4]-?\d{2,4}", r"[A-Za-z]{3,9} \d{4}", r"\d{5}"  # Excel serial
        ]
        for v in values:
            for pattern in date_patterns:
                if re.match(pattern, v.strip()):
                    return True
        return False

    def detect_number_format(self, values):
        number_patterns = [
            r"^-?\(?\$?[\d,]+\.\d+\)?$", r"^-?[\d.]+[KMB]?$", r"^-?\(?[\d,]+\)?$", r"[\d,]+-?$"
        ]
        for v in values:
            for pattern in number_patterns:
                if re.match(pattern, v.strip()):
                    return True
        return False

    def classify_string_type(self, values):
        return 'String'
