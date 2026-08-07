"""
Test the real Nestlé datasets.
"""

from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw")

files = [
    "input_capacity_planning.csv",
    "input_dock_capacity.csv",
    "input_order_data.csv",
    "input_shipping_cost_data.csv",
    "input_throughput_capacity.csv",
]

print("\n========== REAL DATASET INSPECTION ==========\n")

for file in files:

    print("=" * 60)
    print(file)

    df = pd.read_csv(RAW_PATH / file)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names:")

    for col in df.columns:
        print(" -", col)

    print("\nMissing Values:")

    print(df.isnull().sum())

    print("\nData Types:")

    print(df.dtypes)

    print("=" * 60)