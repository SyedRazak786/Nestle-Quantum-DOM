import pandas as pd

from src.analysis.business_metrics import BusinessMetrics


metrics = BusinessMetrics()

df = pd.DataFrame(
    {
        "Shipping_Cost": [100, 120, 150],
        "Inventory": [200, 150, 300],
        "Labor_Capacity": [10, 8, 12],
        "Penalty_Cost": [0, 50, 0],
        "Fulfillment_Value": [500, 600, 700],
    }
)

metrics.calculate(df)