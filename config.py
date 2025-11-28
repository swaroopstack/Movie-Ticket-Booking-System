# config.py
import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",      # MySQL is running locally
            user="root",           # your MySQL username
            password="",           # enter password if you have one
            database="movie_db"    # name of your database
        )
        return conn
    except mysql.connector.Error as err:
        print("Database connection failed:", err)
        return None
