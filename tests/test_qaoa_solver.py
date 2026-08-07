from src.data.loader import DatasetLoader
from src.ai.feature_engineering import AIFeatureEngineer
from src.ai.model_training import AIModelTrainer
from src.ai.demand_prediction import DemandPredictor

from src.optimization.qubo_formulation import QUBOFormulation
from src.optimization.objective_function import ObjectiveFunction
from src.optimization.qubo_builder import QUBOBuilder

from src.quantum.qiskit_solver import QiskitSolver
from src.quantum.solution_decoder import SolutionDecoder

import pandas as pd


# =====================================================
# Load Dataset
# =====================================================

loader = DatasetLoader()
df = loader.load_master_dataset()

print("Rows :", len(df))


# =====================================================
# Feature Engineering
# =====================================================

engineer = AIFeatureEngineer()

df, X, y = engineer.prepare_dataset(
    df,
    target_column="SalesOrderDemand"
)


# =====================================================
# Train Model
# =====================================================

trainer = AIModelTrainer()

model, X_train, X_test, y_train, y_test = trainer.train(
    X,
    y
)


# =====================================================
# Demand Prediction
# =====================================================

predictor = DemandPredictor()

predictions = predictor.predict(
    model,
    X_test
)

test_df = X_test.copy()

test_df["Plant"] = df.loc[X_test.index, "Plant"]
test_df["Predicted_Demand"] = predictions.values


# =====================================================
# Quantum Sample
# =====================================================

SAMPLE_ORDERS = 20
BATCH_SIZE = 3

test_df = test_df.head(SAMPLE_ORDERS).copy()

total_orders = len(test_df)
total_batches = (total_orders + BATCH_SIZE - 1) // BATCH_SIZE

print("\n========================================")
print("QUANTUM OPTIMIZATION")
print("========================================")
print("Orders Selected :", total_orders)
print("Batch Size      :", BATCH_SIZE)
print("Total Batches   :", total_batches)

all_assignments = []


# =====================================================
# Run QAOA
# =====================================================

for batch_no, start in enumerate(range(0, total_orders, BATCH_SIZE), start=1):

    end = min(start + BATCH_SIZE, total_orders)

    print("\n----------------------------------------")
    print(f"Batch {batch_no}/{total_batches}")
    print(f"Orders : {start} - {end-1}")
    print("----------------------------------------")

    batch_df = test_df.iloc[start:end].copy()

    try:

        # Binary Variables
        qubo = QUBOFormulation()

        qubo_result = qubo.create_binary_variables(
            batch_df,
            max_orders=len(batch_df)
        )

        # Objective Function
        objective = ObjectiveFunction()

        objective_df = objective.build_objective(
            batch_df,
            qubo_result["variable_dataframe"]
        )

        # QUBO Matrix
        builder = QUBOBuilder()

        qubo_matrix = builder.build_qubo(
            variable_mapping=qubo_result["variable_dataframe"],
            objective_df=objective_df
        )

        # Solve
        solver = QiskitSolver()

        result = solver.solve(qubo_matrix)

        # Decode
        decoder = SolutionDecoder()

        assignments = decoder.decode(
            variable_mapping=qubo_result["variable_dataframe"],
            qaoa_result=result
        )

        assignments["Batch"] = batch_no

        all_assignments.append(assignments)

        print("Variables   :", len(qubo_result["variable_dataframe"]))
        print("Assignments :", len(assignments))
        print("Objective   :", result.fval)

    except Exception as e:

        print("Batch Failed")
        print(e)


# =====================================================
# Final Output
# =====================================================

print("\n========================================")
print("FINAL RESULTS")
print("========================================")

if len(all_assignments) > 0:

    final_assignments = pd.concat(
        all_assignments,
        ignore_index=True
    )

    print(final_assignments)

    print("\nTotal Assignments :", len(final_assignments))

    final_assignments.to_csv(
        "outputs/all_quantum_assignments.csv",
        index=False
    )

    print("\nSaved : outputs/all_quantum_assignments.csv")

else:

    print("No assignments generated.")