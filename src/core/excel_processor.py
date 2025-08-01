import pandas as pd

class ExcelProcessor:
    def __init__(self):
        self.files_data = {}

    def load_files(self, file_paths):
        for path in file_paths:
            xls = pd.read_excel(path, sheet_name=None, engine='openpyxl')
            self.files_data[path] = xls

    def get_sheet_info(self):
        info = {}
        for file, sheets in self.files_data.items():
            info[file] = {}
            for sheet_name, df in sheets.items():
                info[file][sheet_name] = {
                    'rows': df.shape[0],
                    'columns': df.shape[1],
                    'column_names': df.columns.tolist()
                }
        return info

    def extract_data(self, file_path, sheet_name):
        return self.files_data[file_path][sheet_name]

    def preview_data(self, file_path, sheet_name, rows=5):
        return self.files_data[file_path][sheet_name].head(rows)
