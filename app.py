import streamlit as st
import sqlite3  # Change this if using MySQL or PostgreSQL

# Connect to Database
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn
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

# Run Selected Page
if page in pages:
    exec(open(pages[page]).read())
