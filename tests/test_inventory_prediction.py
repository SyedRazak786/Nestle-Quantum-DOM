from src.pipeline.load_dataset import DatasetLoader
from src.ai.feature_engineering import AIFeatureEngineer
from src.ai.model_training import AIModelTrainer
from src.ai.demand_prediction import DemandPredictor
from src.ai.inventory_prediction import InventoryPredictor

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
# Inventory Prediction
# -------------------------

inventory = InventoryPredictor()

inventory_df = inventory.predict_inventory(
    df.iloc[X_test.index],
    predictions
)

print("\n========== INVENTORY RESULTS ==========\n")

print(
    inventory_df[
        [
            "Available_inventory",
            "Predicted_Demand",
            "Required_Inventory",
            "Inventory_Gap",
            "Replenishment_Required",
            "Inventory_Status"
        ]
    ].head()
)

print("\nFinal Shape:")

print(inventory_df.shape)