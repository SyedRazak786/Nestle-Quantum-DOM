"""
hybrid_solver.py
--------------------------------
Phase 4H

Hybrid Quantum Solver

Runs both:

1. Qiskit QAOA
2. PennyLane QAOA

Compares:

• Objective Value
• Runtime

Returns the best solution.

Author: Sirama Avinash
"""

from pathlib import Path
import time
import pandas as pd

from src.quantum.qiskit_solver import QiskitSolver
from src.quantum.pennylane_solver import PennyLaneSolver


class HybridSolver:

    def __init__(self):

        print("Hybrid Solver initialized.")

    def get_metrics(self, assignments):

        if assignments is None:

            return 0, 0, 0, 0.0

        total_orders = len(assignments)

        reassigned_orders = assignments["Plant_Changed"].sum()

        unchanged_orders = total_orders - reassigned_orders

        reassignment_rate = (
            reassigned_orders / total_orders * 100
            if total_orders > 0 else 0
        )

        return (
            total_orders,
            reassigned_orders,
            unchanged_orders,
            round(reassignment_rate, 2)
        )

    def solve(
        self,
        qubo_matrix,
        qiskit_assignments=None,
        pennylane_assignments=None
    ):

        print("\n========== HYBRID QUANTUM SOLVER ==========\n")

        # ----------------------------------
        # Run Qiskit
        # ----------------------------------

        print("Running Qiskit Solver...\n")

        qiskit_solver = QiskitSolver()

        start = time.perf_counter()

        qiskit_result = qiskit_solver.solve(
            qubo_matrix
        )

        qiskit_time = (
            time.perf_counter() - start
        )

        # ----------------------------------
        # Run PennyLane
        # ----------------------------------

        print("\nRunning PennyLane Solver...\n")

        pennylane_solver = PennyLaneSolver()

        start = time.perf_counter()

        pennylane_result = pennylane_solver.solve(
            qubo_matrix
        )

        pennylane_time = (
            time.perf_counter() - start
        )

        (
            q_total,
            q_reassigned,
            q_unchanged,
            q_rate
        ) = self.get_metrics(
            qiskit_assignments
        )
        

        (
            p_total,
            p_reassigned,
            p_unchanged,
            p_rate
        ) = self.get_metrics(
            pennylane_assignments
        )

        # ----------------------------------
        # Comparison
        # ----------------------------------
        comparison = pd.DataFrame({

            "Solver":[
                "Qiskit",
                "PennyLane"
            ],

            "Objective_Value":[
                qiskit_result.fval,
                pennylane_result.fval
            ],

            "Runtime_Seconds":[
                round(qiskit_time,4),
                round(pennylane_time,4)
            ],

            "Total_Orders":[
                q_total,
                p_total
            ],

            "Reassigned_Orders":[
                q_reassigned,
                p_reassigned
            ],

            "Unchanged_Orders":[
                q_unchanged,
                p_unchanged
            ],

            "Reassignment_Rate":[
                q_rate,
                p_rate
            ]

        })

        print("\nComparison\n")

        print(comparison)

        # ----------------------------------
        # Select Best Solver
        # ----------------------------------

        if qiskit_result.fval <= pennylane_result.fval:

            winner = "Qiskit"

            best_result = qiskit_result

        else:

            winner = "PennyLane"

            best_result = pennylane_result

        print("\nWinner :", winner)

        print(
            "Objective :",
            best_result.fval
        )

        # ----------------------------------
        # Save Comparison
        # ----------------------------------

        output_dir = Path("outputs")

        output_dir.mkdir(exist_ok=True)

        comparison.to_csv(

            output_dir / "hybrid_results.csv",

            index=False

        )

        with open(
            output_dir / "hybrid_summary.txt",
            "w"
        ) as file:

            file.write("Hybrid Quantum Solver\n")
            file.write("=====================\n\n")
            file.write("Solver Comparison\n\n")

            for _, row in comparison.iterrows():

                file.write(f"{row['Solver']}\n")
                file.write("-"*len(row["Solver"]) + "\n")

                file.write(f"Objective Value : {row['Objective_Value']}\n")
                file.write(f"Runtime         : {row['Runtime_Seconds']} sec\n")
                file.write(f"Orders          : {row['Total_Orders']}\n")
                file.write(f"Reassigned      : {row['Reassigned_Orders']}\n")
                file.write(f"Unchanged       : {row['Unchanged_Orders']}\n")
                file.write(f"Rate            : {row['Reassignment_Rate']} %\n\n")

            file.write(f"Winner : {winner}\n")
            file.write("Reason : Lowest Objective Value\n")
        print("\nResults saved to:")

        print(output_dir / "hybrid_results.csv")

        print(output_dir / "hybrid_summary.txt")

        return {

            "winner": winner,

            "result": best_result,

            "comparison": comparison

        }    