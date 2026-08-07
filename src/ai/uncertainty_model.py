"""
uncertainty_model.py
--------------------------------
Estimates prediction uncertainty using the
Random Forest ensemble.

Author: Sirama Avinash
"""

import numpy as np
import pandas as pd


class UncertaintyModel:

    def __init__(self):

        print("Uncertainty Model initialized.")


    def estimate_uncertainty(self, model, X_test):

        print("\n========== UNCERTAINTY ESTIMATION ==========\n")


        # ----------------------------------
        # Convert DataFrame to NumPy array
        # ----------------------------------

        X_numpy = X_test.to_numpy()



        # ----------------------------------
        # Prediction from every tree
        # ----------------------------------

        tree_predictions = np.array(

            [
                tree.predict(X_numpy)
                for tree in model.estimators_
            ]

        )


        # Shape:
        # (number_of_trees, number_of_samples)



        # ----------------------------------
        # Mean Prediction
        # ----------------------------------

        mean_prediction = tree_predictions.mean(axis=0)



        # ----------------------------------
        # Standard Deviation
        # Tree disagreement = uncertainty
        # ----------------------------------

        uncertainty = tree_predictions.std(axis=0)



        # ----------------------------------
        # Confidence Score
        # Normalize uncertainty
        # ----------------------------------

        max_std = uncertainty.max()


        if max_std == 0:

            confidence = np.ones_like(uncertainty)

        else:

            confidence = 1 - (uncertainty / max_std)



        # Keep values between 0 and 1

        confidence = np.clip(confidence, 0, 1)



        # ----------------------------------
        # Confidence Category
        # ----------------------------------

        confidence_level = np.where(

            confidence >= 0.90,

            "High",

            np.where(

                confidence >= 0.60,

                "Medium",

                "Low"

            )

        )



        # ----------------------------------
        # Create Results DataFrame
        # ----------------------------------

        results = pd.DataFrame({

            "Predicted_Demand": mean_prediction,

            "Prediction_STD": uncertainty,

            "Confidence": confidence,

            "Confidence_Level": confidence_level

        })



        print("Uncertainty estimation completed.")

        print(f"Rows : {len(results)}")


        return results