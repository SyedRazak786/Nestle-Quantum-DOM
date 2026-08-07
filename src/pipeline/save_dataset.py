"""
save_dataset.py
--------------------------------
Utility for saving datasets.

Author: Sirama Avinash
"""

from pathlib import Path


class DatasetSaver:

    def __init__(self):

        self.output_folder = Path("data/processed")
        self.output_folder.mkdir(parents=True, exist_ok=True)

        print("Dataset Saver initialized.")

    def save(self, dataframe, filename="master_dataset.csv"):

        output_path = self.output_folder / filename

        dataframe.to_csv(
            output_path,
            index=False
        )

        print("\n========== DATASET SAVED ==========\n")

        print(f"Location : {output_path}")
        print(f"Rows     : {dataframe.shape[0]}")
        print(f"Columns  : {dataframe.shape[1]}")

        return output_path