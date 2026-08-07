from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner
from src.data.merger import DataMerger
from src.data.preprocessing import DataPreprocessor


# ----------------------------
# Load datasets
# ----------------------------

loader = DataLoader()
datasets = loader.load_all_datasets()

cleaner = DataCleaner()

orders = cleaner.clean_dataset(
    datasets["orders"],
    [
        "RequestedDeliveryDate",
        "transportationplanningdate"
    ]
)

shipping = cleaner.clean_dataset(
    datasets["shipping_cost"]
)

capacity = cleaner.clean_dataset(
    datasets["capacity_planning"],
    [
        "DATE",
        "report_date"
    ]
)

throughput = cleaner.clean_dataset(
    datasets["throughput_capacity"],
    [
        "transportationplanningdate",
        "Report_Run_Date"
    ]
)

dock = cleaner.clean_dataset(
    datasets["dock_capacity"],
    [
        "Date",
        "Modified_Date",
        "SnapshotDate",
        "Report_Run_Date"
    ]
)

# ----------------------------
# Merge datasets
# ----------------------------

merger = DataMerger()

result = merger.merge_orders_shipping(
    orders,
    shipping
)

result = merger.merge_capacity(
    result,
    capacity
)

result = merger.merge_throughput(
    result,
    throughput
)

result = merger.merge_dock(
    result,
    dock
)

# ----------------------------
# Preprocess
# ----------------------------

preprocessor = DataPreprocessor()

processed = preprocessor.preprocess(result)

# ----------------------------
# Display Results
# ----------------------------

print("\n========== PREPROCESSED DATA ==========\n")
print(processed.head())

print("\nFinal Shape:")
print(processed.shape)

# ----------------------------
# Display All Columns
# ----------------------------

print("\n========== ALL COLUMNS ==========\n")
print(processed.columns.tolist())

# ----------------------------
# Display Engineered Features
# ----------------------------

print("\n========== ENGINEERED FEATURES ==========\n")

features = [
    "Shipping_Cost_Per_Unit",
    "Inventory_Coverage",
    "Stock_Utilization",
    "Cases_Per_Order",
    "Dock_Utilization"
]

# Check which engineered features exist
existing_features = [
    feature for feature in features
    if feature in processed.columns
]

missing_features = [
    feature for feature in features
    if feature not in processed.columns
]

print("Existing Features:")
print(existing_features)

print("\nMissing Features:")
print(missing_features)

if existing_features:
    print("\nFeature Values:")
    print(processed[existing_features].head())