from src.data.loader import DataLoader


loader = DataLoader()

datasets = loader.load_all_datasets()

print("\n========== DATASETS ==========\n")

for name, df in datasets.items():

    print(name)

    print(df.head())

    print("-" * 60)