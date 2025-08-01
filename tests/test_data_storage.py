import pandas as pd
from src.core.data_storage import DataStorage


def test_store_and_query():
    storage = DataStorage()
    df = pd.DataFrame({
        "Customer": ["Alice", "Bob", "Alice", "Charlie"],
        "Amount": [100, 200, 150, 300]
    })

    storage.store_data(df, "test_table")
    storage.create_indexes("test_table", ["Customer"])

    result = storage.query_by_criteria("SELECT * FROM test_table WHERE Customer = 'Alice'")
    assert len(result) == 2

    agg = storage.aggregate_data("test_table", group_by="Customer", measures="Amount")

    # Flatten multi-index for checking
    flat_columns = ["_".join(col) if isinstance(col, tuple) else col for col in agg.columns]
    assert any("sum" in col for col in flat_columns)
    assert any("mean" in col for col in flat_columns)
    assert any("count" in col for col in flat_columns)

