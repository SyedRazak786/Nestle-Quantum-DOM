"""
qubo_formulation.py
--------------------------------
Phase 4A

Creates binary variables for the
Distributed Order Management (DOM)
QUBO formulation.

Each binary variable represents:

x(order, plant)

= 1 -> Order assigned to Plant
= 0 -> Otherwise

This variable mapping will be reused by:

1. Constraint Builder
2. Objective Function
3. QUBO Builder
4. Quantum Solvers

Author: Sirama Avinash
"""

from pathlib import Path

import pandas as pd


class QUBOFormulation:

    def __init__(self):

        print("QUBO Formulation initialized.")

    def create_binary_variables(
        self,
        dataframe,
        max_orders=50
    ):

        print("\n========== QUBO FORMULATION ==========\n")

        df = dataframe.copy()

        # ----------------------------------
        # Required Columns
        # ----------------------------------

        required = [

            "Plant",
            "Predicted_Demand"

        ]

        missing = [

            c for c in required
            if c not in df.columns

        ]

        if missing:

            raise ValueError(
                f"Missing columns: {missing}"
            )

        # ----------------------------------
        # Small subset
        # ----------------------------------

        df = df.iloc[:max_orders].copy()

        plants = sorted(
            df["Plant"].unique()
        )

        orders = list(df.index)

        # ----------------------------------
        # Create Binary Variables
        # ----------------------------------

        variable_map = {}

        variable_list = []

        variable_index = 0

        for order in orders:

            original_plant = df.loc[order, "Plant"]

            for plant in plants:

                variable_name = f"x_{order}_{plant}"

                variable_map[(order, plant)] = variable_index

                variable_list.append({

                    "Variable_Index": variable_index,

                    "Variable_Name": variable_name,

                    "Order_ID": order,

                    "Original_Plant": original_plant,

                    "Plant": plant

                })

                variable_index += 1

        variable_df = pd.DataFrame(
            variable_list
        )

        # ----------------------------------
        # Debug
        # ----------------------------------

        print(f"Orders              : {len(orders)}")
        print(f"Plants              : {len(plants)}")
        print(f"Binary Variables    : {len(variable_df)}")

        print("\nSample Variables:\n")

        print(variable_df.head())

        # ----------------------------------
        # Save Variable Mapping
        # ----------------------------------

        output_dir = Path("outputs")

        output_dir.mkdir(exist_ok=True)

        output_file = (
            output_dir /
            "qubo_variables.csv"
        )

        variable_df.to_csv(
            output_file,
            index=False
        )

        print(
            f"\nVariable mapping saved to:\n{output_file}"
        )

        return {

            "orders": orders,

            "plants": plants,

            "variable_map": variable_map,

            "variable_dataframe": variable_df

        }