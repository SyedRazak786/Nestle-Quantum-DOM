from src.pipeline.load_dataset import DatasetLoader
from src.ai.feature_engineering import AIFeatureEngineer


loader = DatasetLoader()

df = loader.load_master_dataset()

engineer = AIFeatureEngineer()

# prepare_dataset now returns: df, X, y
df, X, y = engineer.prepare_dataset(
    df,
    target_column="SalesOrderDemand"
)

print("\n========== FEATURE ENGINEERING ==========\n")

print("Processed Dataset Shape :", df.shape)
print("Features Shape :", X.shape)
print("Target Shape :", y.shape)

print("\n========== FEATURES ==========\n")

print(X.head())

print("\n========== TARGET ==========\n")

print(y.head())