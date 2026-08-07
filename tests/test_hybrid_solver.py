"""
test_hybrid_solver.py
--------------------------------
Tests the Hybrid Quantum Solver.

Pipeline

1. Load Dataset
2. AI Prediction
3. QUBO Formulation
4. Qiskit Solver
5. PennyLane Solver
6. Hybrid Solver
7. Decode Solution

Author: Sirama Avinash
"""

from src.data.loader import DatasetLoader

from src.ai.feature_engineering import AIFeatureEngineer
from src.ai.model_training import AIModelTrainer
from src.ai.demand_prediction import DemandPredictor

from src.optimization.qubo_formulation import QUBOFormulation
from src.optimization.objective_function import ObjectiveFunction
from src.optimization.qubo_builder import QUBOBuilder

from src.quantum.hybrid_solver import HybridSolver
from src.quantum.solution_decoder import SolutionDecoder
from src.quantum.qiskit_solver import QiskitSolver
from src.quantum.pennylane_solver import PennyLaneSolver


# =====================================
# Load Dataset
# =====================================

loader = DatasetLoader()

df = loader.load_master_dataset()

# =====================================
# Feature Engineering
# =====================================

engineer = AIFeatureEngineer()

df, X, y = engineer.prepare_dataset(

    df,

    target_column="SalesOrderDemand"

)

# =====================================
# Train Model
# =====================================

trainer = AIModelTrainer()

model, X_train, X_test, y_train, y_test = trainer.train(

    X,

    y

)

# =====================================
# Demand Prediction
# =====================================

predictor = DemandPredictor()

predictions = predictor.predict(

    model,

    X_test

)

# =====================================
# Prepare Test Dataset
# =====================================

test_df = X_test.copy()

test_df["Order_ID"] = X_test.index
test_df["Plant"] = df.loc[X_test.index, "Plant"].values
test_df["Predicted_Demand"] = predictions.values

# =====================================
# Small Quantum Batch
# =====================================

batch_df = test_df.head(5)

# =====================================
# Build QUBO
# =====================================

qubo = QUBOFormulation()

qubo_result = qubo.create_binary_variables(

    batch_df,

    max_orders=len(batch_df)

)

objective = ObjectiveFunction()

objective_df = objective.build_objective(

    batch_df,

    qubo_result["variable_dataframe"]

)

builder = QUBOBuilder()

qubo_matrix = builder.build_qubo(

    variable_mapping=qubo_result["variable_dataframe"],

    objective_df=objective_df

)

# =====================================
# Run Qiskit Solver
# =====================================

qiskit_solver = QiskitSolver()

qiskit_result = qiskit_solver.solve(
    qubo_matrix
)

decoder = SolutionDecoder()

qiskit_assignments = decoder.decode(
    variable_mapping=qubo_result["variable_dataframe"],
    qaoa_result=qiskit_result
)

# =====================================
# Run PennyLane Solver
# =====================================

pennylane_solver = PennyLaneSolver()

pennylane_result = pennylane_solver.solve(
    qubo_matrix
)

pennylane_assignments = decoder.decode(
    variable_mapping=qubo_result["variable_dataframe"],
    qaoa_result=pennylane_result
)
original_df = batch_df[
    ["Order_ID", "Plant"]
].copy()

original_df.rename(
    columns={
        "Plant": "Original_Plant"
    },
    inplace=True
)

qiskit_assignments = qiskit_assignments.merge(
    original_df,
    on="Order_ID",
    how="left"
)

pennylane_assignments = pennylane_assignments.merge(
    original_df,
    on="Order_ID",
    how="left"
)

# =====================================
# Hybrid Solver
# =====================================

hybrid = HybridSolver()

result = hybrid.solve(
    qubo_matrix,
    qiskit_assignments=qiskit_assignments,
    pennylane_assignments=pennylane_assignments
)

print("\n========== WINNER ==========\n")

print(result["winner"])

print("\n========== COMPARISON ==========\n")

print(result["comparison"])

# =====================================
# Final Assignments (Winner)
# =====================================

if result["winner"] == "Qiskit":

    assignments = qiskit_assignments

else:

    assignments = pennylane_assignments

print("\n========== FINAL ASSIGNMENTS ==========\n")

print(assignments)

print("\nHybrid Solver Test Completed.")