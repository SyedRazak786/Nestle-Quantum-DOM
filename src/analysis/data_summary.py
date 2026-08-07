"""
data_summary.py
----------------------------------
Provides a quick summary of the dataset.
"""

import pandas as pd


class DataSummary:

    def __init__(self):
        print("Data Summary initialized.")

    def summarize(self, df: pd.DataFrame):

        print("\n========== DATASET SUMMARY ==========")

        print(f"\nRows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        print("\nColumn Names:")
        for col in df.columns:
            print(f" - {col}")

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\nDescriptive Statistics:")
        print(df.describe(include="all"))

        print("\n========== END SUMMARY ==========")

        return {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "missing": df.isnull().sum().to_dict(),
            "duplicates": int(df.duplicated().sum())
        }