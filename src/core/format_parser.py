import re
import pandas as pd
from datetime import datetime
from dateutil.parser import parse as dateutil_parse
from decimal import Decimal


class FormatParser:
    def __init__(self):
        pass

    def parse_amount(self, value, detected_format=None):
        if pd.isnull(value):
            return None
        value = str(value).strip().replace(',', '')
        multipliers = {'K': 1e3, 'M': 1e6, 'B': 1e9}

        # Abbreviated
        if re.match(r'^[\d\.]+[KMB]$', value):
            return float(value[:-1]) * multipliers[value[-1]]

        # Parentheses negative
        if re.match(r'^\([\d\.]+\)$', value):
            return -float(value.strip('()'))

        # Trailing negative
        if value.endswith('-'):
            return -float(value[:-1])

        # Standard float
        try:
            return float(value.replace('$', '').replace('€', '').replace('₹', ''))
        except:
            return None

    def parse_date(self, value, detected_format=None):
        if isinstance(value, (int, float)) and value > 40000:  # Excel serial
            try:
                return datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(value) - 2)
            except:
                return None

        try:
            return dateutil_parse(str(value), fuzzy=True)
        except:
            return None

    def normalize_currency(self, value):
        return re.sub(r'[^\d\.-]', '', value)

    def handle_special_formats(self, value):
        return str(value).strip()
