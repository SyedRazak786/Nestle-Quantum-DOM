"""
home.py
--------------------------------
Executive Home Dashboard

Author: Syed Razak
"""

import streamlit as st


def show_home():

    # --------------------------------------------------
    # Hero Banner
    # --------------------------------------------------

    st.title("📦 Nestlé Quantum Distributed Order Management")

    st.markdown("""
### AI • Classical Optimization • Quantum Computing

**Enterprise Decision Support System for Smart Supply Chain Optimization**

This dashboard demonstrates an end-to-end Distributed Order Management (DOM)
solution that integrates Artificial Intelligence, Classical Optimization,
and Quantum Computing to improve inventory planning, customer order
fulfillment, and logistics decision-making.
""")

    st.success("✅ Version 1.0 | Phase 5 Completed | Enterprise Demo")

    st.divider()

    # --------------------------------------------------
    # Executive KPI Cards
    # --------------------------------------------------

    st.subheader("📊 Executive Dashboard")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("📦 Orders Processed", "5,036", "100%")

    with c2:
        st.metric("🤖 AI Accuracy", "96.76%", "R²")

    with c3:
        st.metric("⚙ Optimization Methods", "5", "Implemented")

    c4, c5, c6 = st.columns(3)

    with c4:
        st.metric("⚛ Quantum Solvers", "3", "Qiskit | PennyLane | Hybrid")

    with c5:
        st.metric("📄 Reports Generated", "12+", "Business Ready")

    with c6:
        st.metric("🏆 Project Status", "Completed", "Phase 5")

    st.divider()

    # --------------------------------------------------
    # Workflow
    # --------------------------------------------------

    st.subheader("🔄 Project Workflow")

    col = st.columns(7)

    workflow = [
        ("📂", "Raw Data"),
        ("📊", "Engineering"),
        ("🤖", "AI"),
        ("⚙", "Classical"),
        ("⚛", "Quantum"),
        ("📈", "Evaluation"),
        ("💼", "Business"),
    ]

    for c, (icon, label) in zip(col, workflow):
        with c:
            st.markdown(f"## {icon}")
            st.write(label)

    st.divider()

    # --------------------------------------------------
    # Quick Statistics
    # --------------------------------------------------

    st.subheader("📈 Quick Statistics")

    q1, q2 = st.columns(2)

    with q1:

        st.info("""
**Dataset**

• Total Records : 25,193

• Features : 81

• Training Samples : 20,143

• Testing Samples : 5,036
""")

    with q2:

        st.info("""
**Optimization**

• Classical Methods : 3

• Quantum Solvers : 3

• Benchmark Reports : Completed

• Dashboard : Active
""")

    st.divider()

    # --------------------------------------------------
    # Phase Completion
    # --------------------------------------------------

    st.subheader("✅ Project Completion")

    st.progress(100)

    phases = [
        "✅ Phase 1 – Data Engineering",
        "✅ Phase 2 – AI Prediction",
        "✅ Phase 3 – Classical Optimization",
        "✅ Phase 4 – Quantum Optimization",
        "✅ Phase 5 – Evaluation & Dashboard",
    ]

    for p in phases:
        st.success(p)

    st.divider()

    # --------------------------------------------------
    # Technology Stack
    # --------------------------------------------------

    st.subheader("🛠 Technology Stack")

    t1, t2, t3 = st.columns(3)

    with t1:
        st.info("""
### 🤖 Artificial Intelligence

• Python

• Pandas

• NumPy

• Scikit-Learn

• Random Forest
""")

    with t2:
        st.info("""
### ⚙ Optimization

• Default Assignment

• Greedy Algorithm

• Linear Programming
""")

    with t3:
        st.info("""
### ⚛ Quantum

• QUBO

• Qiskit

• PennyLane

• Hybrid Solver

• Streamlit
""")

    st.divider()

    # --------------------------------------------------
    # Business Benefits
    # --------------------------------------------------

    st.subheader("💼 Business Benefits")

    b1, b2 = st.columns(2)

    with b1:

        st.success("""
### 📦 Inventory Optimization

✔ Better demand forecasting

✔ Smart replenishment

✔ Reduced stock shortages

✔ Improved warehouse utilization
""")

        st.success("""
### 🚚 Logistics Optimization

✔ Faster fulfillment

✔ Lower transportation cost

✔ Reduced reassignment

✔ Better resource planning
""")

    with b2:

        st.success("""
### 📈 Decision Support

✔ AI-powered planning

✔ Executive dashboard

✔ Performance analytics

✔ Real-time insights
""")

        st.success("""
### 🌱 Sustainability

✔ Lower fuel consumption

✔ Reduced emissions

✔ Efficient logistics

✔ Future-ready supply chain
""")

    st.divider()

    # --------------------------------------------------
    # Project Objectives
    # --------------------------------------------------

    st.subheader("🎯 Project Objectives")

    st.info("""
✔ Reduce transportation cost

✔ Improve inventory utilization

✔ Optimize customer order assignment

✔ Improve demand forecasting

✔ Demonstrate Quantum Optimization

✔ Support executive decision-making
""")

    st.divider()

    # --------------------------------------------------
    # Architecture
    # --------------------------------------------------

    st.subheader("🏗 System Architecture")

    st.code("""
Customer Orders
        │
        ▼
Data Engineering
        │
        ▼
AI Prediction
        │
        ▼
Classical Optimization
        │
        ▼
Quantum Optimization
        │
        ▼
Benchmark & Reports
        │
        ▼
Business Strategy Dashboard
""", language="text")

    st.divider()

    # --------------------------------------------------
    # About
    # --------------------------------------------------

    st.subheader("ℹ About This Project")

    st.markdown("""
The **Nestlé Quantum Distributed Order Management (DOM)** project combines
Artificial Intelligence, Classical Optimization, and Quantum Computing
to improve logistics planning and supply chain operations.

The solution provides:

- AI-based demand forecasting
- Inventory prediction
- Classical optimization algorithms
- Quantum optimization using Qiskit & PennyLane
- Benchmarking and model comparison
- Business analytics and executive decision support

This project demonstrates how emerging quantum technologies can complement
traditional optimization methods for enterprise logistics.
""")

    st.divider()

    # --------------------------------------------------
    # Footer
    # --------------------------------------------------

    st.caption(
        "Developed by SYED RAZAK | B.Tech Computer Science | "
        "AI • Quantum Computing • Supply Chain Optimization | 2026"
    )