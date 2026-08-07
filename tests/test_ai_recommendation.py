from src.pipeline.load_dataset import DatasetLoader
from src.ai.feature_engineering import AIFeatureEngineer
from src.ai.model_training import AIModelTrainer
from src.ai.uncertainty_model import UncertaintyModel
from src.ai.ai_recommendation import AIRecommendation
from src.ai.inventory_prediction import InventoryPredictor


# Load dataset

loader = DatasetLoader()

df = loader.load_master_dataset()



# Feature engineering

engineer = AIFeatureEngineer()

clean_df, X, y = engineer.prepare_dataset(
    df,
    target_column="SalesOrderDemand"
)



# Train model

trainer = AIModelTrainer()

model, X_train, X_test, y_train, y_test = trainer.train(
    X,
    y
)



# Uncertainty

uncertainty = UncertaintyModel()

uncertainty_results = uncertainty.estimate_uncertainty(
    model,
    X_test
)



# Recommendation
# Inventory Prediction

inventory_predictor = InventoryPredictor()

inventory_results = inventory_predictor.predict_inventory(
    clean_df,
    uncertainty_results["Predicted_Demand"]
)


# Recommendation

recommendation = AIRecommendation()

results = recommendation.generate_recommendations(
    inventory_results,
    uncertainty_results
)



print("\n========== FINAL RECOMMENDATIONS ==========\n")

print(results.head())


print("\nShape:")

print(results.shape)