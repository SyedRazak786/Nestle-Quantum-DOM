"""
linear_programming.py
--------------------------------
Linear Programming optimizer for
Distributed Order Management.

Step 3F:
1. Transportation cost optimization
2. Inventory constraints
3. Plant capacity constraints
4. Reassignment penalty
5. Inventory risk penalty
6. Capacity risk penalty
7. Business cost objective

Author: Sirama Avinash
"""

from src.classical.cost_matrix import CostMatrix

from pathlib import Path

import pulp


class LinearProgrammingOptimizer:


    def __init__(self):

        print("Linear Programming Optimizer initialized.")



    def optimize(
        self,
        dataframe,
        max_orders=50,
        reassignment_penalty=5,
        inventory_penalty=500,
        capacity_penalty=200
    ):


        print("\n========== LINEAR PROGRAMMING ==========\n")


        df = dataframe.copy()



        # ----------------------------------
        # Required Columns
        # ----------------------------------

        required = [

            "Plant",
            "Available_inventory",
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
        # Small Test Dataset
        # ----------------------------------

        df = df.iloc[:max_orders].copy()



        plants = sorted(
            df["Plant"].unique()
        )


        orders = list(df.index)



        # ----------------------------------
        # Cost Matrix
        # ----------------------------------

        cost_builder = CostMatrix()

        cost_matrix = cost_builder.build_cost_matrix(df)



        print("\nTransportation Cost Matrix:\n")

        print(cost_matrix)



        # ----------------------------------
        # Inventory
        # ----------------------------------

        inventory = (

            df.groupby("Plant")
            ["Available_inventory"]
            .sum()
            .to_dict()

        )



        # ----------------------------------
        # Capacity
        # ----------------------------------

        capacity = {}


        for plant in plants:

            capacity[plant] = (
                inventory[plant] * 0.80
            )



        # ----------------------------------
        # Risk Calculation
        # ----------------------------------

        plant_demand = (

            df.groupby("Plant")
            ["Predicted_Demand"]
            .sum()
            .to_dict()

        )


        inventory_risk = {}


        capacity_risk = {}


        for plant in plants:


            # Inventory shortage risk

            if plant_demand[plant] > inventory[plant]:

                inventory_risk[plant] = inventory_penalty

            else:

                inventory_risk[plant] = 0


            utilization = (
            plant_demand[plant]
            /
            capacity[plant]
            )


            if utilization > 0.90:

                capacity_risk[plant] = (
                    capacity_penalty *
                    utilization
                )

            else:

                capacity_risk[plant] = 0



        # ----------------------------------
        # Debug
        # ----------------------------------

        print("\n========== LP DEBUG ==========\n")


        print(
            "Total Predicted Demand:"
        )

        print(
            df["Predicted_Demand"].sum()
        )


        print("\nInventory Per Plant:")

        print(

            df.groupby("Plant")
            ["Available_inventory"]
            .sum()

        )


        print("\nCapacity Per Plant:")

        for plant in plants:

            print(
                f"{plant}: {capacity[plant]:.4f}"
            )



        print("\nInventory Risk:")

        print(inventory_risk)


        print("\nCapacity Risk:")

        print(capacity_risk)



        # ----------------------------------
        # LP Model
        # ----------------------------------

        model = pulp.LpProblem(

            "Nestle_DOM",

            pulp.LpMinimize

        )



        # ----------------------------------
        # Decision Variables
        # ----------------------------------

        x = pulp.LpVariable.dicts(

            "Assign",

            (
                orders,
                plants
            ),

            lowBound=0,

            upBound=1,

            cat="Binary"

        )



        # ----------------------------------
        # Business Objective
        #
        # Transport
        # + Reassignment
        # + Inventory Risk
        # + Capacity Risk
        # ----------------------------------

        model += pulp.lpSum(

            (

                cost_matrix.loc[
                    df.loc[o,"Plant"],
                    p
                ]


                +

                (
                    reassignment_penalty
                    if p != df.loc[o,"Plant"]
                    else 0
                )


                +

                inventory_risk[p]


                +

                capacity_risk[p]

            )

            *

            x[o][p]


            for o in orders

            for p in plants

        )



        # ----------------------------------
        # Order Assignment Constraint
        # ----------------------------------

        for o in orders:

            model += (

                pulp.lpSum(

                    x[o][p]

                    for p in plants

                )

                == 1

            )



        # ----------------------------------
        # Inventory Constraint
        # ----------------------------------

        for p in plants:

            model += (

                pulp.lpSum(

                    x[o][p]
                    *
                    df.loc[o,"Predicted_Demand"]

                    for o in orders

                )

                <= inventory[p]

            )



        # ----------------------------------
        # Capacity Constraint
        # ----------------------------------

        for p in plants:

            model += (

                pulp.lpSum(

                    x[o][p]
                    *
                    df.loc[o,"Predicted_Demand"]

                    for o in orders

                )

                <= capacity[p]

            )



        # ----------------------------------
        # Solve
        # ----------------------------------

        solver = pulp.PULP_CBC_CMD(
            msg=False
        )


        model.solve(solver)



        solver_status = pulp.LpStatus[
            model.status
        ]


        print(
            "\nSolver Status:",
            solver_status
        )



        # ----------------------------------
        # Extract Results
        # ----------------------------------

        assigned = []

        changed = []

        assignment_cost = []



        for o in orders:


            assigned_plant = None


            for p in plants:


                value = pulp.value(
                    x[o][p]
                )


                if value is not None and value > 0.5:

                    assigned_plant = p

                    break



            assigned.append(
                assigned_plant
            )



            if assigned_plant == df.loc[o,"Plant"]:

                changed.append("No")

            else:

                changed.append("Yes")



            if assigned_plant is not None:

                assignment_cost.append(

                    cost_matrix.loc[
                        df.loc[o,"Plant"],
                        assigned_plant
                    ]

                )

            else:

                assignment_cost.append(None)



        # ----------------------------------
        # Final Output
        # ----------------------------------

        df["Original_Plant"] = df["Plant"]

        df["Assigned_Plant"] = assigned

        df["Assignment_Type"] = (
            "Linear Programming"
        )

        df["Plant_Changed"] = changed


        df["Assignment_Cost"] = assignment_cost


        df["Solver_Status"] = solver_status



        # ----------------------------------
        # Save
        # ----------------------------------

        output_dir = Path("outputs")

        output_dir.mkdir(
            exist_ok=True
        )


        output_file = (
            output_dir /
            "linear_programming.csv"
        )


        df.to_csv(
            output_file,
            index=False
        )



        print(
            f"\nResults saved to:\n{output_file}"
        )


        print(
            f"\nOrders Optimized : {len(df)}"
        )


        print(
            "Orders Reassigned :",
            (
                df["Plant_Changed"]
                ==
                "Yes"
            ).sum()
        )


        print(
            "Total Assignment Cost:",
            df["Assignment_Cost"].sum()
        )


        print(
            "Total Business Optimization Cost:",
            pulp.value(model.objective)
        )


        return df