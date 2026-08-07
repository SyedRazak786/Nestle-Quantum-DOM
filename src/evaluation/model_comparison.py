"""
model_comparison.py
--------------------------------
Phase 5

Loads benchmark results and
creates comparison tables
and charts.

Author: Sirama Avinash
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


class ModelComparison:
    """
    Compare optimization models using
    benchmark results.
    """

    def __init__(self):
        print("Model Comparison initialized")

    def compare(
        self,
        benchmark_file="outputs/benchmarks/benchmark_results.csv",
        output_folder="outputs/comparison",
    ):
        """
        Generate comparison charts.
        """

        benchmark_file = Path(benchmark_file)
        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)

        if not benchmark_file.exists():
            raise FileNotFoundError(
                f"Benchmark file not found:\n{benchmark_file}"
            )

        df = pd.read_csv(benchmark_file)

        print("\n========== MODEL COMPARISON ==========\n")
        print(df)

        # Save comparison table
        comparison_csv = output_folder / "model_comparison.csv"
        df.to_csv(comparison_csv, index=False)

        # -------------------------------
        # Total Orders
        # -------------------------------
        plt.figure(figsize=(8, 5))
        plt.bar(df["Method"], df["Total Orders"])
        plt.title("Total Orders Processed")
        plt.ylabel("Orders")
        plt.xticks(rotation=20)
        plt.tight_layout()
        plt.savefig(output_folder / "total_orders.png")
        plt.close()

        # -------------------------------
        # Reassignment Rate
        # -------------------------------
        plt.figure(figsize=(8, 5))
        plt.bar(df["Method"], df["Reassignment Rate (%)"])
        plt.title("Reassignment Rate")
        plt.ylabel("Percentage")
        plt.xticks(rotation=20)
        plt.tight_layout()
        plt.savefig(output_folder / "reassignment_rate.png")
        plt.close()

        # -------------------------------
        # Execution Time
        # -------------------------------
        plt.figure(figsize=(8, 5))
        plt.bar(df["Method"], df["Execution Time(sec)"])
        plt.title("Execution Time")
        plt.ylabel("Seconds")
        plt.xticks(rotation=20)
        plt.tight_layout()
        plt.savefig(output_folder / "execution_time.png")
        plt.close()

        print("\nComparison table saved:")
        print(comparison_csv)

        print("\nCharts saved to:")
        print(output_folder)

        return df