"""
cost_matrix.py
--------------------------------
Creates transportation cost matrix
for Distributed Order Management.

Step 3E:
1. Plant distance matrix
2. Transportation rate
3. Shipping cost calculation

Used by:
- Greedy Assignment
- Linear Programming
- QUBO
- Quantum Optimization

Author: Sirama Avinash
"""

import pandas as pd


class CostMatrix:


    def __init__(self):

        print("Cost Matrix initialized.")



    def build_cost_matrix(self, dataframe):


        print("\n========== BUILDING COST MATRIX ==========\n")


        df = dataframe.copy()



        # ----------------------------------
        # Get Plants
        # ----------------------------------

        plants = sorted(
            df["Plant"].unique()
        )



        # ----------------------------------
        # Temporary Distance Matrix
        #
        # Replace later with real distance
        #
        # km
        # ----------------------------------

        distance_matrix = pd.DataFrame(

            0,

            index=plants,

            columns=plants,

            dtype=float

        )


        for source in plants:

            for destination in plants:


                if source == destination:

                    distance_matrix.loc[
                        source,
                        destination
                    ] = 0


                else:

                    # temporary distance

                    distance_matrix.loc[
                        source,
                        destination
                    ] = 100



        # ----------------------------------
        # Transportation Rate
        #
        # Example:
        # ₹1 per km
        #
        # Replace later
        # ----------------------------------

        transportation_rate = 1



        # ----------------------------------
        # Calculate Cost Matrix
        #
        # Cost = Distance × Rate
        # ----------------------------------

        cost_matrix = (

            distance_matrix
            *
            transportation_rate

        )



        print("Cost matrix created.")

        print(
            f"Plants : {len(plants)}"
        )


        print(
            "\nDistance Matrix:\n"
        )

        print(distance_matrix)



        print(
            "\nTransportation Cost Matrix:\n"
        )

        print(cost_matrix)



        return cost_matrix