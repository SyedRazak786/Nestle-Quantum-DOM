"""
order_analysis.py
----------------------------------
Analyze customer orders.
"""

import pandas as pd


class OrderAnalysis:

    def __init__(self):
        print("Order Analysis initialized.")

    def analyze(self, df: pd.DataFrame):

        print("\n========== ORDER ANALYSIS ==========")

        total_orders = len(df)
        unique_customers = df["Customer"].nunique()
        unique_warehouses = df["Warehouse"].nunique()

        print(f"Total Orders        : {total_orders}")
        print(f"Unique Customers    : {unique_customers}")
        print(f"Unique Warehouses   : {unique_warehouses}")

        print("\nOrders Per Warehouse:")

        warehouse_orders = df["Warehouse"].value_counts()

        print(warehouse_orders)

        print("\nWarehouse with Maximum Orders:")

        print(warehouse_orders.idxmax())

        return {
            "total_orders": total_orders,
            "unique_customers": unique_customers,
            "unique_warehouses": unique_warehouses,
            "warehouse_orders": warehouse_orders.to_dict()
        }