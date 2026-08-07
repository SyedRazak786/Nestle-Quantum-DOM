"""
preprocessing.py
--------------------------------
Preprocesses the merged Nestlé dataset
for AI, Classical Optimization and Quantum Optimization.

Author: Syed Razak
"""
import numpy as np
import pandas as pd


class DataPreprocessor:

    def __init__(self):

        print("Nestlé Data Preprocessor initialized.")

    def preprocess(self, dataframe):

        print("\n========== PREPROCESSING DATA ==========\n")

        df = dataframe.copy()

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Remove duplicate columns
        df = df.loc[:, ~df.columns.duplicated()]

        print(f"Original Shape : {df.shape}")

        # ----------------------------------
        # Remove unnecessary columns
        # ----------------------------------

        columns_to_drop = [

            # Text / comments
            "Additionalcomments",
            "Comments",

            # Report metadata
            "report_date",
            "Report_Run_Date",
            "Report_Run_Date_y",
            "Modified_Date",
            "SnapshotDate",

            # Duplicate date after merge
            "Date"

        ]

        existing_columns = [
            col for col in columns_to_drop
            if col in df.columns
        ]

        df = df.drop(columns=existing_columns)

        print(f"After Column Cleanup : {df.shape}")

        df = self.feature_engineering(df)
        return df
    
    def feature_engineering(self, dataframe):

        df = dataframe.copy()

        print("Generating engineered features...")

        # ----------------------------------
        # Shipping cost per unit ordered
        # ----------------------------------
        if {
            "Shipping_Cost",
            "OrderedQty_converted"
        }.issubset(df.columns):

            df["Shipping_Cost_Per_Unit"] = (
                df["Shipping_Cost"]
                /
                df["OrderedQty_converted"].replace(0, np.nan)
            ).fillna(0)

        # ----------------------------------
        # Inventory coverage
        # ----------------------------------
        if {
            "Available_inventory",
            "TotalDemand"
        }.issubset(df.columns):

            df["Inventory_Coverage"] = (
                df["Available_inventory"]
                /
                df["TotalDemand"].replace(0, np.nan)
            ).fillna(0)

        # ----------------------------------
        # Stock utilization
        # ----------------------------------
        if {
            "TotalDemand",
            "TotalSupply"
        }.issubset(df.columns):

            df["Stock_Utilization"] = (
                df["TotalDemand"]
                /
                df["TotalSupply"].replace(0, np.nan)
            ).fillna(0)

        # ----------------------------------
        # Cases per order
        # ----------------------------------
        if {
            "util_case_picks",
            "order_count"
        }.issubset(df.columns):

            df["Cases_Per_Order"] = (
                df["util_case_picks"]
                /
                df["order_count"].replace(0, np.nan)
            ).fillna(0)

        # ----------------------------------
        # Dock utilization
        # ----------------------------------
        if {
            "Dock_Booked",
            "Dock_Capacity"
        }.issubset(df.columns):

            df["Dock_Utilization"] = (
                df["Dock_Booked"]
                /
                df["Dock_Capacity"].replace(0, np.nan)
            ).fillna(0)

        print(f"Feature engineering completed: {df.shape}")

        return df