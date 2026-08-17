import streamlit as st
import pandas as pd


def show_insights():

    st.title("Business Insights")

    # ===============================
    # Check Dataset
    # ===============================

    if "df" not in st.session_state:

        st.warning("Please upload a dataset first.")
        return

    df = st.session_state["df"]

    st.success("Dataset Loaded Successfully")

    st.divider()

    st.header("Dataset Overview")

    st.write(f"**Total Rows:** {df.shape[0]}")
    st.write(f"**Total Columns:** {df.shape[1]}")
    st.write(f"**Missing Values:** {df.isnull().sum().sum()}")

    st.divider()

    # ===============================
    # Numeric Summary
    # ===============================

    st.header("Numeric Summary")

    st.dataframe(df.describe(), use_container_width=True)

    st.divider()

    # ===============================
    # Missing Values
    # ===============================

    st.header("Missing Values")

    missing = df.isnull().sum()

    st.dataframe(
        missing.to_frame(name="Missing Values"),
        use_container_width=True
    )

    st.divider()

    # ===============================
    # Smart Insights
    # ===============================

    st.header("Smart Insights")

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    if len(numeric_columns) == 0:

        st.warning("No numeric columns found.")

    else:

        selected_column = st.selectbox(
            "Select Numeric Column",
            numeric_columns
        )

        st.metric(
            "Maximum Value",
            round(df[selected_column].max(), 2)
        )

        st.metric(
            "Minimum Value",
            round(df[selected_column].min(), 2)
        )

        st.metric(
            "Average",
            round(df[selected_column].mean(), 2)
        )

        st.metric(
            "Median",
            round(df[selected_column].median(), 2)
        )

        st.metric(
            "Standard Deviation",
            round(df[selected_column].std(), 2)
        )

    st.divider()

    # ===============================
    # Categorical Insights
    # ===============================

    categorical_columns = df.select_dtypes(include="object").columns.tolist()

    if len(categorical_columns) > 0:

        st.header("Category Insights")

        category = st.selectbox(
            "Select Category Column",
            categorical_columns
        )

        st.write("### Top 10 Values")

        st.dataframe(
            df[category].value_counts().head(10),
            use_container_width=True
        )

    st.divider()

    st.success("✅ Analysis Completed Successfully!")