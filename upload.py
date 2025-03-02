import streamlit as st
import pandas as pd
import sqlite3

st.title("Upload Automotive Data")

# Database Connection
def init_db():
    conn = sqlite3.connect("automotive_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS uploads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    return conn

conn = init_db()

# File Upload
uploaded_file = st.file_uploader("Upload Automotive Data (CSV)", type=["csv"])

if uploaded_file:
    try:
        data = pd.read_csv(uploaded_file, encoding="utf-8")
    except UnicodeDecodeError:
        data = pd.read_csv(uploaded_file, encoding="ISO-8859-1")

    st.write("### Raw Data Preview")
    st.dataframe(data.head())

    if st.button("Submit Data"):
        st.session_state["data"] = data
        conn.execute("INSERT INTO uploads (filename) VALUES (?)", (uploaded_file.name,))
        conn.commit()
        st.success("Data uploaded successfully!")
