"""
metrics.py
--------------------------------
Evaluates AI regression models.

Responsibilities
----------------
1. Calculate MAE
2. Calculate RMSE
3. Calculate R² Score

Author: Sirama Avinash
"""

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import numpy as np


class ModelEvaluator:

    def __init__(self):

        print("Model Evaluator initialized.")

    def evaluate(self, y_true, y_pred):

        print("\n========== MODEL EVALUATION ==========\n")

        mae = mean_absolute_error(y_true, y_pred)

        rmse = np.sqrt(
            mean_squared_error(y_true, y_pred)
        )

        r2 = r2_score(
            y_true,
            y_pred
        )

        print(f"MAE  : {mae:.6f}")
        print(f"RMSE : {rmse:.6f}")
        print(f"R²   : {r2:.6f}")

        return {
            "MAE": mae,
            "RMSE": rmse,
            "R2": r2
        }