from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner
from src.data.validator import DataValidator
from src.data.merger import DataMerger
from src.data.preprocessing import DataPreprocessor

print("\n========== DATA PIPELINE TEST ==========\n")

# ---------------------------------
# Load datasets
# ---------------------------------

loader = DataLoader()
datasets = loader.load_all_datasets()

# ---------------------------------
# Initialize modules
# ---------------------------------

cleaner = DataCleaner()
validator = DataValidator()
merger = DataMerger()
preprocessor = DataPreprocessor()

# ---------------------------------
# Clean datasets
# ---------------------------------

orders = cleaner.clean_dataset(
    datasets["orders"],
    date_columns=["transportationplanningdate", "RequestedDeliveryDate"]
)

shipping = cleaner.clean_dataset(
    datasets["shipping_cost"]
)

capacity = cleaner.clean_dataset(
    datasets["capacity_planning"],
    date_columns=["DATE"]
)

throughput = cleaner.clean_dataset(
    datasets["throughput_capacity"],
    date_columns=["transportationplanningdate"]
)

dock = cleaner.clean_dataset(
    datasets["dock_capacity"],
    date_columns=["Date"]
)

datasets = {
    "orders": orders,
    "shipping_cost": shipping,
    "capacity_planning": capacity,
    "throughput_capacity": throughput,
    "dock_capacity": dock
}

# ---------------------------------
# Validate
# ---------------------------------

validator.validate_all(datasets)

# ---------------------------------
# Merge
# ---------------------------------

merged = merger.merge_orders_shipping(
    orders,
    shipping
)

merged = merger.merge_capacity(
    merged,
    capacity
)

merged = merger.merge_throughput(
    merged,
    throughput
)

merged = merger.merge_dock(
    merged,
    dock
)

# ---------------------------------
# Preprocess
# ---------------------------------

processed = preprocessor.preprocess(
    merged
)

print("\n========== FINAL DATASET ==========\n")

print(processed.head())

print("\nShape :", processed.shape)

print("\n========== DATA PIPELINE PASSED ==========\n")