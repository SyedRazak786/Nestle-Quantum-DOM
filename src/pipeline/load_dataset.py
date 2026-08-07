"""
load_dataset.py
-------------------------------
Loads the processed master dataset.

Author: Sirama Avinash
"""

import pandas as pd


class DatasetLoader:

    def __init__(self):

        print("Dataset Loader initialized.")

    def load_master_dataset(
        self,
        file_path="data/processed/master_dataset.csv"
    ):

        print("\n========== LOADING MASTER DATASET ==========\n")

        df = pd.read_csv(file_path)

        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        return df