"""
ai_recommendation.py
--------------------------------
Generates business recommendations
using demand prediction, inventory,
and confidence information.

Author: Sirama Avinash
"""

import pandas as pd


class AIRecommendation:

    def __init__(self):

        print("AI Recommendation initialized.")

    def generate_recommendations(
        self,
        inventory_results,
        uncertainty_results
    ):

        print("\n========== AI RECOMMENDATION ==========\n")

        # ----------------------------------
        # Merge Confidence Information
        # ----------------------------------

        result = inventory_results.copy().reset_index(drop=True)

        uncertainty_results = uncertainty_results.reset_index(drop=True)

        result["Confidence"] = uncertainty_results["Confidence"]
        result["Confidence_Level"] = uncertainty_results["Confidence_Level"]

        recommendations = []

        # ----------------------------------
        # Business Rules
        # ----------------------------------

        for _, row in result.iterrows():

            confidence = row["Confidence"]
            gap = row["Inventory_Gap"]
            demand = row["Predicted_Demand"]

            # Rule 1
            if confidence < 0.60:

                recommendation = "Planner Review"

            # Rule 2
            elif gap > 0:

                recommendation = "Replenish Stock"

            # Rule 3
            elif demand >= 0.70:

                recommendation = "Transfer Stock"

            # Rule 4
            else:

                recommendation = "Maintain Inventory"

            recommendations.append(recommendation)

        result["Recommendation"] = recommendations

        print("Recommendation generation completed.")
        print(f"Rows : {len(result)}")

        return result