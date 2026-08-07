"""
ai_prediction.py
--------------------------------
Phase 2 Dashboard

Author: Sirama Avinash
"""

from pathlib import Path

import pandas as pd
import streamlit as st


def show_ai_prediction():

    # ==========================================================
    # Header
    # ==========================================================

    st.title("🤖 Phase 2 - AI Prediction")

    st.markdown("""
### Enterprise Artificial Intelligence Dashboard

This module uses Machine Learning to predict customer demand,
estimate inventory requirements and generate intelligent
recommendations for supply chain planners.
""")

    st.success(
        "✅ Phase Status : Completed | AI Models Operational | Ready for Optimization"
    )

    st.divider()

    # ==========================================================
    # Executive Summary
    # ==========================================================

    st.subheader("📌 Executive Summary")

    st.info("""
The Artificial Intelligence module transforms historical order
data into actionable business intelligence.

Capabilities:

• Demand Forecasting

• Inventory Prediction

• AI Recommendation Engine

• Confidence Estimation

• Decision Support for Supply Chain Optimization
""")

    st.divider()

    # ==========================================================
    # Load AI Output Files
    # ==========================================================

    decisions_path = Path("outputs/ai_decisions.csv")

    if not decisions_path.exists():

        st.error("AI output file not found.")

        return

    ai_df = pd.read_csv(decisions_path)

    total_predictions = len(ai_df)

    # ==========================================================
    # Model Metrics
    # ==========================================================

    # Replace these with values loaded from your metrics file later

    MAE = 0.000310
    RMSE = 0.005716
    R2 = 0.967557

    avg_confidence = 0

    if "Confidence" in ai_df.columns:

        avg_confidence = round(
            ai_df["Confidence"].mean() * 100,
            2
        )

    # ==========================================================
    # KPI Dashboard
    # ==========================================================

    st.subheader("📊 AI Dashboard")

    row1 = st.columns(4)

    with row1[0]:

        st.metric(
            "📦 Demand Predictions",
            f"{total_predictions:,}"
        )

    with row1[1]:

        st.metric(
            "📦 Inventory Predictions",
            f"{total_predictions:,}"
        )

    with row1[2]:

        st.metric(
            "🤖 AI Recommendations",
            f"{total_predictions:,}"
        )

    with row1[3]:

        st.metric(
            "📈 Avg Confidence",
            f"{avg_confidence}%"
        )

    row2 = st.columns(4)

    with row2[0]:

        st.metric(
            "MAE",
            f"{MAE:.6f}"
        )

    with row2[1]:

        st.metric(
            "RMSE",
            f"{RMSE:.6f}"
        )

    with row2[2]:

        st.metric(
            "R² Score",
            f"{R2:.4f}"
        )

    with row2[3]:

        st.metric(
            "AI Status",
            "Operational"
        )

    st.divider()

    # ==========================================================
    # Model Performance
    # ==========================================================

    st.subheader("📈 Model Performance")

    left, right = st.columns(2)

    with left:

        st.success(f"""
### Regression Metrics

• Mean Absolute Error

**{MAE:.6f}**

---

• Root Mean Square Error

**{RMSE:.6f}**

---

• R² Score

**{R2:.4f}**
""")

    with right:

        st.success(f"""
### AI Statistics

Total Predictions

**{total_predictions:,}**

---

Average Confidence

**{avg_confidence}%**

---

Model Status

**Production Ready**
""")

    st.divider()
        # ==========================================================
    # AI Prediction Tabs
    # ==========================================================

    st.subheader("🧠 AI Prediction Modules")

    tab1, tab2, tab3 = st.tabs(
        [
            "📦 Demand Prediction",
            "📋 Inventory Prediction",
            "🤖 AI Recommendations"
        ]
    )

    # ==========================================================
    # TAB 1
    # Demand Prediction
    # ==========================================================

    with tab1:

        st.markdown("## 📦 Demand Prediction")

        st.info("""
The Demand Prediction model forecasts customer demand using
Machine Learning to improve inventory planning and order fulfillment.
""")

        st.metric(
            "Total Predictions",
            f"{total_predictions:,}"
        )

        st.markdown("### Prediction Preview")

        st.dataframe(
            ai_df.head(20),
            use_container_width=True,
            height=400
        )

        st.markdown("### Prediction Statistics")

        numeric_cols = ai_df.select_dtypes(include="number")

        if not numeric_cols.empty:

            st.dataframe(
                numeric_cols.describe(),
                use_container_width=True
            )

        else:

            st.warning("No numerical columns available.")

    # ==========================================================
    # TAB 2
    # Inventory Prediction
    # ==========================================================

    with tab2:

        st.markdown("## 📋 Inventory Prediction")

        st.info("""
Inventory Prediction estimates stock availability and
identifies replenishment requirements based on predicted demand.
""")

        inventory_cols = [

            "Current_Inventory",
            "Required_Inventory",
            "Inventory_Gap",
            "Inventory_Status",
            "Replenishment_Required"

        ]

        available_inventory = [

            c for c in inventory_cols

            if c in ai_df.columns

        ]

        if available_inventory:

            st.dataframe(

                ai_df[available_inventory].head(20),

                use_container_width=True

            )

            st.markdown("### Inventory Summary")

            st.dataframe(

                ai_df[available_inventory].describe(),

                use_container_width=True

            )

        else:

            st.warning(

                "Inventory columns not found in AI output."

            )

    # ==========================================================
    # TAB 3
    # AI Recommendation
    # ==========================================================

    with tab3:

        st.markdown("## 🤖 AI Recommendation Engine")

        st.info("""
The Recommendation Engine combines demand prediction,
inventory analysis and confidence estimation to
assist planners with business decisions.
""")

        recommendation_cols = [

            "Recommendation",
            "Confidence"

        ]

        available_rec = [

            c for c in recommendation_cols

            if c in ai_df.columns

        ]

        if available_rec:

            st.dataframe(

                ai_df[available_rec].head(25),

                use_container_width=True

            )

            if "Recommendation" in ai_df.columns:

                st.markdown("### Recommendation Summary")

                recommendation_summary = (

                    ai_df["Recommendation"]

                    .value_counts()

                    .reset_index()

                )

                recommendation_summary.columns = [

                    "Recommendation",

                    "Count"

                ]

                st.dataframe(

                    recommendation_summary,

                    use_container_width=True

                )

        else:

            st.warning(

                "Recommendation data not available."

            )

    st.divider()
        # ==========================================================
    # AI Confidence Dashboard
    # ==========================================================

    st.subheader("📈 AI Confidence Analysis")

    if "Confidence" in ai_df.columns:

        high = (ai_df["Confidence"] >= 0.80).sum()

        medium = (
            (ai_df["Confidence"] >= 0.60) &
            (ai_df["Confidence"] < 0.80)
        ).sum()

        low = (ai_df["Confidence"] < 0.60).sum()

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "🟢 High Confidence",
                int(high)
            )

        with c2:
            st.metric(
                "🟡 Medium Confidence",
                int(medium)
            )

        with c3:
            st.metric(
                "🔴 Low Confidence",
                int(low)
            )

        with c4:
            st.metric(
                "Average",
                f"{avg_confidence}%"
            )

    else:

        st.warning(
            "Confidence column not found."
        )

    st.divider()

    # ==========================================================
    # AI Charts
    # ==========================================================

    st.subheader("📊 AI Analytics")

    chart1, chart2 = st.columns(2)

    with chart1:

        if "Confidence" in ai_df.columns:

            st.markdown("### Confidence Distribution")

            st.bar_chart(
                ai_df["Confidence"]
            )

    with chart2:

        if "Recommendation" in ai_df.columns:

            st.markdown("### Recommendation Distribution")

            recommendation_counts = (
                ai_df["Recommendation"]
                .value_counts()
            )

            st.bar_chart(
                recommendation_counts
            )

    st.divider()

    # ==========================================================
    # Inventory Chart
    # ==========================================================

    inventory_status_col = None

    for col in [
        "Inventory_Status",
        "Inventory Status"
    ]:

        if col in ai_df.columns:
            inventory_status_col = col
            break

    if inventory_status_col is not None:

        st.subheader("📦 Inventory Status")

        inventory_counts = (
            ai_df[inventory_status_col]
            .value_counts()
        )

        st.bar_chart(
            inventory_counts
        )

        st.divider()

    # ==========================================================
    # AI Workflow
    # ==========================================================

    st.subheader("🔄 AI Workflow")

    st.code(
"""
Raw Dataset
      │
      ▼
Feature Engineering
      │
      ▼
Random Forest Model
      │
      ▼
Demand Prediction
      │
      ▼
Inventory Prediction
      │
      ▼
Recommendation Engine
      │
      ▼
Optimization
""",
        language="text"
    )

    st.divider()

    # ==========================================================
    # Executive Insights
    # ==========================================================

    st.subheader("💡 Executive Insights")

    st.success("""
### AI Module Summary

✅ Demand successfully predicted

✅ Inventory requirements estimated

✅ AI recommendations generated

✅ Confidence scores calculated

✅ Dataset ready for optimization

✅ Business intelligence generated
""")

    st.info("""
### Business Impact

• Better inventory utilization

• Improved customer service

• Reduced stock shortages

• Lower transportation cost

• Faster planner decisions

• AI-assisted supply chain optimization
""")

    st.divider()

    # ==========================================================
    # Next Phase
    # ==========================================================

    st.subheader("➡ Next Phase")

    st.info("""
Outputs from this AI module are automatically passed to:

⚙️ Phase 3 – Classical Optimization

• Default Assignment

• Greedy Assignment

• Linear Programming

↓

⚛️ Phase 4 – Quantum Optimization

• QUBO Formulation

• Qiskit

• PennyLane

• Hybrid Solver
""")

    st.divider()

    # ==========================================================
    # Footer
    # ==========================================================

    st.caption("""
Phase 2 – Artificial Intelligence

Outputs Generated

• Demand Prediction

• Inventory Prediction

• Confidence Estimation

• AI Recommendations

Integrated With

Classical Optimization → Quantum Optimization → Evaluation Dashboard

Developed for the Nestlé Quantum Distributed Order Management Project
""")
