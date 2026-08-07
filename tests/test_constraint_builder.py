"""
test_constraint_builder.py
--------------------------------
Test Phase 4B

Constraint Builder

Author: Sirama Avinash
"""

import pandas as pd

from src.optimization.qubo_formulation import QUBOFormulation
from src.optimization.constraint_builder import ConstraintBuilder


# ----------------------------------
# Load AI Output
# ----------------------------------

df = pd.read_csv("outputs/ai_decisions.csv")

print("Rows :", len(df))


# ----------------------------------
# Create QUBO Variables
# ----------------------------------

qubo = QUBOFormulation()

qubo_result = qubo.create_binary_variables(
    df,
    max_orders=50
)

variables = qubo_result["variable_dataframe"]


# ----------------------------------
# Build Constraints
# ----------------------------------

builder = ConstraintBuilder()

constraints = builder.build_constraints(
    variables
)


# ----------------------------------
# Results
# ----------------------------------

print("\n========== CONSTRAINTS ==========\n")

print(constraints.head())

print("\nTotal Constraints :")

print(len(constraints))