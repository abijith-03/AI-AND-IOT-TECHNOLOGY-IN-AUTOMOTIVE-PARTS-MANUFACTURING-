import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    return conn
