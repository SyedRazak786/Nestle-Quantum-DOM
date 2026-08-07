"""
downloads.py
--------------------------------
Phase H Dashboard

Enterprise Reporting & Downloads Center

Author: SYED RAZAK
"""

from pathlib import Path
import streamlit as st


def show_downloads():

    # ==========================================================
    # Header
    # ==========================================================

    st.title("📥 Enterprise Reporting & Downloads Center")

    st.markdown("""
## Nestlé Quantum Distributed Order Management

Centralized reporting hub for downloading datasets,
AI outputs, optimization results, quantum solutions,
evaluation reports and executive summaries.
""")

    st.success(
        "✅ Dashboard Status : Completed | Reports Ready for Export"
    )

    st.divider()


    # ==========================================================
    # Export Summary
    # ==========================================================

    st.subheader("📌 Export Summary")


    summary1, summary2, summary3, summary4 = st.columns(4)


    with summary1:

        st.metric(
            "Project",
            "Nestlé Quantum DOM"
        )


    with summary2:

        st.metric(
            "Completed Phases",
            "8"
        )


    with summary3:

        st.metric(
            "Report Categories",
            "6"
        )


    with summary4:

        st.metric(
            "Status",
            "Ready"
        )


    st.divider()


    # ==========================================================
    # Reporting Categories Overview
    # ==========================================================

    st.subheader("📊 Available Reports")


    report_df = {

        "Category": [

            "Data Engineering",

            "AI Prediction",

            "Classical Optimization",

            "Quantum Optimization",

            "Evaluation",

            "Business Strategy"

        ],

        "Status": [

            "Available",

            "Available",

            "Available",

            "Available",

            "Available",

            "Available"

        ]

    }


    import pandas as pd


    st.dataframe(

        pd.DataFrame(report_df),

        use_container_width=True,

        hide_index=True

    )


    st.divider()


    # ==========================================================
    # Data Engineering Downloads
    # ==========================================================

    st.subheader("📊 Data Engineering Reports")


    data_files = {

        "Master Dataset":

        "data/processed/master_dataset.csv",

    }


    for name, file_path in data_files.items():


        path = Path(file_path)


        if path.exists():


            with open(path, "rb") as file:


                st.download_button(

                    label=f"⬇ Download {name}",

                    data=file,

                    file_name=path.name,

                    mime="text/csv"

                )


        else:

            st.warning(
                f"{name} not found"
            )


    st.divider()


    # ==========================================================
    # AI Prediction Downloads
    # ==========================================================

    st.subheader("🤖 AI Prediction Reports")


    ai_files = {


        "AI Decisions":

        "outputs/ai_decisions.csv",


        "Inventory Prediction":

        "outputs/inventory_prediction.csv",


        "Demand Prediction":

        "outputs/demand_prediction.csv"

    }



    for name, file_path in ai_files.items():


        path = Path(file_path)


        if path.exists():


            with open(path, "rb") as file:


                st.download_button(

                    label=f"⬇ Download {name}",

                    data=file,

                    file_name=path.name,

                    mime="text/csv"

                )


        else:

            st.info(
                f"{name} file not available"
            )


    st.divider()
        # ==========================================================
    # Classical Optimization Downloads
    # ==========================================================

    st.subheader("⚙️ Classical Optimization Reports")


    classical_files = {


        "Default Assignment":

        "outputs/default_assignment.csv",


        "Greedy Assignment":

        "outputs/greedy_assignment.csv",


        "Linear Programming":

        "outputs/linear_programming.csv"

    }


    for name, file_path in classical_files.items():


        path = Path(file_path)


        if path.exists():


            with open(path, "rb") as file:


                st.download_button(

                    label=f"⬇ Download {name}",

                    data=file,

                    file_name=path.name,

                    mime="text/csv"

                )


        else:

            st.info(
                f"{name} report not available"
            )


    st.divider()



    # ==========================================================
    # Quantum Optimization Downloads
    # ==========================================================

    st.subheader("⚛️ Quantum Optimization Reports")


    quantum_files = {


        "Qiskit Assignment":

        "outputs/qiskit_assignments.csv",


        "PennyLane Assignment":

        "outputs/pennylane_assignments.csv",


        "Hybrid Quantum Result":

        "outputs/hybrid_results.csv"

    }



    for name, file_path in quantum_files.items():


        path = Path(file_path)


        if path.exists():


            with open(path, "rb") as file:


                st.download_button(

                    label=f"⬇ Download {name}",

                    data=file,

                    file_name=path.name,

                    mime="text/csv"

                )


        else:

            st.info(
                f"{name} report not available"
            )


    st.divider()



    # ==========================================================
    # Evaluation Reports Downloads
    # ==========================================================

    st.subheader("📈 Evaluation & Benchmark Reports")


    evaluation_files = {


        "Benchmark Results":

        "outputs/benchmarks/benchmark_results.csv",


        "Model Comparison":

        "outputs/comparison/model_comparison.csv",


        "Business Summary":

        "outputs/business_report/business_summary.csv"

    }



    for name, file_path in evaluation_files.items():


        path = Path(file_path)


        if path.exists():


            with open(path, "rb") as file:


                st.download_button(

                    label=f"⬇ Download {name}",

                    data=file,

                    file_name=path.name,

                    mime="text/csv"

                )


        else:

            st.warning(
                f"{name} report missing"
            )


    st.divider()



    # ==========================================================
    # Business Strategy Downloads
    # ==========================================================

    st.subheader("💼 Business Strategy Reports")


    strategy_files = {


        "Executive Strategy":

        "outputs/business_strategy/executive_strategy.csv",


        "Strategy Summary":

        "outputs/business_strategy/business_strategy_summary.csv"

    }



    for name, file_path in strategy_files.items():


        path = Path(file_path)


        if path.exists():


            with open(path, "rb") as file:


                st.download_button(

                    label=f"⬇ Download {name}",

                    data=file,

                    file_name=path.name,

                    mime="text/csv"

                )


        else:

            st.info(
                f"{name} will be generated after export"
            )


    st.divider()
        # ==========================================================
    # Complete Project Export
    # ==========================================================

    st.subheader("📦 Complete Project Export")


    st.info("""
Download all project outputs together.

The export package contains:

✓ AI Reports

✓ Classical Optimization Results

✓ Quantum Solver Outputs

✓ Evaluation Reports

✓ Business Strategy Reports

✓ Dataset Files
""")


    import zipfile
    import io


    export_files = [

        "data/processed/master_dataset.csv",

        "outputs/ai_decisions.csv",

        "outputs/default_assignment.csv",

        "outputs/greedy_assignment.csv",

        "outputs/linear_programming.csv",

        "outputs/benchmarks/benchmark_results.csv",

        "outputs/comparison/model_comparison.csv",

        "outputs/business_report/business_summary.csv",

    ]


    zip_buffer = io.BytesIO()


    with zipfile.ZipFile(
        zip_buffer,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zip_file:


        for file_path in export_files:


            path = Path(file_path)


            if path.exists():

                zip_file.write(
                    path,
                    arcname=path.name
                )


    zip_buffer.seek(0)


    st.download_button(

        label="📦 Download Complete Nestlé Quantum DOM Package",

        data=zip_buffer,

        file_name="Nestle_Quantum_DOM_Report.zip",

        mime="application/zip"

    )


    st.divider()



    # ==========================================================
    # Executive Summary Export
    # ==========================================================

    st.subheader("📄 Executive Summary Export")


    executive_summary = """

Nestlé Quantum Distributed Order Management

Enterprise Project Summary


Completed Modules:

✓ Data Engineering

✓ AI Prediction

✓ Classical Optimization

✓ Quantum Optimization

✓ Benchmarking

✓ Model Comparison

✓ Business Strategy


Technology Stack:

Python

Machine Learning

Optimization Algorithms

Qiskit

PennyLane

Streamlit


Business Outcomes:

• Improved supply chain decision making

• AI assisted planning

• Optimization based allocation

• Quantum ready architecture


Project Status:

Enterprise Ready


Developed by:

Sirama Avinash

"""


    st.download_button(

        label="📄 Download Executive Summary",

        data=executive_summary,

        file_name="Nestle_Quantum_DOM_Executive_Summary.txt",

        mime="text/plain"

    )


    st.divider()



    # ==========================================================
    # Project Completion Dashboard
    # ==========================================================

    st.subheader("🏆 Project Completion Status")


    completion = {

        "Phase": [

            "Data Engineering",

            "AI Prediction",

            "Classical Optimization",

            "Quantum Optimization",

            "Evaluation",

            "Business Strategy",

            "Downloads"

        ],

        "Status": [

            "✅ Completed",

            "✅ Completed",

            "✅ Completed",

            "✅ Completed",

            "✅ Completed",

            "✅ Completed",

            "✅ Completed"

        ]

    }


    import pandas as pd


    st.dataframe(

        pd.DataFrame(completion),

        use_container_width=True,

        hide_index=True

    )


    st.divider()



    # ==========================================================
    # Technology Stack
    # ==========================================================

    st.subheader("🛠 Enterprise Technology Stack")


    t1, t2, t3, t4 = st.columns(4)


    with t1:

        st.success("""
### Data

• Pandas

• NumPy

• CSV Pipeline

• Feature Engineering
""")


    with t2:

        st.info("""
### AI

• Scikit-learn

• Random Forest

• Prediction Models

• Recommendation Engine
""")


    with t3:

        st.warning("""
### Optimization

• Greedy

• Linear Programming

• QUBO

• QAOA
""")


    with t4:

        st.success("""
### Quantum

• Qiskit

• PennyLane

• Hybrid Solver

• Quantum Roadmap
""")


    st.divider()



    # ==========================================================
    # Final Footer
    # ==========================================================

    st.caption("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📥 Phase H – Enterprise Downloads Center


Nestlé Quantum Distributed Order Management


Complete AI + Classical + Quantum Supply Chain Platform


Modules:

✓ Data Engineering

✓ AI Prediction

✓ Classical Optimization

✓ Quantum Optimization

✓ Evaluation

✓ Business Strategy

✓ Enterprise Reporting


Developed by

SYED RAZAK


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")