import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

st.title("Machine Learning Model for Automotive Industry")

if "cleaned_data" in st.session_state:
    data = st.session_state["cleaned_data"]
    st.write("### Cleaned Data Preview")
    st.dataframe(data.head())

    target = st.selectbox("Select Target Variable", data.columns)
    features = st.multiselect("Select Features", [col for col in data.columns if col != target])

    if features and target:
        # Convert Date-Time Columns to Numeric (Unix Timestamp)
        for col in features:
            if data[col].dtype == "object":  # Check if column is string (likely a date)
                try:
                    data[col] = pd.to_datetime(data[col])  # Convert to DateTime
                    data[col] = data[col].astype(int) / 10**9  # Convert to Unix Timestamp
                except:
                    st.warning(f"Skipping column '{col}' as it cannot be converted to numeric.")
                    features.remove(col)  # Remove problematic column

        # Ensure Features are Numeric
        X = data[features].apply(pd.to_numeric, errors='coerce')
        y = pd.to_numeric(data[target], errors='coerce')

        # Drop rows where target or features have NaN values
        X = X.dropna()
        y = y.loc[X.index]  # Keep only rows that exist in both X and y

        # 🚨 Check if there are valid data points left
        if X.empty or y.empty:
            st.error("Error: No valid numeric data available for training. Check your selected features.")
        else:
            # Split the data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train Model
            model = RandomForestRegressor(n_estimators=100)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            st.write(f"Mean Absolute Error: {mae:.4f}")
            st.write(f"R² Score: {r2:.4f}")

            if st.button("Save Model Results"):
                st.session_state["model_results"] = {"MAE": mae, "R2": r2}
                st.success("Model Results Saved!")
else:
    st.warning("Please clean the data first!")
