import os
from dotenv import load_dotenv
import mysql.connector as con
from mysql.connector import Error

load_dotenv()

connection_params = {
    'host': os.getenv('HOST_NAME'),
    'user': os.getenv('USER_NAME'),
    'password': os.getenv('PASSWORD'),
    'database': os.getenv('DATABASE_NAME'),
}
try:
    connection = con.connect(**connection_params)
    print(connection)
    if connection and connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection and connection.is_connected():
        # cursor.close()
        connection.close()
        print("MySQL connection is closed")