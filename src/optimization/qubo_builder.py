"""
qubo_builder.py
--------------------------------
Phase 4D

Builds the mathematical QUBO matrix
for Distributed Order Management.

QUBO Objective

Minimize

Business Cost
+
Penalty × (Assignment Constraint)^2

Author: Sirama Avinash
"""

from pathlib import Path

import numpy as np
import pandas as pd


class QUBOBuilder:

    def __init__(self):

        print("QUBO Builder initialized.")

    def build_qubo(
        self,
        variable_mapping,
        objective_df,
        penalty=1000
    ):

        print("\n========== BUILDING QUBO MATRIX ==========\n")

        variables = variable_mapping.copy()

        objective = objective_df.copy()

        n = len(variables)

        Q = np.zeros((n, n))

        # ----------------------------------
        # Add Business Cost
        # ----------------------------------

        for _, row in objective.iterrows():

            idx = int(row["Variable_Index"])

            Q[idx, idx] += row["Business_Cost"]

        # ----------------------------------
        # Assignment Constraints
        #
        # (Σx - 1)^2
        # ----------------------------------

        for order in sorted(variables["Order_ID"].unique()):

            order_vars = variables[
                variables["Order_ID"] == order
            ]["Variable_Index"].tolist()

            # Diagonal terms

            for i in order_vars:

                Q[i, i] += -penalty

            # Off-diagonal terms

            for i in order_vars:

                for j in order_vars:

                    if i < j:

                        Q[i, j] += 2 * penalty

        # ----------------------------------
        # Symmetric Matrix
        # ----------------------------------

        Q = np.triu(Q)

        Q = Q + Q.T - np.diag(np.diag(Q))

        qubo_df = pd.DataFrame(Q)

        print("Variables :", n)

        print("Matrix Shape :", qubo_df.shape)

        print("\nSample Matrix:\n")

        print(qubo_df.iloc[:5, :5])

        # ----------------------------------
        # Save
        # ----------------------------------

        output_dir = Path("outputs")

        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / "qubo_matrix.csv"

        qubo_df.to_csv(
            output_file,
            index=False
        )

        print(
            f"\nQUBO matrix saved to:\n{output_file}"
        )

        return qubo_df