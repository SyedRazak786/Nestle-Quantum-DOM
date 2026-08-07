import pandas as pd

from src.analysis.order_analysis import OrderAnalysis


analysis = OrderAnalysis()

df = pd.DataFrame(
    {
        "Order_ID": [1, 2, 3, 4, 5],
        "Customer": ["A", "B", "A", "C", "D"],
        "Warehouse": ["WH_A", "WH_A", "WH_B", "WH_B", "WH_A"],
        "Cost": [100, 200, 150, 250, 120],
    }
)

analysis.analyze(df)