import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Exploratory Data Analysis - Automotive Industry")

if "data" not in st.session_state:
    st.warning("Please upload a dataset first.")
else:
    data = st.session_state["data"]

    target = st.selectbox("Select Target Variable", data.columns)
    features = st.multiselect("Select Features", [col for col in data.columns if col != target])

    charts = st.multiselect("Select Chart Types", ["Bar Chart", "Scatter Plot", "Histogram"])

    for chart in charts:
        if chart == "Bar Chart":
            x = st.selectbox("X-axis", features, key="bar_x")
            y = st.selectbox("Y-axis", features, key="bar_y")
            fig = px.bar(data, x=x, y=y)
            st.plotly_chart(fig)

        if chart == "Scatter Plot":
            x = st.selectbox("X-axis", features, key="scatter_x")
            y = st.selectbox("Y-axis", features, key="scatter_y")
            fig = px.scatter(data, x=x, y=y)
            st.plotly_chart(fig)

        if chart == "Histogram":
            x = st.selectbox("X-axis", features, key="hist_x")
            fig = px.histogram(data, x=x)
            st.plotly_chart(fig)
