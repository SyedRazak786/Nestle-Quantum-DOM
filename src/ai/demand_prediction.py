"""
demand_prediction.py
--------------------------------
Uses the trained AI model to predict
future customer demand.

Responsibilities
----------------
1. Accept trained model
2. Predict demand
3. Return predictions

Author: Sirama Avinash
"""

import pandas as pd


class DemandPredictor:

    def __init__(self):

        print("Demand Predictor initialized.")

    def predict(self, model, X_test):

        print("\n========== DEMAND PREDICTION ==========\n")

        predictions = model.predict(X_test)

        predictions = pd.Series(
            predictions,
            name="Predicted_Demand"
        )

        print("Prediction completed.")

        print(f"Predictions Generated : {len(predictions)}")

        return predictions