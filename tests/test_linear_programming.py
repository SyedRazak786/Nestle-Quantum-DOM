import pandas as pd

from src.classical.linear_programming import (
    LinearProgrammingOptimizer
)


# -----------------------------
# Load AI Decisions
# -----------------------------

df = pd.read_csv(
    "outputs/ai_decisions.csv"
)

print(
    f"Rows : {len(df)}"
)

# -----------------------------
# Run LP
# -----------------------------

optimizer = (

    LinearProgrammingOptimizer()

)

results = optimizer.optimize(

    df,

    max_orders=50

)

# -----------------------------
# Display
# -----------------------------

print(
    "\n========== LP RESULTS ==========\n"
)

print(

    results[
        [

            "Original_Plant",

            "Assigned_Plant",

            "Predicted_Demand",

            "Plant_Changed",

            "Solver_Status"

        ]

    ].head()

)

print("\nShape:")

print(results.shape)