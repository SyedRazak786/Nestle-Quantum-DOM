"""
classical.py
--------------------------------
Phase 3 Dashboard

Author: SYED RAZAK
"""

from pathlib import Path

import pandas as pd
import streamlit as st


def show_classical():

    # ==========================================================
    # Header
    # ==========================================================

    st.title("⚙️ Phase 3 - Classical Optimization")

    st.markdown("""
### Enterprise Classical Optimization Dashboard

This module applies classical optimization techniques to allocate
customer orders across distribution centers while minimizing
transportation cost and improving inventory utilization.
""")

    st.success(
        "✅ Phase Status : Completed | Classical Solvers Operational | Ready for Quantum Optimization"
    )

    st.divider()

    # ==========================================================
    # Executive Summary
    # ==========================================================

    st.subheader("📌 Executive Summary")

    st.info("""
The Classical Optimization module determines efficient order
assignments using three optimization approaches.

Implemented Solvers

• Default Assignment

• Greedy Assignment

• Linear Programming

The optimized assignments become the baseline for Quantum
Optimization in the next phase.
""")

    st.divider()

    # ==========================================================
    # Load Output Files
    # ==========================================================

    default_path = Path("outputs/default_assignment.csv")
    greedy_path = Path("outputs/greedy_assignment.csv")
    lp_path = Path("outputs/linear_programming.csv")
    benchmark_path = Path("outputs/benchmarks/benchmark_results.csv")

    default_df = pd.read_csv(default_path) if default_path.exists() else pd.DataFrame()
    greedy_df = pd.read_csv(greedy_path) if greedy_path.exists() else pd.DataFrame()
    lp_df = pd.read_csv(lp_path) if lp_path.exists() else pd.DataFrame()

    benchmark_df = (
        pd.read_csv(benchmark_path)
        if benchmark_path.exists()
        else pd.DataFrame()
    )

    # ==========================================================
    # Calculate Statistics
    # ==========================================================

    total_default = len(default_df)
    total_greedy = len(greedy_df)
    total_lp = len(lp_df)

    total_orders = max(
        total_default,
        total_greedy,
        total_lp
    )

    total_assignments = (
        total_default +
        total_greedy +
        total_lp
    )

    execution_time = "-"

    reassignment_rate = "-"

    if not benchmark_df.empty:

        classical = benchmark_df[
            benchmark_df["Method"] == "Greedy"
        ]

        if not classical.empty:

            execution_time = (
                classical.iloc[0]["Execution Time(sec)"]
            )

            reassignment_rate = (
                classical.iloc[0]["Reassignment Rate (%)"]
            )

    # ==========================================================
    # Enterprise KPI Dashboard
    # ==========================================================

    st.subheader("📊 Optimization Dashboard")

    row1 = st.columns(4)

    with row1[0]:

        st.metric(
            "📦 Orders",
            f"{total_orders:,}"
        )

    with row1[1]:

        st.metric(
            "📌 Default",
            total_default
        )

    with row1[2]:

        st.metric(
            "⚡ Greedy",
            total_greedy
        )

    with row1[3]:

        st.metric(
            "📈 LP",
            total_lp
        )

    row2 = st.columns(4)

    with row2[0]:

        st.metric(
            "Assignments",
            total_assignments
        )

    with row2[1]:

        st.metric(
            "Reassignment %",
            reassignment_rate
        )

    with row2[2]:

        st.metric(
            "Execution Time",
            execution_time
        )

    with row2[3]:

        st.metric(
            "Status",
            "Operational"
        )

    st.divider()

    # ==========================================================
    # Solver Performance
    # ==========================================================

    st.subheader("📈 Solver Performance Summary")

    if benchmark_df.empty:

        st.warning(
            "Benchmark results not found."
        )

    else:

        st.dataframe(
            benchmark_df[
                [
                    "Method",
                    "Total Orders",
                    "Reassignment Rate (%)",
                    "Execution Time(sec)"
                ]
            ],
            use_container_width=True,
            hide_index=True
        )

    st.divider()
        # ==========================================================
    # Classical Optimization Tabs
    # ==========================================================

    st.subheader("⚙️ Classical Optimization Modules")

    tab1, tab2, tab3 = st.tabs(
        [
            "📌 Default Assignment",
            "⚡ Greedy Assignment",
            "📈 Linear Programming"
        ]
    )

    # ==========================================================
    # TAB 1 : Default Assignment
    # ==========================================================

    with tab1:

        st.markdown("## 📌 Default Assignment")

        st.info("""
The Default Assignment algorithm assigns customer orders using
the initial business rules without optimization. It serves as
the baseline for comparing optimization techniques.
""")

        st.metric(
            "Orders Assigned",
            f"{len(default_df):,}"
        )

        if default_df.empty:

            st.warning("Default Assignment output not found.")

        else:

            st.dataframe(
                default_df.head(25),
                use_container_width=True,
                height=450
            )

            st.markdown("### Assignment Statistics")

            numeric = default_df.select_dtypes(include="number")

            if not numeric.empty:

                st.dataframe(
                    numeric.describe(),
                    use_container_width=True
                )

            st.success("""
### Business Notes

• Initial allocation strategy

• No optimization performed

• Used as benchmark for comparison
""")

    # ==========================================================
    # TAB 2 : Greedy Assignment
    # ==========================================================

    with tab2:

        st.markdown("## ⚡ Greedy Assignment")

        st.info("""
The Greedy algorithm iteratively selects the locally optimal
assignment for each customer order while considering available
inventory and transportation costs.
""")

        st.metric(
            "Orders Optimized",
            f"{len(greedy_df):,}"
        )

        if greedy_df.empty:

            st.warning("Greedy Assignment output not found.")

        else:

            st.dataframe(
                greedy_df.head(25),
                use_container_width=True,
                height=450
            )

            st.markdown("### Assignment Statistics")

            numeric = greedy_df.select_dtypes(include="number")

            if not numeric.empty:

                st.dataframe(
                    numeric.describe(),
                    use_container_width=True
                )

            left, right = st.columns(2)

            with left:

                st.success("""
### Advantages

✔ Fast execution

✔ Low computational cost

✔ Good practical performance

✔ Easy implementation
""")

            with right:

                st.warning("""
### Limitations

• May not reach global optimum

• Depends on local decisions

• Sensitive to assignment order
""")

    # ==========================================================
    # TAB 3 : Linear Programming
    # ==========================================================

    with tab3:

        st.markdown("## 📈 Linear Programming")

        st.info("""
Linear Programming finds the mathematically optimal assignment
while satisfying capacity, demand and business constraints.
""")

        st.metric(
            "Orders Optimized",
            f"{len(lp_df):,}"
        )

        if lp_df.empty:

            st.warning("Linear Programming output not found.")

        else:

            st.dataframe(
                lp_df.head(25),
                use_container_width=True,
                height=450
            )

            st.markdown("### Optimization Statistics")

            numeric = lp_df.select_dtypes(include="number")

            if not numeric.empty:

                st.dataframe(
                    numeric.describe(),
                    use_container_width=True
                )

            left, right = st.columns(2)

            with left:

                st.success("""
### Business Benefits

✔ Cost minimization

✔ Capacity optimization

✔ Balanced resource utilization

✔ Constraint satisfaction
""")

            with right:

                st.info("""
### Solver Characteristics

• Mathematical optimization

• Exact optimization approach

• Suitable for medium-scale planning

• Higher computational effort
""")

    st.divider()
        # ==========================================================
    # Reassignment Analytics
    # ==========================================================

    st.subheader("📊 Reassignment Analytics")

    if not benchmark_df.empty:

        greedy_data = benchmark_df[
            benchmark_df["Method"] == "Greedy"
        ]

        lp_data = benchmark_df[
            benchmark_df["Method"] == "Linear Programming"
        ]

        greedy_rate = 0.0
        lp_rate = 0.0

        if not greedy_data.empty:
            greedy_rate = float(
                greedy_data.iloc[0]["Reassignment Rate (%)"]
            )

        if not lp_data.empty:
            lp_rate = float(
                lp_data.iloc[0]["Reassignment Rate (%)"]
            )

        reassigned_orders = int(
            total_orders * greedy_rate / 100
        )

        stable_orders = total_orders - reassigned_orders

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "📦 Total Orders",
                f"{total_orders:,}"
            )

        with c2:
            st.metric(
                "🔄 Reassigned",
                f"{reassigned_orders:,}"
            )

        with c3:
            st.metric(
                "✅ Stable",
                f"{stable_orders:,}"
            )

        with c4:
            st.metric(
                "📈 Reassignment %",
                f"{greedy_rate:.2f}%"
            )

    st.divider()

    # ==========================================================
    # Analytics Charts
    # ==========================================================

    st.subheader("📈 Optimization Analytics")

    chart1, chart2 = st.columns(2)

    with chart1:

        st.markdown("### Orders Processed")

        orders_chart = pd.DataFrame({

            "Orders": [

                total_default,

                total_greedy,

                total_lp

            ]

        },

        index=[

            "Default",

            "Greedy",

            "Linear Programming"

        ])

        st.bar_chart(orders_chart)

    with chart2:

        if not benchmark_df.empty:

            st.markdown("### Execution Time")

            execution_chart = benchmark_df.set_index(
                "Method"
            )["Execution Time(sec)"]

            st.bar_chart(execution_chart)

    st.divider()

    chart3, chart4 = st.columns(2)

    with chart3:

        if not benchmark_df.empty:

            st.markdown("### Reassignment Rate")

            reassignment_chart = benchmark_df.set_index(
                "Method"
            )["Reassignment Rate (%)"]

            st.bar_chart(reassignment_chart)

    with chart4:

        if not benchmark_df.empty:

            st.markdown("### Solver Comparison")

            comparison = benchmark_df.set_index("Method")[
                [
                    "Total Orders",
                    "Execution Time(sec)"
                ]
            ]

            st.dataframe(
                comparison,
                use_container_width=True
            )

    st.divider()

    # ==========================================================
    # Optimization Workflow
    # ==========================================================

    st.subheader("🔄 Classical Optimization Workflow")

    st.code(
"""
AI Prediction
      │
      ▼
Default Assignment
      │
      ▼
Greedy Optimization
      │
      ▼
Linear Programming
      │
      ▼
Optimized Assignment
      │
      ▼
Quantum Optimization
""",
        language="text"
    )

    st.divider()

    # ==========================================================
    # Executive Business Insights
    # ==========================================================

    st.subheader("💼 Executive Business Insights")

    st.success("""
### Optimization Achievements

✅ Customer orders successfully assigned

✅ Warehouse capacity considered

✅ Transportation planning improved

✅ Resource utilization optimized

✅ Classical optimization completed successfully
""")

    st.info("""
### Business Benefits

• Faster order allocation

• Reduced transportation cost

• Better inventory balancing

• Improved warehouse utilization

• Lower manual planning effort

• Optimization-ready dataset for quantum solvers
""")

    st.divider()

    # ==========================================================
    # Next Phase
    # ==========================================================

    st.subheader("➡ Next Phase")

    st.info("""
Outputs from Classical Optimization are forwarded to

⚛️ Phase 4 – Quantum Optimization

Implemented Modules

• QUBO Formulation

• Constraint Builder

• Objective Function

• Qiskit Solver

• PennyLane Solver

• Hybrid Quantum Solver
""")

    st.divider()

    # ==========================================================
    # Footer
    # ==========================================================

    st.caption("""
Phase 3 – Classical Optimization

Algorithms Implemented

• Default Assignment

• Greedy Assignment

• Linear Programming

Integrated With

AI Prediction → Quantum Optimization → Evaluation Dashboard

Developed for the Nestlé Quantum Distributed Order Management Project
""")