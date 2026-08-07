from pathlib import Path

import pandas as pd

from src.classical.default_assignment import (
    DefaultAssignment
)


# ----------------------------------
# Load AI Decision Table
# ----------------------------------

input_file = Path(
    "outputs/ai_decisions.csv"
)

df = pd.read_csv(input_file)

print("Rows :", len(df))


# ----------------------------------
# Default Assignment
# ----------------------------------

assignment = DefaultAssignment()

results = assignment.assign_orders(df)


# ----------------------------------
# Save Output
# ----------------------------------

output_dir = Path("outputs")

output_dir.mkdir(exist_ok=True)

output_file = output_dir / "default_assignment.csv"

results.to_csv(
    output_file,
    index=False
)

print(
    f"\nDefault assignment saved to:\n{output_file}"
)


# ----------------------------------
# Preview
# ----------------------------------

print("\n========== DEFAULT ASSIGNMENT ==========\n")

print(

    results[

        [
            "Plant",
            "Assigned_Plant",
            "Predicted_Demand",
            "Current_Inventory",
            "Inventory_Status",
            "Recommendation",
            "Assignment_Type",
            "Assignment_Status"
        ]

    ].head()

)


print("\nShape:")

print(results.shape)