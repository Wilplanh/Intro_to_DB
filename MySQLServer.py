# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (update user & password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pass_word"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Use CREATE DATABASE IF NOT EXISTS so it won’t fail
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: feedback when closing
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
