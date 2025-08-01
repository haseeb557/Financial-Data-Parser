import pandas as pd
import sqlite3
import numpy as np

class DataStorage:
    def __init__(self):
        self.store = {}
        self.conn = sqlite3.connect(":memory:")

    def store_data(self, dataframe, table_name):
        # Convert columns with very large integers to string
        for col in dataframe.columns:
            if pd.api.types.is_integer_dtype(dataframe[col]):
                if dataframe[col].max() > np.iinfo(np.int64).max or dataframe[col].min() < np.iinfo(np.int64).min:
                    dataframe[col] = dataframe[col].astype(str)
            elif pd.api.types.is_object_dtype(dataframe[col]):
                try:
                    # Try converting to int to test for oversized values
                    converted = pd.to_numeric(dataframe[col], errors='coerce')
                    if converted.max() > np.iinfo(np.int64).max:
                        dataframe[col] = dataframe[col].astype(str)
                except:
                    pass

        dataframe.to_sql(table_name, self.conn, if_exists='replace', index=False)
        self.store[table_name] = dataframe

    def create_indexes(self, table_name, columns):
        cursor = self.conn.cursor()
        for col in columns:
            try:
                cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_{table_name}_{col} ON {table_name}({col})")
            except:
                continue
        self.conn.commit()

    def query_by_criteria(self, query):
        return pd.read_sql_query(query, self.conn)

    def aggregate_data(self, table_name, group_by, measures):
        df = self.store[table_name]
        return df.groupby(group_by)[measures].agg(['sum', 'mean', 'count'])
