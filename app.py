import streamlit as st
import sqlite3  # Change this if using MySQL or PostgreSQL
import os
import importlib.util

# Connect to Database
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Streamlit Config
st.set_page_config(page_title="AI in Automotive Industry", layout="wide")
st.sidebar.title("Navigation")

# Multi-Page Navigation
pages = {
    "📂 Upload Data": "upload.py",
    "🛠 Data Cleaning": "cleaning.py",
    "📊 Data Analysis": "analysis5.py",
    "🤖 Machine Learning & Reports": "ml6.py",
    "📈 Results": "results.py"
}

page = st.sidebar.radio("Go to", list(pages.keys()))

# Function to Import and Run Selected Page
def load_page(page_file):
    if os.path.exists(page_file):
        spec = importlib.util.spec_from_file_location("page_module", page_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    else:
        st.error(f"⚠️ Error: `{page_file}` not found! Please check the file path.")

# Run Selected Page
if page in pages:
    load_page(pages[page])
