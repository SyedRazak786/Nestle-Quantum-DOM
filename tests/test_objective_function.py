import pandas as pd

from src.optimization.qubo_formulation import QUBOFormulation
from src.optimization.objective_function import ObjectiveFunction

df = pd.read_csv("outputs/ai_decisions.csv")

print("Rows :", len(df))

qubo = QUBOFormulation()

qubo_result = qubo.create_binary_variables(
    df,
    max_orders=50
)

variables = qubo_result["variable_dataframe"]

builder = ObjectiveFunction()

objective = builder.build_objective(
    df.iloc[:50].reset_index(drop=True),
    variables
)

print("\n========== OBJECTIVE ==========\n")

print(objective.head())

print("\nTotal Objective Terms:")

print(len(objective))