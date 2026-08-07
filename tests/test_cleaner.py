from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner



loader = DataLoader()

datasets = loader.load_all_datasets()



cleaner = DataCleaner()



orders = cleaner.clean_dataset(

    datasets["orders"]

)


capacity = cleaner.clean_dataset(

    datasets["capacity_planning"],

    ["DATE"]

)


print("\nOrders after cleaning:")
print(orders.shape)


print("\nCapacity after cleaning:")
print(capacity.shape)