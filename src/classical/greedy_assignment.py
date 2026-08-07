"""
greedy_assignment.py
--------------------------------
Greedy optimization for Distributed Order
Management (DOM).

The algorithm keeps the original plant if it
has sufficient inventory. Otherwise, it assigns
the order to the plant with the highest
available inventory.

Responsibilities
----------------
1. Read AI decision table
2. Check inventory availability
3. Reassign orders when necessary
4. Save optimized assignments

Author: Sirama Avinash
"""

from pathlib import Path
import pandas as pd


class GreedyAssignment:

    def __init__(self):

        print("Greedy Assignment initialized.")

    def optimize(self, dataframe):

        print("\n========== GREEDY ASSIGNMENT ==========\n")

        df = dataframe.copy()

        # ----------------------------------
        # Required columns
        # ----------------------------------

        required_columns = [

            "Plant",
            "Available_inventory",
            "Predicted_Demand"

        ]

        missing = [

            col for col in required_columns
            if col not in df.columns

        ]

        if missing:

            raise ValueError(
                f"Missing columns: {missing}"
            )

        # ----------------------------------
        # Build inventory lookup
        # ----------------------------------

        plant_inventory = (

            df.groupby("Plant")["Available_inventory"]
              .max()
              .to_dict()

        )

        # ----------------------------------
        # Assignment lists
        # ----------------------------------

        assigned_plants = []

        plant_changed = []

        optimization_status = []

        # ----------------------------------
        # Greedy Optimization
        # ----------------------------------

        for _, row in df.iterrows():

            current_plant = row["Plant"]

            demand = row["Predicted_Demand"]

            current_inventory = row["Available_inventory"]

            # ------------------------------
            # Keep current plant
            # ------------------------------

            if current_inventory >= demand:

                assigned_plants.append(current_plant)

                plant_changed.append("No")

                optimization_status.append("Unchanged")

            # ------------------------------
            # Find better plant
            # ------------------------------

            else:

                best_plant = max(

                    plant_inventory,
                    key=plant_inventory.get

                )

                assigned_plants.append(best_plant)

                if best_plant == current_plant:

                    plant_changed.append("No")

                    optimization_status.append("Unchanged")

                else:

                    plant_changed.append("Yes")

                    optimization_status.append("Optimized")

        # ----------------------------------
        # Add new columns
        # ----------------------------------

        df["Original_Plant"] = df["Plant"]

        df["Assigned_Plant"] = assigned_plants

        df["Assignment_Type"] = "Greedy"

        df["Plant_Changed"] = plant_changed

        df["Optimization_Status"] = optimization_status

        # ----------------------------------
        # Statistics
        # ----------------------------------

        changed_orders = (df["Plant_Changed"] == "Yes").sum()

        print("Greedy optimization completed.")

        print(f"Total Orders      : {len(df)}")

        print(f"Plants            : {df['Plant'].nunique()}")

        print(f"Orders Reassigned : {changed_orders}")

        # ----------------------------------
        # Save Results
        # ----------------------------------

        output_dir = Path("outputs")

        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / "greedy_assignment.csv"

        df.to_csv(

            output_file,
            index=False

        )

        print(f"\nGreedy assignment saved to:\n{output_file}")

        return df