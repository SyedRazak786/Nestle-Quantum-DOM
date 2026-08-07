"""
business_metrics.py
----------------------------------
Calculate business KPIs.
"""

import pandas as pd


class BusinessMetrics:

    def __init__(self):
        print("Business Metrics initialized.")

    def calculate(self, df: pd.DataFrame):

        print("\n========== BUSINESS METRICS ==========")

        total_shipping = df["Shipping_Cost"].sum()
        average_shipping = df["Shipping_Cost"].mean()

        total_inventory = df["Inventory"].sum()

        total_labor = df["Labor_Capacity"].sum()

        total_penalty = df["Penalty_Cost"].sum()

        total_value = df["Fulfillment_Value"].sum()

        print(f"Total Shipping Cost     : {total_shipping}")
        print(f"Average Shipping Cost   : {average_shipping:.2f}")
        print(f"Total Inventory         : {total_inventory}")
        print(f"Total Labor Capacity    : {total_labor}")
        print(f"Total Penalty Cost      : {total_penalty}")
        print(f"Total Fulfillment Value : {total_value}")

        return {
            "shipping_cost": total_shipping,
            "average_shipping": average_shipping,
            "inventory": total_inventory,
            "labor": total_labor,
            "penalty": total_penalty,
            "fulfillment": total_value,
        }