"""
scaler.py
--------------------------------
Scales numerical features of the merged
Nestlé dataset for AI, Classical Optimization
and Quantum Optimization.

Author: Sirama Avinash
"""

from sklearn.preprocessing import MinMaxScaler


class DataScaler:

    def __init__(self):

        print("Nestlé Data Scaler initialized.")

        self.scaler = MinMaxScaler()

    def scale(self, dataframe):

        print("\n========== FEATURE SCALING ==========\n")

        df = dataframe.copy()

        # ----------------------------
        # Columns to Scale
        # ----------------------------

        columns_to_scale = [

            # Shipping
            "Shipping_Cost",
            "Shipping_Cost_Per_Unit",
            "Distance",

            # Order
            "OrderedQty_converted",
            "OrderedWeight",
            "OrderedVolume",
            "CalculatedFootprints",

            # Inventory
            "OpeningStock_x",
            "OpeningStock_y",
            "ClosingStock",
            "Available_inventory",
            "TotalSupply",
            "TotalDemand",
            "SalesOrderDemand",

            # Engineered Features
            "Inventory_Coverage",
            "Stock_Utilization",
            "Cases_Per_Order",

            # Throughput
            "util_case_picks",
            "util_pallets",
            "order_count",

            # Dock
            "Dock_Capacity",
            "Dock_Booked",
            "Dock_Remaining",
            "Dock_Utilization"
        ]

        # ----------------------------
        # Scale only existing columns
        # ----------------------------

        existing_columns = [
            col for col in columns_to_scale
            if col in df.columns
        ]

        print(f"Columns Selected : {len(existing_columns)}")
        print(existing_columns)

        if existing_columns:

            df[existing_columns] = self.scaler.fit_transform(
                df[existing_columns]
            )

        print("\nScaling completed successfully.")
        print(f"Dataset Shape : {df.shape}")

        return df