"""
Phase 5 - Benchmarking

Compares:

1. Greedy Classical
2. Linear Programming
3. Qiskit
4. PennyLane
5. Hybrid

Output:
outputs/benchmarks/benchmark_results.csv
"""

import os
import time
import pandas as pd


class Benchmark:


    def __init__(self):

        print("Benchmark initialized")


    def calculate_metrics(
            self,
            method,
            file_path,
            runtime
    ):

        df = pd.read_csv(file_path)


        total_orders = len(df)


        # Find plant columns automatically

        original_col = None
        assigned_col = None


        for col in df.columns:

            if "Original" in col:
                original_col = col

            if "Assigned" in col:
                assigned_col = col



        if original_col and assigned_col:

            reassigned = (
                df[original_col]
                !=
                df[assigned_col]
            ).sum()

        else:

            reassigned = 0



        rate = (
            reassigned /
            total_orders
        ) * 100



        return {


            "Method": method,

            "Total Orders": total_orders,

            "Reassigned Orders": reassigned,

            "Reassignment Rate (%)":
                round(rate,2),

            "Execution Time(sec)":
                round(runtime,4)

        }



    def run(self):


        print(
            "\n========== BENCHMARK RUN ==========\n"
        )


        os.makedirs(
            "outputs/benchmarks",
            exist_ok=True
        )


        start=time.time()

        results=[]



        files = [

            (
                "Greedy",
                "outputs/greedy_assignment.csv"
            ),

            (
                "Linear Programming",
                "outputs/linear_programming.csv"
            ),

            (
                "Qiskit",
                "outputs/quantum_assignments.csv"
            ),

            (
                "PennyLane",
                "outputs/pennylane_assignments.csv"
            ),

            (
                "Hybrid",
                "outputs/hybrid_results.csv"
            )

        ]



        for method,file in files:


            if os.path.exists(file):


                runtime = (
                    time.time()-start
                )


                result = self.calculate_metrics(
                    method,
                    file,
                    runtime
                )


                results.append(result)


            else:

                print(
                    "Missing:",
                    file
                )



        benchmark_df = pd.DataFrame(results)



        print(benchmark_df)



        benchmark_df.to_csv(

            "outputs/benchmarks/benchmark_results.csv",

            index=False

        )


        print(
            "\nSaved:"
            " outputs/benchmarks/benchmark_results.csv"
        )


        return benchmark_df