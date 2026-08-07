from src.quantum.solution_decoder import SolutionDecoder
from src.quantum.qiskit_solver import QiskitSolver

import pandas as pd


print("Loading QUBO variable mapping...")

variable_mapping = pd.read_csv(
    "outputs/qubo_variables.csv"
)

print(variable_mapping)


print("\nLoading QUBO matrix...")

qubo_matrix = pd.read_csv(
    "outputs/qubo_matrix.csv"
)

print(qubo_matrix.head())

qubo_matrix = qubo_matrix.values

print("QUBO Matrix Shape:")
print(qubo_matrix.shape)


solver = QiskitSolver()

result = solver.solve(
    qubo_matrix
)


decoder = SolutionDecoder()

assignments = decoder.decode(
    variable_mapping=variable_mapping,
    qaoa_result=result
)


print("\n========== FINAL ASSIGNMENTS ==========\n")

print(assignments)