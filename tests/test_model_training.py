from src.pipeline.load_dataset import DatasetLoader
from src.ai.feature_engineering import AIFeatureEngineer
from src.ai.model_training import AIModelTrainer

# -------------------------
# Load Dataset
# -------------------------

loader = DatasetLoader()

df = loader.load_master_dataset()

# -------------------------
# AI Feature Engineering
# -------------------------

engineer = AIFeatureEngineer()

clean_df, X, y = engineer.prepare_dataset(
    df,
    target_column="SalesOrderDemand"
)

# -------------------------
# Target Validation
# -------------------------

print("\n========== TARGET VALIDATION ==========\n")

print(f"Target Column : {y.name}")
print(f"Total Samples : {len(y)}")
print(f"NaN Values    : {y.isna().sum()}")

if y.isna().sum() > 0:
    print("\nRows containing NaN values:")
    print(y[y.isna()].head())

# -------------------------
# Train Model
# -------------------------

trainer = AIModelTrainer()

model, X_train, X_test, y_train, y_test = trainer.train(
    X,
    y
)

# -------------------------
# Results
# -------------------------

print("\n========== TRAINING COMPLETED ==========\n")

print("Training Shape :", X_train.shape)
print("Testing Shape  :", X_test.shape)

print("\nModel Type:")
print(type(model).__name__)