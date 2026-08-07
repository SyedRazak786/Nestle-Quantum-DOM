from src.pipeline.load_dataset import DatasetLoader
from src.ai.feature_engineering import AIFeatureEngineer
from src.ai.model_training import AIModelTrainer
from src.ai.demand_prediction import DemandPredictor
from src.evaluation.metrics import ModelEvaluator

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
# Predict
# -------------------------

predictor = DemandPredictor()

predictions = predictor.predict(
    model,
    X_test
)

# -------------------------
# Evaluate
# -------------------------

evaluator = ModelEvaluator()

results = evaluator.evaluate(
    y_test,
    predictions
)

print("\n========== RESULTS ==========\n")

for metric, value in results.items():

    print(f"{metric:5} : {value:.6f}")