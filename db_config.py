import mysql.connector
from mysql.connector import Error

def get_db_connection():

    
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',    # Replace with your MySQL username
            password='your_password', # Replace with your MySQL password
            database='student_db'     # Ensure this database is created
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None
