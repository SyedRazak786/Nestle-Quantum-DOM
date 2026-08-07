"""
objective_function.py
--------------------------------
Phase 4C

Builds the business objective
for the QUBO formulation.

Business Objective

=

Transportation Cost

+

Reassignment Penalty

+

Inventory Risk

+

Capacity Risk

Author: Sirama Avinash
"""

from pathlib import Path

import pandas as pd

from src.classical.cost_matrix import CostMatrix


class ObjectiveFunction:

    def __init__(self):

        print("Objective Function initialized.")

    def build_objective(
        self,
        dataframe,
        variable_mapping
    ):

        print("\n========== BUILDING OBJECTIVE FUNCTION ==========\n")

        df = dataframe.copy()

        variables = variable_mapping.copy()

        # ----------------------------------
        # Build Transportation Cost Matrix
        # ----------------------------------

        cost_builder = CostMatrix()

        cost_matrix = cost_builder.build_cost_matrix(df)

        # ----------------------------------
        # Temporary Risks
        # ----------------------------------

        inventory_risk = {}

        capacity_risk = {}

        plants = sorted(df["Plant"].unique())

        for plant in plants:

            inventory_risk[plant] = 0

            capacity_risk[plant] = 0

        reassignment_penalty = 5

        objective_rows = []

        # ----------------------------------
        # Cost of every binary variable
        # ----------------------------------

        for _, row in variables.iterrows():

            variable_index = row["Variable_Index"]
            order = row["Order_ID"]

            plant = row["Plant"]

            variable = row["Variable_Name"]

            original = df.loc[order, "Plant"]

            transport_cost = cost_matrix.loc[
                original,
                plant
            ]

            reassign = (

                reassignment_penalty

                if plant != original

                else 0

            )

            inventory = inventory_risk[plant]

            capacity = capacity_risk[plant]

            total_cost = (

                transport_cost
                + reassign
                + inventory
                + capacity

            )

            objective_rows.append({

                "Variable_Index": row["Variable_Index"],

                "Variable_Name": variable,

                "Order_ID": order,

                "Assigned_Plant": plant,

                "Transportation_Cost": transport_cost,

                "Reassignment_Penalty": reassign,

                "Inventory_Risk": inventory,

                "Capacity_Risk": capacity,

                "Business_Cost": total_cost

            })

        objective_df = pd.DataFrame(
            objective_rows
        )

        print(
            "Variables :",
            len(objective_df)
        )

        print("\nSample Objective Terms:\n")

        print(
            objective_df.head()
        )

        # ----------------------------------
        # Save
        # ----------------------------------

        output_dir = Path("outputs")

        output_dir.mkdir(
            exist_ok=True
        )

        output_file = (

            output_dir /
            "qubo_objective.csv"

        )

        objective_df.to_csv(

            output_file,

            index=False

        )

        print(
            f"\nObjective saved to:\n{output_file}"
        )

        return objective_df