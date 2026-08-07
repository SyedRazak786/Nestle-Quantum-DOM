"""
pennylane_solver.py
--------------------------------
Phase 4G.1

Real PennyLane QAOA Solver
for the Nestlé Distributed
Order Management project.

Author: Sirama Avinash
"""

from pathlib import Path

import numpy as np
import pennylane as qml

from src.quantum.simulator_config import SimulatorConfig


class PennyLaneResult:
    """
    Keeps the same output format as
    QiskitSolver so that the existing
    SolutionDecoder can be reused.
    """

    def __init__(
        self,
        solution,
        energy,
        status="SUCCESS"
    ):

        self.x = np.array(solution)

        self.fval = float(energy)

        self.status = status


class PennyLaneSolver:

    def __init__(self):

        print("PennyLane Solver initialized.")

    def solve(
        self,
        qubo_matrix
    ):

        print(
            "\n========== PENNYLANE QAOA SOLVER ==========\n"
        )

        # =====================================
        # Convert DataFrame to NumPy
        # =====================================

        if hasattr(
            qubo_matrix,
            "values"
        ):

            Q = qubo_matrix.values

        else:

            Q = np.array(
                qubo_matrix,
                dtype=float
            )

        n = Q.shape[0]

        print("Variables :", n)

        # =====================================
        # Safety Check
        # =====================================

        MAX_VARIABLES = 20

        if n > MAX_VARIABLES:

            raise ValueError(

                "\n=====================================\n"
                "PennyLane QAOA cannot simulate\n"
                "this many variables.\n"
                "=====================================\n\n"

                f"Variables           : {n}\n"
                f"Recommended Maximum : {MAX_VARIABLES}\n\n"

                "Reason:\n"
                "Statevector simulation grows as 2^n.\n\n"

                "Recommended:\n"
                "- Use 2-4 orders per batch\n"
                "- Use Hybrid Solver\n"
                "- Use Quantum Hardware\n"
            )

        # =====================================
        # Output Folder
        # =====================================

        output_dir = Path("outputs")

        output_dir.mkdir(
            exist_ok=True
        )

        # =====================================
        # Quantum Device
        # =====================================

        simulator = SimulatorConfig()

        dev = simulator.get_pennylane_device(
            wires=n
        )

        print("\nQuantum Device Ready")

        print("Wires :", n)

        # =====================================
        # Convert QUBO Matrix
        # =====================================

        print(
            "\nPreparing QUBO Matrix..."
        )

        diagonal = np.diag(Q)

        print(
            "Diagonal Terms :",
            len(diagonal)
        )

        non_zero = np.count_nonzero(Q)

        print(
            "Non-zero Elements :",
            non_zero
        )

        print(
            "\nQUBO preprocessing completed."
        )

        # =====================================
        # PART 1 ENDS HERE
        # =====================================

        # Next Part:
        # Build Cost Hamiltonian
                # =====================================
        # PART 1B
        # Build Cost Hamiltonian
        # =====================================

        print("\nBuilding Cost Hamiltonian...")

        coeffs = []

        observables = []

        # -------------------------------------
        # Linear Terms
        # -------------------------------------

        for i in range(n):

            if abs(Q[i, i]) > 1e-10:

                coeffs.append(
                    float(Q[i, i])
                )

                observables.append(

                    qml.PauliZ(i)

                )

        # -------------------------------------
        # Quadratic Terms
        # -------------------------------------

        for i in range(n):

            for j in range(i + 1, n):

                if abs(Q[i, j]) > 1e-10:

                    coeffs.append(

                        float(Q[i, j])

                    )

                    observables.append(

                        qml.PauliZ(i)
                        @
                        qml.PauliZ(j)

                    )

        # -------------------------------------
        # Create Hamiltonian
        # -------------------------------------

        cost_hamiltonian = qml.Hamiltonian(

            coeffs,

            observables

        )

        print("Cost Hamiltonian created.")

        print("Terms :", len(coeffs))

        # -------------------------------------
        # Display Sample Terms
        # -------------------------------------

        sample = min(5, len(coeffs))

        print("\nSample Hamiltonian Terms:\n")

        for i in range(sample):

            print(

                f"{coeffs[i]:8.2f}",

                observables[i]

            )

        # -------------------------------------
        # Save Hamiltonian
        # -------------------------------------

        hamiltonian_file = (

            output_dir /

            "cost_hamiltonian.txt"

        )

        with open(

            hamiltonian_file,

            "w"

        ) as f:

            f.write(

                "Cost Hamiltonian\n\n"

            )

            for c, op in zip(

                coeffs,

                observables

            ):

                f.write(

                    f"{c} * {op}\n"

                )

        print(

            "\nHamiltonian saved to:"

        )

        print(hamiltonian_file)

        # =====================================
        # PART 1B COMPLETE
        # =====================================
                # =====================================
        # PART 2
        # Build Mixer Hamiltonian
        # =====================================

        print("\nBuilding Mixer Hamiltonian...")

        mixer_hamiltonian = qml.qaoa.x_mixer(
            wires=range(n)
        )

        print("Mixer Hamiltonian created.")

        # =====================================
        # QAOA Parameters
        # =====================================

        p = 2

        print("\nQAOA Layers :", p)

        # =====================================
        # Create QAOA Circuit
        # =====================================

        @qml.qnode(dev)

        def circuit(gammas, betas):

            # -----------------------------
            # Initial Superposition
            # -----------------------------

            for wire in range(n):

                qml.Hadamard(
                    wires=wire
                )

            # -----------------------------
            # QAOA Layers
            # -----------------------------

            for layer in range(p):

                qml.qaoa.cost_layer(

                    gammas[layer],

                    cost_hamiltonian

                )

                qml.qaoa.mixer_layer(

                    betas[layer],

                    mixer_hamiltonian

                )

            # -----------------------------
            # Measure All Qubits
            # -----------------------------

            return qml.probs(
                wires=range(n)
            )

        print("\nQuantum Circuit Created.")

        # =====================================
        # Energy Function
        # =====================================

        def qubo_energy(bitstring):

            energy = 0.0

            for i in range(n):

                energy += (
                    Q[i, i]
                    * bitstring[i]
                )

                for j in range(i + 1, n):

                    energy += (

                        Q[i, j]

                        * bitstring[i]

                        * bitstring[j]

                    )

            return energy

        # =====================================
        # Expectation Value
        # =====================================

        def objective(params):

            gammas = params[:p]

            betas = params[p:]

            probs = circuit(

                gammas,

                betas

            )

            expectation = 0.0

            for state in range(2 ** n):

                bits = np.array(

                    list(

                        np.binary_repr(

                            state,

                            width=n

                        )

                    ),

                    dtype=int

                )

                expectation += (

                    probs[state]

                    * qubo_energy(bits)

                )

            return expectation

        print("Objective Function Ready.")


        # =====================================
        # PART 3
        # Optimize QAOA Parameters
        # =====================================

        print("\nRunning PennyLane QAOA...\n")

        from scipy.optimize import minimize

        # Initial parameters
        initial_params = np.random.uniform(
            low=0,
            high=np.pi,
            size=2 * p
        )

        optimization = minimize(

            objective,

            initial_params,

            method="COBYLA",

            options={
                "maxiter": 30,
                "disp": False
            }

        )

        print("Optimization Finished.")

        print("\nOptimal Parameters")

        print(optimization.x)

        print("\nMinimum Energy")

        print(optimization.fun)

        # =====================================
        # Execute Final Circuit
        # =====================================

        gammas = optimization.x[:p]

        betas = optimization.x[p:]

        probabilities = circuit(
            gammas,
            betas
        )

        # =====================================
        # Find Best Bitstring
        # =====================================

        best_state = int(
            np.argmax(probabilities)
        )

        solution = np.array(

            list(

                np.binary_repr(

                    best_state,

                    width=n

                )

            ),

            dtype=int

        )

        energy = qubo_energy(solution)

        print("\nMost Probable State")

        print(best_state)

        print("\nSolution")

        print(solution)

        print("\nObjective Value")

        print(energy)

        # =====================================
        # Save Results
        # =====================================

        result_file = (
            output_dir /
            "pennylane_solution.txt"
        )

        with open(
            result_file,
            "w"
        ) as f:

            f.write(
                "PennyLane QAOA Result\n\n"
            )

            f.write(
                f"Variables : {n}\n\n"
            )

            f.write(
                "Optimal Parameters\n"
            )

            f.write(
                str(optimization.x)
            )

            f.write("\n\n")

            f.write(
                "Objective Value\n"
            )

            f.write(
                str(energy)
            )

            f.write("\n\n")

            f.write(
                "Solution\n"
            )

            f.write(
                str(solution)
            )

        print(
            "\nResults saved to:"
        )

        print(result_file)

        # =====================================
        # Return Compatible Result
        # =====================================

        return PennyLaneResult(

            solution=solution,

            energy=energy,

            status="SUCCESS"

        )