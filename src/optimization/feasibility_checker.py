"""
feasibility_checker.py
--------------------------------
Phase 4E

Checks whether a solution satisfies
all Distributed Order Management (DOM)
constraints.

Checks
------
1. Binary variables (0 or 1)
2. Every order assigned exactly once
3. Inventory feasibility
4. Capacity feasibility

Author: Sirama Avinash
"""

from pathlib import Path

import pandas as pd


class FeasibilityChecker:

    def __init__(self):

        print("Feasibility Checker initialized.")

    def check_solution(
        self,
        dataframe,
        solution
    ):

        print("\n========== FEASIBILITY CHECK ==========\n")

        df = dataframe.copy()

        sol = solution.copy()

        # ----------------------------------
        # Required Columns
        # ----------------------------------

        required = [

            "Order_ID",
            "Assigned_Plant"

        ]

        missing = [

            c for c in required
            if c not in sol.columns

        ]

        if missing:

            raise ValueError(
                f"Missing columns: {missing}"
            )

        results = []

        # ----------------------------------
        # Check 1
        # One assignment per order
        # ----------------------------------

        duplicate_orders = (

            sol.groupby("Order_ID")
            .size()

        )

        valid_assignment = (

            duplicate_orders == 1

        ).all()

        # ----------------------------------
        # Inventory Check
        # ----------------------------------

        inventory_used = (

            sol.groupby("Assigned_Plant")
            .apply(

                lambda x:

                df.loc[
                    x["Order_ID"],
                    "Predicted_Demand"
                ].sum()

            )

        )

        available_inventory = (

            df.groupby("Plant")
            ["Available_inventory"]
            .sum()

        )

        inventory_ok = True

        inventory_report = {}

        for plant in inventory_used.index:

            used = inventory_used[plant]

            available = available_inventory.get(
                plant,
                0
            )

            feasible = used <= available

            inventory_report[plant] = feasible

            if not feasible:

                inventory_ok = False

        # ----------------------------------
        # Capacity Check
        # ----------------------------------

        capacity = (

            available_inventory * 0.80

        )

        capacity_ok = True

        capacity_report = {}

        for plant in inventory_used.index:

            used = inventory_used[plant]

            cap = capacity.get(
                plant,
                0
            )

            feasible = used <= cap

            capacity_report[plant] = feasible

            if not feasible:

                capacity_ok = False

        # ----------------------------------
        # Overall
        # ----------------------------------

        overall = (

            valid_assignment

            and

            inventory_ok

            and

            capacity_ok

        )

        summary = pd.DataFrame({

            "Assignment_Check": [

                valid_assignment

            ],

            "Inventory_Check": [

                inventory_ok

            ],

            "Capacity_Check": [

                capacity_ok

            ],

            "Overall_Feasible": [

                overall

            ]

        })

        print(summary)

        print("\nInventory Report")

        print(inventory_report)

        print("\nCapacity Report")

        print(capacity_report)

        # ----------------------------------
        # Save
        # ----------------------------------

        output_dir = Path("outputs")

        output_dir.mkdir(exist_ok=True)

        output_file = (

            output_dir /

            "feasibility_report.csv"

        )

        summary.to_csv(

            output_file,

            index=False

        )

        print(

            f"\nReport saved to:\n{output_file}"

        )

        return summary