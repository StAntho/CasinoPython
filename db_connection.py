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
        mySql_Create_Table_Query = """CREATE TABLE User ( 
                            Id int(11) NOT NULL,
                            pseudo varchar(250) NOT NULL,
                            first_connection Date NOT NULL,
                            PRIMARY KEY (Id)) """
        
        cursor = connection.cursor()
        cursor.execute(mySql_Create_Table_Query)
        print("Laptop Table created successfully ")
        # record = cursor.fetchone()
        # print("You're connected to database: ", record)
except Error as e:
    print("Failed to create table in MySQL: {}".format(e))
finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")