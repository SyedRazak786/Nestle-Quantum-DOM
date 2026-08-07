from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner
from src.data.merger import DataMerger

# ==========================
# Load datasets
# ==========================

loader = DataLoader()
datasets = loader.load_all_datasets()

# ==========================
# Clean datasets
# ==========================

cleaner = DataCleaner()

orders = cleaner.clean_dataset(
    datasets["orders"],
    ["RequestedDeliveryDate", "transportationplanningdate"]
)

shipping = cleaner.clean_dataset(
    datasets["shipping_cost"]
)

capacity = cleaner.clean_dataset(
    datasets["capacity_planning"],
    ["DATE", "report_date"]
)

throughput = cleaner.clean_dataset(
    datasets["throughput_capacity"],
    ["transportationplanningdate", "Report_Run_Date"]
)

dock = cleaner.clean_dataset(
    datasets["dock_capacity"],
    ["Date", "Modified_Date", "SnapshotDate", "Report_Run_Date"]
)

# ==========================
# Merge datasets
# ==========================

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

# ==========================
# Final Output
# ==========================

print("\n========== MERGED DATA PREVIEW ==========\n")

print(result.head())

print("\nFinal Shape:")
print(result.shape)

print("\nTotal Columns:")
print(len(result.columns))

print("\nMerge completed successfully!")