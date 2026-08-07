from pathlib import Path
import pandas as pd

from src.optimization.qubo_formulation import QUBOFormulation
from src.optimization.objective_function import ObjectiveFunction
from src.optimization.qubo_builder import QUBOBuilder

# ----------------------------------
# Load AI Output
# ----------------------------------

df = pd.read_csv(
    Path("outputs") / "ai_decisions.csv"
)

print("Rows :", len(df))

# ----------------------------------
# Phase 4A
# ----------------------------------

qubo = QUBOFormulation()

qubo_result = qubo.create_binary_variables(
    df,
    max_orders=50
)

variables = qubo_result["variable_dataframe"]

# ----------------------------------
# Phase 4C
# ----------------------------------

objective = ObjectiveFunction()

objective_df = objective.build_objective(
    df.iloc[:50],
    variables
)

# ----------------------------------
# Phase 4D
# ----------------------------------

builder = QUBOBuilder()

qubo_matrix = builder.build_qubo(
    variables,
    objective_df
)

print("\n========== QUBO MATRIX ==========\n")

print(qubo_matrix.iloc[:5, :5])

print("\nMatrix Shape:")

print(qubo_matrix.shape)