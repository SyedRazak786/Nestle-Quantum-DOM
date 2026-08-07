import pandas as pd

from src.optimization.feasibility_checker import FeasibilityChecker

# ----------------------------------
# Load AI Output
# ----------------------------------

df = pd.read_csv("outputs/ai_decisions.csv")

df = df.iloc[:50].copy()

# ----------------------------------
# Create Solution
# ----------------------------------

solution = pd.DataFrame({

    "Order_ID": df.index,

    "Assigned_Plant": df["Plant"]

})

checker = FeasibilityChecker()

report = checker.check_solution(

    df,

    solution

)

print("\n========== FEASIBILITY REPORT ==========\n")

print(report)