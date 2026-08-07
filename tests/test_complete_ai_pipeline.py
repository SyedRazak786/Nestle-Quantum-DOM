from pathlib import Path

from src.pipeline.load_dataset import DatasetLoader

from src.ai.feature_engineering import AIFeatureEngineer
from src.ai.model_training import AIModelTrainer

from src.evaluation.metrics import ModelEvaluator

from src.ai.uncertainty_model import UncertaintyModel
from src.ai.inventory_prediction import InventoryPredictor
from src.ai.ai_recommendation import AIRecommendation


# -----------------------------
# Load Dataset
# -----------------------------

loader = DatasetLoader()

df = loader.load_master_dataset()


# =====================================================
# TEMPORARY DEBUG
# Check Master Dataset
# =====================================================

print("\n========== CHECK MASTER DATASET ==========\n")

inventory_cols = [
    "LocationID",
    "MaterialID",
    "Available_inventory",
    "SalesOrderDemand"
]

print("Missing values in master dataset:\n")

print(df[inventory_cols].isnull().sum())

missing_master = df[
    df[inventory_cols].isnull().any(axis=1)
]

print("\nRows with missing inventory data:")

print(len(missing_master))

if not missing_master.empty:

    print("\nRows:\n")

    print(
        missing_master[
            inventory_cols
        ].head()
    )


# -----------------------------
# Feature Engineering
# -----------------------------

engineer = AIFeatureEngineer()

clean_df, X, y = engineer.prepare_dataset(
    df,
    target_column="SalesOrderDemand"
)


# -----------------------------
# Train Model
# -----------------------------

trainer = AIModelTrainer()

model, X_train, X_test, y_train, y_test = trainer.train(
    X,
    y
)


# -----------------------------
# Model Evaluation
# -----------------------------

predictions = model.predict(X_test)

evaluator = ModelEvaluator()

metrics = evaluator.evaluate(
    y_test,
    predictions
)


# -----------------------------
# Uncertainty Estimation
# -----------------------------

uncertainty = UncertaintyModel()

uncertainty_results = uncertainty.estimate_uncertainty(
    model,
    X_test
)


# -----------------------------
# Inventory Prediction
# -----------------------------

inventory = InventoryPredictor()

inventory_results = inventory.predict_inventory(
    clean_df,
    uncertainty_results["Predicted_Demand"]
)


# -----------------------------
# AI Recommendation
# -----------------------------

recommend = AIRecommendation()

final_results = recommend.generate_recommendations(
    inventory_results,
    uncertainty_results
)


# -----------------------------
# Save AI Decision Table
# -----------------------------

output_dir = Path("outputs")

output_dir.mkdir(exist_ok=True)

output_file = output_dir / "ai_decisions.csv"

final_results.to_csv(
    output_file,
    index=False
)

print(f"\nAI decision table saved to: {output_file}")


# -----------------------------
# Verification
# -----------------------------

print("\n========== VERIFICATION ==========\n")

print("Missing Values:")

missing = final_results.isnull().sum()

missing = missing[missing > 0]

if missing.empty:

    print("No missing values found.")

else:

    print(missing)


print("\nConfidence Range:")

print(
    final_results["Confidence"].min(),
    final_results["Confidence"].max()
)


print("\nRecommendation Counts:")

print(
    final_results["Recommendation"].value_counts()
)


print("\nTotal Rows:")

print(len(final_results))


# =====================================================
# TEMPORARY DEBUGGING SECTION
# =====================================================

print("\n========== DEBUGGING MISSING VALUES ==========\n")

missing_rows = final_results[
    final_results.isnull().any(axis=1)
]

if missing_rows.empty:

    print("No rows contain missing values.")

else:

    print(f"Rows with missing values: {len(missing_rows)}")

    print("\nRow Indices:")

    print(missing_rows.index.tolist())

    print("\nMissing Columns Per Row:\n")

    for idx in missing_rows.index:

        cols = final_results.columns[
            final_results.loc[idx].isnull()
        ]

        print(f"Row {idx} -> {list(cols)}")

    print("\nComplete Rows:\n")

    print(missing_rows)


# -----------------------------
# Final Output
# -----------------------------

print("\n========== FINAL AI OUTPUT ==========\n")

print(final_results.head())

print("\nMetrics:")

print(metrics)