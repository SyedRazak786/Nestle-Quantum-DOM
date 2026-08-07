import pandas as pd

from src.analysis.data_summary import DataSummary


summary = DataSummary()

df = pd.DataFrame(
    {
        "Order_ID": [1, 2, 3],
        "Customer": ["Alice", "Bob", "Charlie"],
        "Warehouse": ["WH_A", "WH_B", "WH_C"],
        "Cost": [100, 200, 150],
    }
)

summary.summarize(df)