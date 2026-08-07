"""
business_report.py
--------------------------------
Phase 5

Generates a business summary
from benchmark results.

Author: Sirama Avinash
"""

from pathlib import Path
import pandas as pd


class BusinessReport:
    """
    Generate a business-friendly
    report from benchmark results.
    """

    def __init__(self):
        print("Business Report initialized")

    def generate(
        self,
        benchmark_file="outputs/benchmarks/benchmark_results.csv",
        output_folder="outputs/business_report",
    ):
        benchmark_file = Path(benchmark_file)
        output_folder = Path(output_folder)

        output_folder.mkdir(parents=True, exist_ok=True)

        if not benchmark_file.exists():
            raise FileNotFoundError(
                f"Benchmark file not found:\n{benchmark_file}"
            )

        df = pd.read_csv(benchmark_file)

        # -------------------------
        # Summary Statistics
        # -------------------------

        total_methods = len(df)

        total_orders = int(df["Total Orders"].sum())

        fastest = df.loc[df["Execution Time(sec)"].idxmin()]

        slowest = df.loc[df["Execution Time(sec)"].idxmax()]

        lowest_reassign = df.loc[df["Reassignment Rate (%)"].idxmin()]

        highest_reassign = df.loc[df["Reassignment Rate (%)"].idxmax()]

        average_time = df["Execution Time(sec)"].mean()

        report = pd.DataFrame(
            {
                "Metric": [
                    "Optimization Methods",
                    "Total Orders Evaluated",
                    "Fastest Method",
                    "Slowest Method",
                    "Lowest Reassignment",
                    "Highest Reassignment",
                    "Average Execution Time (sec)",
                ],
                "Value": [
                    total_methods,
                    total_orders,
                    fastest["Method"],
                    slowest["Method"],
                    lowest_reassign["Method"],
                    highest_reassign["Method"],
                    round(average_time, 4),
                ],
            }
        )

        print("\n========== BUSINESS REPORT ==========\n")
        print(report)

        csv_path = output_folder / "business_summary.csv"

        report.to_csv(csv_path, index=False)

        txt_path = output_folder / "business_summary.txt"

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("NESTLÉ QUANTUM DOM BUSINESS REPORT\n")
            f.write("=" * 40 + "\n\n")

            f.write(f"Optimization Methods : {total_methods}\n")
            f.write(f"Total Orders Evaluated : {total_orders}\n")
            f.write(
                f"Fastest Method : {fastest['Method']} ({fastest['Execution Time(sec)']:.4f} sec)\n"
            )
            f.write(
                f"Slowest Method : {slowest['Method']} ({slowest['Execution Time(sec)']:.4f} sec)\n"
            )
            f.write(
                f"Lowest Reassignment : {lowest_reassign['Method']} ({lowest_reassign['Reassignment Rate (%)']:.2f}%)\n"
            )
            f.write(
                f"Highest Reassignment : {highest_reassign['Method']} ({highest_reassign['Reassignment Rate (%)']:.2f}%)\n"
            )
            f.write(f"Average Execution Time : {average_time:.4f} sec\n")

        print("\nSaved:")
        print(csv_path)
        print(txt_path)

        return report