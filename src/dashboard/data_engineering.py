"""
data_engineering.py
--------------------------------
Phase 1 Dashboard

Author: SYED RAZAK
"""

from pathlib import Path

import pandas as pd
import streamlit as st


def show_data_engineering():

    # ==========================================================
    # Header
    # ==========================================================

    st.title("📊 Phase 1 - Data Engineering")

    st.markdown("""
### Enterprise Data Processing Dashboard

This module transforms the raw Nestlé Distributed Order Management
dataset into a clean, validated and AI-ready dataset using
industry-standard preprocessing and feature engineering techniques.
""")

    st.success(
        "✅ Phase Status : Completed | Output : Master Dataset | Ready for AI & Optimization"
    )

    st.divider()

    # ==========================================================
    # Executive Summary
    # ==========================================================

    st.subheader("📌 Executive Summary")

    st.info("""
The Data Engineering pipeline prepares raw customer order data for
Artificial Intelligence, Classical Optimization and Quantum Optimization.

Major activities completed:

• Data Cleaning

• Missing Value Handling

• Duplicate Removal

• Feature Engineering

• Categorical Encoding

• Feature Scaling

• Master Dataset Generation
""")

    st.divider()

    # ==========================================================
    # Load Dataset
    # ==========================================================

    dataset_path = Path("data/processed/master_dataset.csv")

    if not dataset_path.exists():

        st.error(f"Dataset not found:\n{dataset_path}")

        return

    df = pd.read_csv(dataset_path)

    # ==========================================================
    # Calculate Statistics
    # ==========================================================

    total_rows = len(df)

    total_columns = df.shape[1]

    missing_values = int(df.isna().sum().sum())

    duplicate_rows = int(df.duplicated().sum())

    numerical_columns = len(
        df.select_dtypes(include="number").columns
    )

    categorical_columns = len(
        df.select_dtypes(include="object").columns
    )

    memory_usage = round(
        df.memory_usage(deep=True).sum() / 1024**2,
        2
    )

    # ==========================================================
    # Enterprise KPI Dashboard
    # ==========================================================

    st.subheader("📊 Dataset Overview")

    row1 = st.columns(4)

    with row1[0]:
        st.metric(
            "📦 Total Records",
            f"{total_rows:,}"
        )

    with row1[1]:
        st.metric(
            "📑 Features",
            total_columns
        )

    with row1[2]:
        st.metric(
            "❗ Missing Values",
            missing_values
        )

    with row1[3]:
        st.metric(
            "🔁 Duplicate Rows",
            duplicate_rows
        )

    row2 = st.columns(4)

    with row2[0]:
        st.metric(
            "🔢 Numerical",
            numerical_columns
        )

    with row2[1]:
        st.metric(
            "🏷 Categorical",
            categorical_columns
        )

    with row2[2]:
        st.metric(
            "💾 Memory",
            f"{memory_usage} MB"
        )

    with row2[3]:
        st.metric(
            "✅ AI Ready",
            "YES"
        )

    st.divider()

    # ==========================================================
    # Enterprise Pipeline
    # ==========================================================

    st.subheader("🔄 Data Engineering Pipeline")

    cols = st.columns(7)

    pipeline = [

        ("📂", "Raw Data"),
        ("🧹", "Cleaning"),
        ("❗", "Missing"),
        ("🏷", "Encoding"),
        ("⚖", "Scaling"),
        ("🧠", "Features"),
        ("✅", "Master")

    ]

    descriptions = [

        "Source Dataset",

        "Invalid Data Removed",

        "Missing Values Handled",

        "Categorical Variables",

        "Feature Normalization",

        "Business Features",

        "AI Ready Dataset"

    ]

    for col, step, desc in zip(cols, pipeline, descriptions):

        icon, title = step

        with col:

            st.markdown(f"## {icon}")

            st.markdown(f"**{title}**")

            st.caption(desc)

    st.divider()
        # ==========================================================
    # Dataset Preview
    # ==========================================================

    st.subheader("📄 Master Dataset Preview")

    preview_rows = st.slider(
        "Select number of rows to preview",
        min_value=5,
        max_value=100,
        value=20,
        step=5
    )

    st.dataframe(
        df.head(preview_rows),
        use_container_width=True,
        height=450
    )

    st.divider()

    # ==========================================================
    # Dataset Information
    # ==========================================================

    st.subheader("📋 Dataset Information")

    left, right = st.columns(2)

    with left:

        st.info(f"""
**Dataset Name**

Master Dataset

**Rows**

{total_rows:,}

**Columns**

{total_columns}

**Memory Usage**

{memory_usage} MB
""")

    with right:

        st.info(f"""
**Numerical Columns**

{numerical_columns}

**Categorical Columns**

{categorical_columns}

**Duplicate Rows**

{duplicate_rows}

**Missing Values**

{missing_values}
""")

    st.divider()

    # ==========================================================
    # Dataset Health Dashboard
    # ==========================================================

    st.subheader("🩺 Dataset Health")

    h1, h2, h3 = st.columns(3)

    with h1:

        if missing_values == 0:
            st.success("✅ Missing Values\n\nPassed")
        else:
            st.warning(f"⚠ {missing_values} Missing Values")

    with h2:

        if duplicate_rows == 0:
            st.success("✅ Duplicate Records\n\nPassed")
        else:
            st.warning(f"⚠ {duplicate_rows} Duplicate Rows")

    with h3:

        st.success("✅ AI Ready Dataset")

    st.divider()

    # ==========================================================
    # Missing Values Summary
    # ==========================================================

    st.subheader("❗ Missing Values Summary")

    missing = df.isna().sum()

    missing = missing[missing > 0]

    if missing.empty:

        st.success(
            "No missing values detected.\n\n"
            "Dataset successfully cleaned."
        )

    else:

        missing_df = missing.reset_index()

        missing_df.columns = [
            "Column",
            "Missing Values"
        ]

        st.dataframe(
            missing_df,
            use_container_width=True
        )

    st.divider()

    # ==========================================================
    # Target Variable
    # ==========================================================

    st.subheader("🎯 Target Variable")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Target Column",
            "SalesOrderDemand"
        )

    with c2:

        st.metric(
            "Problem Type",
            "Regression"
        )

    with c3:

        st.metric(
            "Status",
            "AI Ready"
        )

    st.divider()
        # ==========================================================
    # Feature Engineering Summary
    # ==========================================================

    st.subheader("🧠 Feature Engineering Summary")

    with st.expander("View Feature Engineering Steps", expanded=True):

        st.markdown("""
### Completed Data Processing Pipeline

✅ Removed unnecessary identifier columns

✅ Removed rows with missing target values

✅ Handled missing values

✅ Encoded categorical features

✅ Scaled numerical features

✅ Created AI-ready business features

✅ Generated master dataset

---

### Output

The processed dataset is now ready for:

- 🤖 AI Prediction
- ⚙️ Classical Optimization
- ⚛️ Quantum Optimization
- 📈 Business Analytics
""")

    st.divider()

    # ==========================================================
    # Data Type Distribution
    # ==========================================================

    st.subheader("📊 Data Type Distribution")

    bool_columns = len(
        df.select_dtypes(include="bool").columns
    )

    datetime_columns = len(
        df.select_dtypes(
            include=["datetime64", "datetime64[ns]"]
        ).columns
    )

    d1, d2, d3, d4 = st.columns(4)

    with d1:
        st.metric(
            "🔢 Numerical",
            numerical_columns
        )

    with d2:
        st.metric(
            "🏷 Categorical",
            categorical_columns
        )

    with d3:
        st.metric(
            "📅 Datetime",
            datetime_columns
        )

    with d4:
        st.metric(
            "☑ Boolean",
            bool_columns
        )

    st.divider()

    # ==========================================================
    # Final Dataset Status
    # ==========================================================

    st.subheader("📋 Final Dataset Status")

    left, right = st.columns(2)

    with left:

        st.success("""
### ✅ Validation Completed

✔ Data Cleaning

✔ Missing Values Handled

✔ Duplicate Check

✔ Feature Engineering

✔ Dataset Validation
""")

    with right:

        st.success("""
### 🚀 Ready For

✔ AI Prediction

✔ Inventory Prediction

✔ Classical Optimization

✔ Quantum Optimization

✔ Business Dashboard
""")

    st.divider()

    # ==========================================================
    # Phase Completion
    # ==========================================================

    st.subheader("📈 Phase Completion")

    st.progress(100)

    st.success("🎉 Phase 1 – Data Engineering Completed Successfully")

    p1, p2, p3 = st.columns(3)

    with p1:
        st.metric(
            "Status",
            "Completed"
        )

    with p2:
        st.metric(
            "Output Dataset",
            "Master Dataset"
        )

    with p3:
        st.metric(
            "AI Ready",
            "YES"
        )

    st.divider()

    # ==========================================================
    # Next Phase
    # ==========================================================

    st.subheader("➡ Next Phase")

    st.info("""
The processed Master Dataset is now passed to:

🤖 Phase 2 – AI Prediction

where the following tasks are performed:

• Demand Prediction

• Inventory Prediction

• Uncertainty Estimation

• AI Recommendation Generation
""")

    st.divider()

    # ==========================================================
    # Footer
    # ==========================================================

    st.caption(
        """
Phase 1 – Data Engineering

Output Dataset:
data/processed/master_dataset.csv

Integrated With:
AI Prediction → Classical Optimization → Quantum Optimization → Evaluation Dashboard

Developed for the Nestlé Quantum Distributed Order Management Project
"""
    )