from src.core.format_parser import FormatParser
from datetime import datetime, timedelta


def test_parse_amount():
    parser = FormatParser()

    assert parser.parse_amount("$1,234.56") == 1234.56
    assert parser.parse_amount("(2,500.00)") == -2500.0
    assert parser.parse_amount("1.5M") == 1500000.0
    assert parser.parse_amount("₹1,23,456") == 123456.0


def parse_date(self, value, detected_format=None):
    try:
        # Handle Excel serial dates
        if isinstance(value, (int, float)) or str(value).isdigit():
            serial = int(value)
            if 30000 < serial < 60000:  # Rough range for Excel dates
                return datetime(1899, 12, 30) + timedelta(days=serial)

        # Try known formats
        known_formats = [
            "%m/%d/%Y", "%d/%m/%Y", "%Y-%m-%d", "%d-%b-%Y", "%b %Y", "%B %Y"
        ]
        for fmt in known_formats:
            try:
                return datetime.strptime(value, fmt)
            except:
                continue

    except:
        pass

    return None
