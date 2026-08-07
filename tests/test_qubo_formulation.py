import pandas as pd

from src.optimization.qubo_formulation import (
    QUBOFormulation
)


df = pd.read_csv(
    "outputs/ai_decisions.csv"
)

print("Rows :", len(df))

qubo = QUBOFormulation()

result = qubo.create_binary_variables(
    df
)

print("\n========== QUBO VARIABLES ==========\n")

print(
    result["variable_dataframe"].head()
)

print("\nTotal Variables:")

print(
    len(result["variable_dataframe"])
)