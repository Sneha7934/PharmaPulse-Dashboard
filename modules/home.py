import streamlit as st


def show_home():

    # =====================================
    # Page Title
    # =====================================

    st.title("PharmaPulse")


    st.subheader("Healthcare & Pharmacy Analytics Dashboard")

    st.markdown("""
Welcome to **PharmaPulse**!

This application is designed to analyze Healthcare and Pharmacy datasets through interactive dashboards, dynamic visualizations and business insights.
""")

    st.subheader("Healthcare & Pharmacy Analytics Dashboard")

    st.markdown("""
Welcome to **PharmaPulse**!

This application is designed to analyze **Healthcare and Pharmacy datasets**
through interactive dashboards, dynamic visualizations and business insights.
""")

    st.divider()

    # =====================================
    # Features
    # =====================================

    st.header("Features")

    col1, col2 = st.columns(2)

    with col1:
        st.success("Upload Healthcare Dataset")
        st.success("Interactive Data Visualization")
        st.success("Multiple Chart Types")

    with col2:
        st.success("Business Insights")
        st.success("Dataset Summary")
        st.success("Fast & Easy Analysis")

    st.divider()

    # =====================================
    # Supported Datasets
    # =====================================

    st.header("Supported Datasets")

    st.markdown("""
- Pharmacy Sales Dataset
- Medicine Inventory
- Hospital Dataset
- Diagnostic Lab Dataset
- Clinic Dataset
- Medical Store Dataset
""")

    st.divider()

    # =====================================
    # Technologies
    # =====================================

    st.header("🛠 Technologies Used")

    tech1, tech2, tech3 = st.columns(3)

    with tech1:
        st.info("Python")

    with tech2:
        st.info("Pandas")

    with tech3:
        st.info("Streamlit")

    st.divider()

    # =====================================
    # Workflow
    # =====================================

    st.header("How It Works")

    st.markdown("""
### Step 1
Upload a Healthcare or Pharmacy CSV dataset.

### Step 2
Generate interactive visualizations.

### Step 3
Explore business insights.

### Step 4
Understand the dataset through charts and analysis.
""")

    st.divider()

    # =====================================
    # About Project
    # =====================================

    st.header("About PharmaPulse")

    st.markdown("""PharmaPulse is a healthcare-focused data analytics dashboard developed using Python, Pandas, Matplotlib, and Streamlit. The primary objective of this project is to simplify the analysis of pharmacy and healthcare datasets by transforming raw CSV data into meaningful visualizations and actionable business insights. It enables users to upload healthcare-related datasets and explore them through an intuitive, interactive interface without requiring advanced programming knowledge.

The dashboard supports key analytical tasks such as dataset exploration, interactive chart generation, and business insight discovery. By providing visual representations of healthcare data, PharmaPulse helps users identify sales trends, inventory patterns, category performance, and other valuable metrics that support informed decision-making. This project demonstrates the practical application of data analytics and visualization techniques in the healthcare domain while showcasing the capabilities of Python-based dashboard development.""")

#    st.divider()

#     # =====================================
#     # Developer
#     # =====================================

#     st.header("Developer")

#     st.write("**Sneha Dey**")
#     st.write("Python | Data Analytics | Streamlit")

#     st.divider()

#     st.success("Use the sidebar to upload a healthcare dataset and start exploring.")