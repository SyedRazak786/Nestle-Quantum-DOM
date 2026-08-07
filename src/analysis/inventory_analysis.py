"""
inventory_analysis.py
----------------------------------
Analyze warehouse inventory.
"""

import pandas as pd


class InventoryAnalysis:

    def __init__(self):
        print("Inventory Analysis initialized.")

    def analyze(self, df: pd.DataFrame):

        print("\n========== INVENTORY ANALYSIS ==========")

        total_inventory = df["Inventory"].sum()
        average_inventory = df["Inventory"].mean()

        warehouse_inventory = (
            df.groupby("Warehouse")["Inventory"]
            .sum()
            .sort_values(ascending=False)
        )

        print(f"Total Inventory   : {total_inventory}")
        print(f"Average Inventory : {average_inventory:.2f}")

        print("\nInventory Per Warehouse:")
        print(warehouse_inventory)

        print("\nHighest Inventory Warehouse:")
        print(warehouse_inventory.idxmax())

        print("\nLowest Inventory Warehouse:")
        print(warehouse_inventory.idxmin())

        return {
            "total_inventory": total_inventory,
            "average_inventory": average_inventory,
            "warehouse_inventory": warehouse_inventory.to_dict()
        }