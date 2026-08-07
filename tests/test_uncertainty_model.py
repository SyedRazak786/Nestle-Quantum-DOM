from src.pipeline.load_dataset import DatasetLoader
from src.ai.feature_engineering import AIFeatureEngineer
from src.ai.model_training import AIModelTrainer
from src.ai.uncertainty_model import UncertaintyModel

# ----------------------------------
# Load Dataset
# ----------------------------------

loader = DatasetLoader()

df = loader.load_master_dataset()

# ----------------------------------
# Feature Engineering
# ----------------------------------

engineer = AIFeatureEngineer()

clean_df, X, y = engineer.prepare_dataset(
    df,
    target_column="SalesOrderDemand"
)

# ----------------------------------
# Train Model
# ----------------------------------

trainer = AIModelTrainer()

model, X_train, X_test, y_train, y_test = trainer.train(
    X,
    y
)

# ----------------------------------
# Uncertainty
# ----------------------------------

uncertainty = UncertaintyModel()

results = uncertainty.estimate_uncertainty(
    model,
    X_test
)

print("\n========== UNCERTAINTY RESULTS ==========\n")

print(results.head())

print("\nShape:")

print(results.shape)