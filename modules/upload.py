import streamlit as st
import pandas as pd


def show_upload():

    st.title("Upload Healthcare Dataset")

    st.write(
        "Upload a Healthcare or Pharmacy related CSV file to begin the analysis."
    )

    uploaded_file = st.file_uploader(
        "Choose a CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        # Read CSV
        df = pd.read_csv(uploaded_file)

        # ----------------------------
        # Basic Healthcare Validation
        # ----------------------------

        healthcare_keywords = [
            "medicine",
            "drug",
            "patient",
            "hospital",
            "clinic",
            "doctor",
            "pharmacy",
            "category",
            "brand",
            "stock",
            "supplier",
            "expiry"
        ]

        columns = [col.lower() for col in df.columns]

        matched = any(
            keyword in column
            for keyword in healthcare_keywords
            for column in columns
        )

        if not matched:

            st.error("This dataset doesn't appear to be a Healthcare or Pharmacy dataset.")
            st.stop()

        # Save dataframe
        st.session_state["df"] = df

        st.success("Dataset Uploaded Successfully!")

        st.divider()

        # =============================
        # Dataset Summary
        # =============================

        st.subheader("Dataset Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Rows", df.shape[0])

        with col2:
            st.metric("Columns", df.shape[1])

        with col3:
            st.metric("Missing Values", df.isnull().sum().sum())

        st.divider()

        # =============================
        # Preview
        # =============================

        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        st.divider()

        # =============================
        # Column Names
        # =============================

        st.subheader("Available Columns")

        st.write(df.columns.tolist())

        st.divider()

        st.info("Dataset loaded successfully. Go to the Visualization page.")

    else:

        st.warning("Please upload a CSV file.")