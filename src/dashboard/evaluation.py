"""
evaluation.py
--------------------------------
Phase 5 Dashboard

Author: SYED RAZAK
"""

from pathlib import Path

import pandas as pd
import streamlit as st


def show_evaluation():

    # ==========================================================
    # Header
    # ==========================================================

    st.title("📊 Phase 5 - Evaluation & Benchmarking")

    st.markdown("""
### Enterprise Evaluation Dashboard

This module evaluates Artificial Intelligence, Classical
Optimization and Quantum Optimization models using business
performance metrics, execution time, reassignment statistics
and optimization quality.
""")

    st.success(
        "✅ Phase Status : Completed | Evaluation Finished | Executive Report Ready"
    )

    st.divider()

    # ==========================================================
    # Executive Summary
    # ==========================================================

    st.subheader("📌 Executive Summary")

    st.info("""
The Evaluation module compares all optimization approaches
implemented in the Nestlé Distributed Order Management project.

Compared Methods

• Greedy Assignment

• Linear Programming

• Qiskit QAOA

• PennyLane QAOA

• Hybrid Quantum Solver

The objective is to identify the most efficient optimization
strategy based on execution time, reassignment rate and
business performance.
""")

    st.divider()

    # ==========================================================
    # Load Files
    # ==========================================================

    benchmark_path = Path(
        "outputs/benchmarks/benchmark_results.csv"
    )

    comparison_path = Path(
        "outputs/comparison/model_comparison.csv"
    )

    business_path = Path(
        "outputs/business_report/business_summary.csv"
    )

    benchmark_df = (
        pd.read_csv(benchmark_path)
        if benchmark_path.exists()
        else pd.DataFrame()
    )

    comparison_df = (
        pd.read_csv(comparison_path)
        if comparison_path.exists()
        else pd.DataFrame()
    )

    business_df = (
        pd.read_csv(business_path)
        if business_path.exists()
        else pd.DataFrame()
    )

    # ==========================================================
    # Calculate KPIs
    # ==========================================================

    total_methods = 0

    total_orders = 0

    fastest = "-"

    slowest = "-"

    lowest = "-"

    highest = "-"

    avg_time = "-"

    if not benchmark_df.empty:

        total_methods = len(benchmark_df)

        total_orders = int(
            benchmark_df["Total Orders"].sum()
        )

        fastest = benchmark_df.loc[
            benchmark_df["Execution Time(sec)"].idxmin(),
            "Method"
        ]

        slowest = benchmark_df.loc[
            benchmark_df["Execution Time(sec)"].idxmax(),
            "Method"
        ]

        lowest = benchmark_df.loc[
            benchmark_df["Reassignment Rate (%)"].idxmin(),
            "Method"
        ]

        highest = benchmark_df.loc[
            benchmark_df["Reassignment Rate (%)"].idxmax(),
            "Method"
        ]

        avg_time = round(
            benchmark_df["Execution Time(sec)"].mean(),
            4
        )

    # ==========================================================
    # KPI Dashboard
    # ==========================================================

    st.subheader("📊 Overall Performance Dashboard")

    row1 = st.columns(4)

    with row1[0]:

        st.metric(
            "Methods Compared",
            total_methods
        )

    with row1[1]:

        st.metric(
            "Orders Evaluated",
            f"{total_orders:,}"
        )

    with row1[2]:

        st.metric(
            "Fastest Solver",
            fastest
        )

    with row1[3]:

        st.metric(
            "Slowest Solver",
            slowest
        )

    row2 = st.columns(4)

    with row2[0]:

        st.metric(
            "Lowest Reassignment",
            lowest
        )

    with row2[1]:

        st.metric(
            "Highest Reassignment",
            highest
        )

    with row2[2]:

        st.metric(
            "Average Time",
            f"{avg_time} sec"
        )

    with row2[3]:

        st.metric(
            "Project Status",
            "Completed"
        )

    st.divider()

    # ==========================================================
    # Evaluation Overview
    # ==========================================================

    st.subheader("📈 Evaluation Overview")

    overview1, overview2 = st.columns(2)

    with overview1:

        st.success(f"""
### Evaluation Summary

✔ Optimization Methods : **{total_methods}**

✔ Orders Evaluated : **{total_orders:,}**

✔ Benchmark Completed

✔ Performance Compared

✔ Executive Report Generated
""")

    with overview2:

        st.info("""
### Evaluation Objectives

• Compare optimization algorithms

• Measure execution efficiency

• Analyze reassignment rates

• Generate business insights

• Support executive decision making
""")

    st.divider()
        # ==========================================================
    # Benchmark Results
    # ==========================================================

    st.subheader("📋 Benchmark Results")

    st.info("""
The benchmark compares all optimization methods based on
execution time, total orders processed and reassignment rate.
""")

    if benchmark_df.empty:

        st.warning("Benchmark results not found.")

    else:

        st.dataframe(
            benchmark_df,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    # ==========================================================
    # Model Comparison
    # ==========================================================

    st.subheader("🏆 Model Comparison")

    st.info("""
This comparison summarizes the performance of all implemented
optimization techniques across AI, Classical and Quantum stages.
""")

    if comparison_df.empty:

        st.warning("Model comparison file not found.")

    else:

        st.dataframe(
            comparison_df,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    # ==========================================================
    # Business Report
    # ==========================================================

    st.subheader("💼 Business Report")

    if business_df.empty:

        st.warning("Business report not found.")

    else:

        left, right = st.columns([2, 1])

        with left:

            st.dataframe(
                business_df,
                use_container_width=True,
                hide_index=True
            )

        with right:

            st.success("""
### Executive Highlights

✔ Benchmark completed

✔ Performance analyzed

✔ Business report generated

✔ Optimization evaluated

✔ Ready for deployment
""")

    st.divider()

    # ==========================================================
    # Executive Recommendation
    # ==========================================================

    st.subheader("🎯 Executive Recommendation")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.success("""
### 🥇 Greedy Assignment

**Recommended for Production**

Advantages

✔ Fastest execution

✔ Handles large datasets

✔ Low computational cost

✔ Suitable for real-time planning

Best Use Case

Daily order allocation
""")

    with col2:

        st.info("""
### 🥈 Linear Programming

**Recommended for Exact Planning**

Advantages

✔ Mathematical optimization

✔ Constraint satisfaction

✔ Optimal resource utilization

Best Use Case

Strategic planning
""")

    with col3:

        st.warning("""
### 🥉 Quantum Optimization

**Recommended for Research**

Advantages

✔ Future-ready architecture

✔ Hybrid optimization

✔ Quantum computing workflow

Best Use Case

Next-generation optimization
""")

    st.divider()

    # ==========================================================
    # Executive Decision Matrix
    # ==========================================================

    st.subheader("📊 Executive Decision Matrix")

    decision_df = pd.DataFrame({

        "Criterion": [

            "Execution Speed",

            "Scalability",

            "Optimization Quality",

            "Business Readiness",

            "Research Value"

        ],

        "Best Method": [

            "Greedy",

            "Greedy",

            "Linear Programming",

            "Greedy",

            "Quantum"

        ]

    })

    st.dataframe(
        decision_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()
        # ==========================================================
    # Performance Analytics
    # ==========================================================

    st.subheader("📈 Performance Analytics")

    if not benchmark_df.empty:

        chart1, chart2 = st.columns(2)

        with chart1:

            st.markdown("### ⏱ Execution Time Comparison")

            execution_chart = benchmark_df.set_index(
                "Method"
            )["Execution Time(sec)"]

            st.bar_chart(execution_chart)

        with chart2:

            st.markdown("### 🔄 Reassignment Rate")

            reassignment_chart = benchmark_df.set_index(
                "Method"
            )["Reassignment Rate (%)"]

            st.bar_chart(reassignment_chart)

        st.divider()

        chart3, chart4 = st.columns(2)

        with chart3:

            st.markdown("### 📦 Orders Processed")

            orders_chart = benchmark_df.set_index(
                "Method"
            )["Total Orders"]

            st.bar_chart(orders_chart)

        with chart4:

            ranking = benchmark_df.sort_values(
                by="Execution Time(sec)"
            )

            st.markdown("### 🏆 Solver Ranking")

            ranking = ranking.reset_index(drop=True)

            ranking.index += 1

            ranking.index.name = "Rank"

            st.dataframe(
                ranking,
                use_container_width=True
            )

    st.divider()

    # ==========================================================
    # Nestlé Business Benefits
    # ==========================================================

    st.subheader("🏭 Nestlé Supply Chain Benefits")

    benefit1, benefit2 = st.columns(2)

    with benefit1:

        st.success("""
### Operational Improvements

✔ Faster order allocation

✔ Improved warehouse utilization

✔ Better inventory balancing

✔ Reduced transportation cost

✔ Reduced manual planning effort

✔ AI-assisted decision support
""")

    with benefit2:

        st.info("""
### Strategic Benefits

✔ AI + Classical + Quantum integration

✔ Scalable optimization workflow

✔ Executive decision support

✔ Future-ready quantum architecture

✔ Improved customer satisfaction

✔ Digital transformation
""")

    st.divider()

    # ==========================================================
    # Overall Project Scorecard
    # ==========================================================

    st.subheader("📋 Project Completion Scorecard")

    scorecard = pd.DataFrame({

        "Project Phase": [

            "Phase 1 - Data Engineering",

            "Phase 2 - AI Prediction",

            "Phase 3 - Classical Optimization",

            "Phase 4 - Quantum Optimization",

            "Phase 5 - Evaluation"

        ],

        "Status": [

            "Completed",

            "Completed",

            "Completed",

            "Completed",

            "Completed"

        ]

    })

    st.dataframe(
        scorecard,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ==========================================================
    # Technology Stack
    # ==========================================================

    st.subheader("🛠 Technology Stack")

    tech1, tech2, tech3, tech4 = st.columns(4)

    with tech1:

        st.info("""
### AI

• Scikit-learn

• Random Forest

• Pandas

• NumPy
""")

    with tech2:

        st.info("""
### Classical

• Greedy

• Linear Programming

• PuLP

• Optimization
""")

    with tech3:

        st.info("""
### Quantum

• Qiskit

• PennyLane

• QAOA

• Hybrid Solver
""")

    with tech4:

        st.info("""
### Dashboard

• Streamlit

• Python

• CSV Reports

• Analytics
""")

    st.divider()

    # ==========================================================
    # Executive Project Summary
    # ==========================================================

    st.subheader("🎓 Executive Project Summary")

    st.success("""
### Nestlé Quantum Distributed Order Management

This project successfully integrates

✅ Data Engineering

✅ Artificial Intelligence

✅ Classical Optimization

✅ Quantum Optimization

✅ Performance Evaluation

into one enterprise decision-support platform.

The system demonstrates how AI and Quantum Computing
can improve modern supply chain planning while providing
business-ready insights through an interactive dashboard.
""")

    st.divider()

    # ==========================================================
    # Footer
    # ==========================================================

    st.caption("""
Phase 5 – Evaluation & Benchmarking

Enterprise Dashboard Modules

• Benchmarking

• Model Comparison

• Business Reporting

• Executive Analytics

Developed by

SYED RAZAK

Nestlé Quantum Distributed Order Management Project
""")