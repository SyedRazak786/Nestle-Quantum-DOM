from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner
from src.data.merger import DataMerger
from src.data.preprocessing import DataPreprocessor
from src.data.scaler import DataScaler

from src.pipeline.save_dataset import DatasetSaver

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
# Scale
# ----------------------------

scaler = DataScaler()

scaled = scaler.scale(processed)

# ----------------------------
# Save Master Dataset
# ----------------------------

saver = DatasetSaver()

saver.save(
    scaled,
    "master_dataset.csv"
)

# ----------------------------
# Results
# ----------------------------

print("\n========== SCALED DATA ==========\n")

print(scaled.head())

print("\nFinal Shape:")
print(scaled.shape)

print("\n========== SCALING VALIDATION ==========\n")

features = [
    "Shipping_Cost",
    "Shipping_Cost_Per_Unit",
    "Inventory_Coverage",
    "Stock_Utilization",
    "Cases_Per_Order",
    "Dock_Utilization"
]

for feature in features:

    if feature in scaled.columns:

        print(
            f"{feature:30}"
            f" Min = {scaled[feature].min():.4f}"
            f"   Max = {scaled[feature].max():.4f}"
        )