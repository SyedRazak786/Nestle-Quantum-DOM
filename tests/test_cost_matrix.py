import pandas as pd

from src.classical.cost_matrix import CostMatrix


df = pd.read_csv(
    "outputs/ai_decisions.csv"
)

builder = CostMatrix()

matrix = builder.build_cost_matrix(df)

print("\n========== COST MATRIX ==========\n")

print(matrix)