"""
loader.py
--------------------------------
Loads all Nestlé raw datasets.

Author: Sirama Avinash
"""

from pathlib import Path
import pandas as pd


class DataLoader:

    def __init__(self):

        self.raw_data_path = Path("data/raw")

        print("Data Loader initialized.")
        print(f"Raw Data Folder : {self.raw_data_path}")

    # ----------------------------------
    # Load all raw datasets
    # ----------------------------------

    def load_all_datasets(self):

        print("\n========== LOADING NESTLÉ DATASETS ==========\n")

        datasets = {

            "capacity_planning":
                "input_capacity_planning.csv",

            "dock_capacity":
                "input_dock_capacity.csv",

            "orders":
                "input_order_data.csv",

            "shipping_cost":
                "input_shipping_cost_data.csv",

            "throughput_capacity":
                "input_throughput_capacity.csv"

        }

        loaded_data = {}

        for name, filename in datasets.items():

            file_path = self.raw_data_path / filename

            print(f"Loading {filename}...")

            df = pd.read_csv(file_path)

            loaded_data[name] = df

            print(
                f"Loaded {name} : "
                f"{df.shape[0]} rows × {df.shape[1]} columns"
            )

        print("\nAll datasets loaded successfully.\n")

        return loaded_data


# =====================================================
# Backward Compatibility
# Older tests import DatasetLoader
# =====================================================

class DatasetLoader(DataLoader):

    def __init__(self):
        super().__init__()

    def load_master_dataset(self):
        """
        Loads the processed master dataset.
        """
        master_path = Path("data/processed/master_dataset.csv")

        print("\n========== LOADING MASTER DATASET ==========\n")

        df = pd.read_csv(master_path)
        print(df.columns)

        print(f"Rows    : {len(df)}")
        print(f"Columns : {len(df.columns)}")

        return df