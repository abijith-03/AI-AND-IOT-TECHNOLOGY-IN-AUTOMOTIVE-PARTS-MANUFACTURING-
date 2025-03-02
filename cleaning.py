import streamlit as st
import pandas as pd

st.title("Data Cleaning for Automotive Data")

if "data" not in st.session_state:
    st.warning("Please upload a dataset first.")
else:
    data = st.session_state["data"]

    st.write("### Raw Data Preview")
    st.dataframe(data.head())

    missing_values = data.isnull().sum()
    st.write("### Missing Values", missing_values)

    method = st.selectbox("Handle Missing Values", ["Drop Rows", "Fill Mean", "Fill Median", "Fill Mode"])

    if method == "Drop Rows":
        data = data.dropna()
    elif method == "Fill Mean":
        data = data.fillna(data.mean(numeric_only=True))
    elif method == "Fill Median":
        data = data.fillna(data.median(numeric_only=True))
    elif method == "Fill Mode":
        data = data.fillna(data.mode().iloc[0])

    if st.button("Save Cleaned Data"):
        st.session_state["cleaned_data"] = data
        st.success("Data Cleaning Completed!")
