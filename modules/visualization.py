import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def show_visualization():

    st.title("Data Visualization")

    # ============================
    # Check Dataset
    # ============================

    if "df" not in st.session_state:

        st.warning("Please upload a dataset first.")
        return

    df = st.session_state["df"]

    st.success("Dataset Loaded Successfully")

    st.divider()

    # ============================
    # Chart Selection
    # ============================

    chart_type = st.selectbox(
        "Select Chart Type",
        [
            "Bar Chart",
            "Pie Chart",
            "Line Chart",
            "Histogram",
            "Scatter Plot",
            "Box Plot"
        ]
    )

    all_columns = df.columns.tolist()

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    x_column = st.selectbox(
        "Select X-Axis",
        all_columns
    )

    if chart_type != "Pie Chart":

        y_column = st.selectbox(
            "Select Y-Axis",
            numeric_columns
        )

    st.divider()

    # ============================
    # Generate Button
    # ============================

    if st.button("Generate Chart"):

        fig, ax = plt.subplots(figsize=(8,5))

        # ----------------------------
        # Bar Chart
        # ----------------------------

        if chart_type == "Bar Chart":

            data = df.groupby(x_column)[y_column].sum()

            ax.bar(data.index.astype(str), data.values)

            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            ax.set_title("Bar Chart")

            plt.xticks(rotation=45)

        # ----------------------------
        # Pie Chart
        # ----------------------------

        elif chart_type == "Pie Chart":

            data = df[x_column].value_counts()

            ax.pie(
                data,
                labels=data.index,
                autopct="%1.1f%%"
            )

            ax.set_title("Pie Chart")

        # ----------------------------
        # Line Chart
        # ----------------------------

        elif chart_type == "Line Chart":

            data = df.groupby(x_column)[y_column].sum()

            ax.plot(
                data.index.astype(str),
                data.values,
                marker="o"
            )

            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)

            plt.xticks(rotation=45)

        # ----------------------------
        # Histogram
        # ----------------------------

        elif chart_type == "Histogram":

            ax.hist(df[y_column], bins=10)

            ax.set_xlabel(y_column)

        # ----------------------------
        # Scatter Plot
        # ----------------------------

        elif chart_type == "Scatter Plot":

            ax.scatter(
                df[x_column],
                df[y_column]
            )

            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)

        # ----------------------------
        # Box Plot
        # ----------------------------

        elif chart_type == "Box Plot":

            ax.boxplot(df[y_column])

            ax.set_ylabel(y_column)

        st.pyplot(fig)