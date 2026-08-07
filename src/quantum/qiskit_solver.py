"""
qiskit_solver.py
--------------------------------
Phase 4G.2

Converts the QUBO matrix into a
QuadraticProgram and solves it
using QAOA.

Author: Sirama Avinash
"""

from pathlib import Path

import numpy as np

from qiskit.primitives import StatevectorSampler

from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA

from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer


class QiskitSolver:

    def __init__(self):

        print("Qiskit Solver initialized.")

    def solve(self, qubo_matrix):

        print("\n========== QISKIT QAOA SOLVER ==========\n")

        # =====================================
        # Convert DataFrame to NumPy
        # =====================================

        if hasattr(qubo_matrix, "values"):

            Q = qubo_matrix.values

        else:

            Q = np.array(qubo_matrix)

        n = Q.shape[0]

        print(f"Variables : {n}")

        # =====================================
        # Safety Check
        # =====================================

        MAX_QAOA_VARIABLES = 20

        if n > MAX_QAOA_VARIABLES:

            raise ValueError(

                "\n=====================================\n"
                "QAOA cannot simulate this problem.\n"
                "=====================================\n\n"
                f"Variables           : {n}\n"
                f"Recommended Maximum : {MAX_QAOA_VARIABLES}\n\n"
                "Reason:\n"
                "Statevector simulation requires 2^n amplitudes.\n"
                "100 variables requires an impossible amount of memory.\n\n"
                "Solutions:\n"
                "1. Reduce max_orders to 2-4.\n"
                "2. Use the Hybrid Solver (Phase 4G.3).\n"
                "3. Run on real quantum hardware.\n"

            )

        # =====================================
        # Build Quadratic Program
        # =====================================

        qp = QuadraticProgram("Nestle_DOM_QUBO")

        for i in range(n):

            qp.binary_var(name=f"x{i}")

        linear = {}
        quadratic = {}

        for i in range(n):

            linear[f"x{i}"] = float(Q[i, i])

            for j in range(i + 1, n):

                if Q[i, j] != 0:

                    quadratic[(f"x{i}", f"x{j}")] = float(Q[i, j])

        qp.minimize(

            linear=linear,

            quadratic=quadratic

        )

        print("Quadratic Program created successfully.")

        # =====================================
        # Save LP Model
        # =====================================
        output_dir = Path("outputs")
        output_dir.mkdir(exist_ok=True)

        lp_file = output_dir / "quadratic_program.lp"

        with open(lp_file, "w") as f:
            f.write(qp.export_as_lp_string())

        print(f"\nLP model saved to:\n{lp_file}")
        # =====================================
        # Configure QAOA
        # =====================================

        sampler = StatevectorSampler()
        optimizer = COBYLA(
            maxiter=20
        )

        qaoa = QAOA(
            sampler=sampler,
            optimizer=optimizer,
            reps=1
        )

        solver = MinimumEigenOptimizer(

            qaoa

        )

        print("\nRunning QAOA...\n")

        # =====================================
        # Solve
        # =====================================

        result = solver.solve(qp)

        print("\nOptimization Finished.")

        print("\nObjective Value")

        print(result.fval)

        print("\nStatus")

        print(result.status)

        print("\nSolution")

        print(result.x)

        # =====================================
        # Save Results
        # =====================================

        result_file = output_dir / "qaoa_solution.txt"

        with open(result_file, "w") as f:

            f.write("Objective Value\n")
            f.write(f"{result.fval}\n\n")

            f.write("Status\n")
            f.write(f"{result.status}\n\n")

            f.write("Solution\n")
            f.write(str(result.x))

        print(f"\nResults saved to:\n{result_file}")

        return result