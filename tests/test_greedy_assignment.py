import pandas as pd

from src.classical.greedy_assignment import GreedyAssignment


# -----------------------------
# Load AI Decision Table
# -----------------------------

df = pd.read_csv(
    "outputs/ai_decisions.csv"
)

print(f"Rows : {len(df)}")

# -----------------------------
# Run Greedy Assignment
# -----------------------------

optimizer = GreedyAssignment()

results = optimizer.optimize(df)

# -----------------------------
# Display Results
# -----------------------------

print("\n========== GREEDY ASSIGNMENT ==========\n")

print(
    results[
        [
            "Original_Plant",
            "Assigned_Plant",
            "Available_inventory",
            "Predicted_Demand",
            "Plant_Changed",
            "Optimization_Status"
        ]
    ].head()
)

print("\nShape:")

print(results.shape)