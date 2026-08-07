"""
inventory_prediction.py
--------------------------------
Uses predicted demand to estimate
future inventory requirements.

Responsibilities
----------------
1. Estimate required inventory
2. Calculate inventory gap
3. Determine replenishment quantity
4. Preserve business information
5. Prepare optimization-ready inventory data

Author: Sirama Avinash
"""

import pandas as pd
import numpy as np


class InventoryPredictor:

    def __init__(self):

        print("Inventory Predictor initialized.")

    def predict_inventory(
        self,
        dataframe,
        predicted_demand
    ):

        print("\n========== INVENTORY PREDICTION ==========\n")

        # ---------------------------------
        # Copy Dataset
        # ---------------------------------

        df = dataframe.copy().reset_index(drop=True)

        predicted_demand = predicted_demand.reset_index(drop=True)

        # Keep only rows corresponding to predictions
        df = df.iloc[:len(predicted_demand)].copy()

        # ---------------------------------
        # Preserve Business Columns
        # ---------------------------------

        business_columns = [
            "Order_ID",
            "Distribution_Center",
            "Warehouse",
            "Plant",
            "Region"
        ]

        for column in business_columns:

            if column not in df.columns:

                df[column] = "Unknown"

        # ---------------------------------
        # Attach Predicted Demand
        # ---------------------------------

        df["Predicted_Demand"] = predicted_demand

        # ---------------------------------
        # Current Inventory
        # ---------------------------------

        if "Available_inventory" not in df.columns:

            raise ValueError(
                "Available_inventory column not found."
            )

        df["Current_Inventory"] = df["Available_inventory"]

        # ---------------------------------
        # Required Inventory
        # Add 10% safety stock
        # ---------------------------------

        df["Required_Inventory"] = (
            df["Predicted_Demand"] * 1.10
        )

        # ---------------------------------
        # Inventory Gap
        # ---------------------------------

        df["Inventory_Gap"] = (
            df["Required_Inventory"]
            - df["Current_Inventory"]
        )

        # ---------------------------------
        # Replenishment Quantity
        # ---------------------------------

        df["Replenishment_Required"] = np.where(
            df["Inventory_Gap"] > 0,
            df["Inventory_Gap"],
            0
        )

        # ---------------------------------
        # Inventory Status
        # ---------------------------------

        df["Inventory_Status"] = np.where(
            df["Inventory_Gap"] > 0,
            "Replenish",
            "Sufficient"
        )

        print("Inventory prediction completed.")
        print(f"Rows : {len(df)}")

        return df