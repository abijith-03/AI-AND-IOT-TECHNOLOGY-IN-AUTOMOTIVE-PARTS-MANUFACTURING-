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
            if data[col].dtype == "object":  # If column is string (likely a date)
                try:
                    data[col] = pd.to_datetime(data[col])  # Convert to DateTime
                    data[col] = data[col].astype(int) / 10**9  # Convert to Unix Timestamp
                except:
                    st.warning(f"Skipping column '{col}' as it cannot be converted to numeric.")
                    features.remove(col)  # Remove problematic column

        # Ensure Features are Numeric
        X = data[features].apply(pd.to_numeric, errors='coerce')
        y = pd.to_numeric(data[target], errors='coerce')

        # Drop any remaining NaN values in both X and y
        X.dropna(inplace=True)
        y.dropna(inplace=True)

        # Ensure X and y have the same number of rows
        X, y = X.align(y, join="inner", axis=0)

        if X.empty or y.empty:
            st.error("Error: No valid data after cleaning. Please check your dataset.")
        else:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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
