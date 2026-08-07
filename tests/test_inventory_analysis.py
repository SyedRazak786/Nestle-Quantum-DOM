import pandas as pd

from src.analysis.inventory_analysis import InventoryAnalysis


analysis = InventoryAnalysis()

df = pd.DataFrame(
    {
        "Warehouse": [
            "WH_A",
            "WH_A",
            "WH_B",
            "WH_C",
            "WH_C",
        ],
        "Inventory": [
            100,
            150,
            80,
            300,
            120,
        ],
    }
)

analysis.analyze(df)