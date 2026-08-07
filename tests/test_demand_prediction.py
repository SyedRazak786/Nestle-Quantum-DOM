from src.pipeline.load_dataset import DatasetLoader
from src.ai.feature_engineering import AIFeatureEngineer
from src.ai.model_training import AIModelTrainer
from src.ai.demand_prediction import DemandPredictor


# -------------------------
# Load Dataset
# -------------------------

loader = DatasetLoader()

df = loader.load_master_dataset()

# -------------------------
# Feature Engineering
# -------------------------

engineer = AIFeatureEngineer()

processed_df, X, y = engineer.prepare_dataset(
    df,
    target_column="SalesOrderDemand"
)

# -------------------------
# Train Model
# -------------------------

trainer = AIModelTrainer()

model, X_train, X_test, y_train, y_test = trainer.train(
    X,
    y
)

# -------------------------
# Predict Demand
# -------------------------

predictor = DemandPredictor()

predictions = predictor.predict(
    model,
    X_test
)

# -------------------------
# Results
# -------------------------

print("\n========== PREDICTED DEMAND ==========\n")

print(predictions.head())

print("\nPrediction Shape:")

print(predictions.shape)