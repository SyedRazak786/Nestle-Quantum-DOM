"""
default_assignment.py
--------------------------------
Creates the baseline order assignment.

Responsibilities
----------------
1. Keep the original plant assignment
2. Create baseline assignment
3. Add assignment information
4. Return assignment table

Author: Sirama Avinash
"""

import pandas as pd


class DefaultAssignment:

    def __init__(self):

        print("Default Assignment initialized.")

    def assign_orders(self, dataframe):

        print("\n========== DEFAULT ASSIGNMENT ==========\n")

        df = dataframe.copy()

        # ----------------------------------
        # Check required column
        # ----------------------------------

        if "Plant" not in df.columns:

            raise ValueError(
                "Plant column not found."
            )

        # ----------------------------------
        # Keep original assignment
        # ----------------------------------

        df["Assigned_Plant"] = df["Plant"]

        # ----------------------------------
        # Assignment Type
        # ----------------------------------

        df["Assignment_Type"] = "Default"

        # ----------------------------------
        # Assignment Status
        # ----------------------------------

        df["Assignment_Status"] = "Assigned"

        # ----------------------------------
        # Baseline Cost
        # Placeholder value
        # (Will be replaced later with
        # shipping cost calculations.)
        # ----------------------------------

        df["Assignment_Cost"] = 0.0

        # ----------------------------------
        # Fulfillment Status
        # ----------------------------------

        if "Inventory_Status" in df.columns:

            df["Fulfillment_Status"] = df[
                "Inventory_Status"
            ]

        else:

            df["Fulfillment_Status"] = "Unknown"

        # ----------------------------------
        # Summary
        # ----------------------------------

        print("Default assignment completed.")

        print(f"Orders Assigned : {len(df)}")

        print(
            f"Plants : {df['Assigned_Plant'].nunique()}"
        )

        return df