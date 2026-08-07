"""
solution_decoder.py
--------------------------------
Phase 4H

Decodes the binary QAOA solution into
business-readable order assignments.

Author: Sirama Avinash
"""

from pathlib import Path

import pandas as pd


class SolutionDecoder:

    def __init__(self):

        print("Solution Decoder initialized.")

    def decode(
        self,
        variable_mapping,
        qaoa_result
    ):

        print("\n========== DECODING QUANTUM SOLUTION ==========\n")

        solution = list(qaoa_result.x)

        mapping = variable_mapping.copy()

        mapping["Selected"] = solution

        assignments = mapping[
            mapping["Selected"] == 1
        ].copy()

        # ---------------------------------
        # Reassignment Status
        # ---------------------------------

        assignments["Status"] = assignments.apply(
            lambda row:
                "Reassigned"
                if row["Original_Plant"] != row["Plant"]
                else "Assigned",
            axis=1
        )

        assignments.rename(
            columns={
                "Plant": "Assigned_Plant"
            },
            inplace=True
        )

        
        assignments["Plant_Changed"] = (
            assignments["Original_Plant"]
            !=
            assignments["Assigned_Plant"]
        ).astype(int)

        assignments = assignments[
            [
                "Order_ID",
                "Original_Plant",
                "Assigned_Plant",
                "Status",
                "Plant_Changed",
                "Variable_Name"
            ]
        ]
        

        assignments.reset_index(
            drop=True,
            inplace=True
        )
        # ---------------------------------
        # Business Metrics
        # ---------------------------------

        reassigned_orders = assignments[
            assignments["Plant_Changed"] == 1
        ]

        unchanged_orders = assignments[
            assignments["Plant_Changed"] == 0
        ]

        print("\n========== BUSINESS METRICS ==========\n")

        print(f"Total Orders       : {len(assignments)}")
        print(f"Reassigned Orders  : {len(reassigned_orders)}")
        print(f"Unchanged Orders   : {len(unchanged_orders)}")

        if len(assignments) > 0:
            print(
                f"Reassignment Rate  : "
                f"{100 * len(reassigned_orders) / len(assignments):.2f}%"
            )

        print(assignments)

        return assignments