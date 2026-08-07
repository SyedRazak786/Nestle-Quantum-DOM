"""
test_qiskit_solver.py
--------------------------------
Tests the Qiskit Solver using batch processing.

Pipeline

1. Load Dataset
2. AI Prediction
3. Select 50 Benchmark Orders
4. Split into batches of 10
5. Build QUBO
6. Solve using Qiskit
7. Decode Solution
8. Merge all assignments
9. Save Output

Author: Sirama Avinash
"""

import pandas as pd

from src.data.loader import DatasetLoader

from src.ai.feature_engineering import AIFeatureEngineer
from src.ai.model_training import AIModelTrainer
from src.ai.demand_prediction import DemandPredictor

from src.optimization.qubo_formulation import QUBOFormulation
from src.optimization.objective_function import ObjectiveFunction
from src.optimization.qubo_builder import QUBOBuilder

from src.quantum.qiskit_solver import QiskitSolver
from src.quantum.solution_decoder import SolutionDecoder


# ==========================================
# Load Dataset
# ==========================================

loader = DatasetLoader()

df = loader.load_master_dataset()

print("Rows :", len(df))


# ==========================================
# AI Pipeline
# ==========================================

engineer = AIFeatureEngineer()

df, X, y = engineer.prepare_dataset(
    df,
    target_column="SalesOrderDemand"
)

trainer = AIModelTrainer()

model, X_train, X_test, y_train, y_test = trainer.train(
    X,
    y
)

predictor = DemandPredictor()

predictions = predictor.predict(
    model,
    X_test
)


# ==========================================
# Prepare Test Dataset
# ==========================================

test_df = X_test.copy()

test_df["Order_ID"] = X_test.index
test_df["Plant"] = df.loc[X_test.index, "Plant"].values
test_df["Predicted_Demand"] = predictions.values


# ==========================================
# Benchmark Dataset (10 Orders)
# ==========================================

benchmark_df = test_df.head(5).copy()

batch_size = 5

all_assignments = []


# ==========================================
# Initialize Objects
# ==========================================

qubo = QUBOFormulation()

objective = ObjectiveFunction()

builder = QUBOBuilder()

solver = QiskitSolver()

decoder = SolutionDecoder()


# ==========================================
# Process Each Batch
# ==========================================

for batch_no, start in enumerate(
    range(0, len(benchmark_df), batch_size),
    start=1
):

    print(f"\n========== BATCH {batch_no} ==========\n")

    batch_df = benchmark_df.iloc[
        start:start + batch_size
    ].copy()

    # ------------------------------
    # Binary Variables
    # ------------------------------

    qubo_result = qubo.create_binary_variables(
        batch_df,
        max_orders=len(batch_df)
    )

    variables = qubo_result["variable_dataframe"]

    # ------------------------------
    # Objective Function
    # ------------------------------

    objective_df = objective.build_objective(
        batch_df,
        variables
    )

    # ------------------------------
    # Build QUBO
    # ------------------------------

    qubo_matrix = builder.build_qubo(
        variable_mapping=variables,
        objective_df=objective_df
    )

    # ------------------------------
    # Solve
    # ------------------------------

    result = solver.solve(
        qubo_matrix
    )

    print(result)

    # ------------------------------
    # Decode
    # ------------------------------

    assignments = decoder.decode(
        variable_mapping=variables,
        qaoa_result=result
    )

    all_assignments.append(assignments)


# ==========================================
# Merge All Results
# ==========================================

final_assignments = pd.concat(
    all_assignments,
    ignore_index=True
)


# ==========================================
# Display
# ==========================================

print("\n========== FINAL ASSIGNMENTS ==========\n")

print(final_assignments)


# ==========================================
# Save
# ==========================================

final_assignments.to_csv(
    "outputs/quantum_assignments.csv",
    index=False
)

print(
    "\nSaved : outputs/quantum_assignments.csv"
)