import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("Results & Reports")

if "model_results" in st.session_state:
    results = st.session_state["model_results"]
    st.write("### Model Performance")
    st.write(f"Mean Absolute Error: {results['MAE']:.4f}")
    st.write(f"R² Score: {results['R2']:.4f}")

    # Determine machine performance
    performance = "Good Performance" if results['R2'] > 0.7 else "Bad Performance"
    st.write(f"### Machine Performance: {performance}")

    # Visualization - Bar Chart
    performance_data = pd.DataFrame({
        "Metric": ["Mean Absolute Error", "R² Score"],
        "Value": [results['MAE'], results['R2']]
    })
    fig_bar = px.bar(performance_data, x="Metric", y="Value", title="Model Performance Metrics", color="Metric")
    st.plotly_chart(fig_bar)

    # Visualization - Line Chart for Trend Analysis
    trend_data = pd.DataFrame({
        "Epoch": list(range(1, 11)),  # Simulated 10 Epochs
        "Performance Score": [results['R2'] - (i * 0.02) for i in range(10)]
    })
    fig_line = px.line(trend_data, x="Epoch", y="Performance Score", title="Performance Trend Over Time")
    st.plotly_chart(fig_line)

    # Visualization - Gauge Chart for Performance Indicator
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=results['R2'],
        title={"text": "R² Score"},
        gauge={
            "axis": {"range": [0, 1]},
            "steps": [
                {"range": [0, 0.5], "color": "red"},
                {"range": [0.5, 0.7], "color": "yellow"},
                {"range": [0.7, 1], "color": "green"}
            ],
            "threshold": {"line": {"color": "black", "width": 4}, "thickness": 0.75, "value": results['R2']}
        }
    ))
    st.plotly_chart(fig_gauge)

