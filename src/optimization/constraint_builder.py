"""
constraint_builder.py
--------------------------------
Builds QUBO constraints for
Distributed Order Management.

Phase 4B

Constraints:

1. Every order assigned exactly once.

Author: Sirama Avinash
"""

from pathlib import Path

import pandas as pd


class ConstraintBuilder:

    def __init__(self):

        print("Constraint Builder initialized.")

    def build_constraints(
        self,
        variable_mapping
    ):

        print("\n========== BUILDING CONSTRAINTS ==========\n")

        df = variable_mapping.copy()

        required = [

            "Variable_Index",
            "Variable_Name",
            "Order_ID",
            "Plant"

        ]

        missing = [

            c for c in required
            if c not in df.columns

        ]

        if missing:

            raise ValueError(
                f"Missing columns: {missing}"
            )

        constraints = []

        # ----------------------------------
        # One assignment constraint
        # for every order
        # ----------------------------------

        for order in sorted(df["Order_ID"].unique()):

            order_df = (

                df[
                    df["Order_ID"] == order
                ]

                .sort_values("Plant")

            )

            variables = list(
                order_df["Variable_Name"]
            )

            equation = (

                " + ".join(variables)

                + " = 1"

            )

            constraints.append({

                "Order_ID": order,

                "Constraint_Type":
                    "Assignment",

                "Variables":
                    ", ".join(variables),

                "Equation":
                    equation

            })

        constraints_df = pd.DataFrame(
            constraints
        )

        print(
            "Orders :",
            constraints_df.shape[0]
        )

        print(
            "Constraints Built :",
            len(constraints_df)
        )

        print("\nSample Constraints:\n")

        print(
            constraints_df.head()
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
            "qubo_constraints.csv"

        )

        constraints_df.to_csv(

            output_file,

            index=False

        )

        print(

            f"\nConstraint file saved to:\n{output_file}"

        )

        return constraints_df