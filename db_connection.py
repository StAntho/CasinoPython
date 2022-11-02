import os
from dotenv import load_dotenv
import mysql.connector as con
from mysql.connector import Error
from datetime import datetime
load_dotenv()

def connectDB():
    connection_params = {
    'host': os.getenv('HOST_NAME'),
    'user': os.getenv('USER_NAME'),
    'password': os.getenv('PASSWORD'),
    'database': os.getenv('DATABASE_NAME'),
    }
    try:
        connection = con.connect(**connection_params)
        if connection and connection.is_connected():
            return connection
    except Error as e:
        print("Failed to connect: {}".format(e))


def insert_data(pseudo,sold,cur_level,datetime):
    db = connectDB()
    mySql_insert_query = """INSERT INTO User (pseudo, sold, first_connection) VALUES (%s, %s,%s,%s) """
    cursor = db.cursor()
    record = (pseudo, sold,cur_level ,datetime)
    cursor.execute(mySql_insert_query, record)
    db.commit()
    print(cursor.rowcount, "Record inserted successfully into User table")
    
def select_user_by_psuedo(pseudo):
    db = connectDB()
    mySql_select_query = """SELECT * FROM User WHERE pseudo = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (pseudo,))
    records = cursor.fetchall()
    return records


def select_user():
    db = connectDB()
    mySql_select_query = """SELECT * FROM User"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query)
    records = cursor.fetchall()
    return records

def delete_user(username):
    db = connectDB()
    mySql_delete_query = """DELETE FROM User WHERE pseudo = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_delete_query, (username,))
    db.commit()
    print(cursor.rowcount, "Record deleted successfully from User table")

def insert_level(user_id,level,mise,gain,nb_coup):
    db = connectDB()
    mySql_insert_query = """INSERT INTO Level (user_id,level,mise,gain,nb_coup) VALUES (%s,%s,%s,%s,%s) """
    cursor = db.cursor()
    record = (user_id,level,mise,gain,nb_coup)
    cursor.execute(mySql_insert_query, record)
    db.commit()
    print(cursor.rowcount, "Record inserted successfully into Level table")


def select_user_level(user_name):
    db = connectDB()
    mySql_select_query = """SELECT current_level FROM User WHERE pseudo = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (user_name,))
    records = cursor.fetchall()
    for row in records:
        return row[0]
    # return records

def update_user_sold_level(sold,current_level):
    db = connectDB()
    mySql_update_query = """UPDATE User SET sold = %s, current_level = %s WHERE pseudo = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_update_query, (sold,current_level))
    db.commit()
    print(cursor.rowcount, "Record updated successfully into User table")

def update_user_level(user_id,current_level):
    db = connectDB()
    mySql_update_query = """UPDATE User SET current_level = %s WHERE id = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_update_query, (user_id,current_level))
    db.commit()
    print(cursor.rowcount, "Record updated successfully into User table")

def update_user_sold(user_id,sold):
    db = connectDB()
    mySql_update_query = """UPDATE User SET sold = %s WHERE id = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_update_query, (user_id,sold))
    db.commit()
    print(cursor.rowcount, "Record updated successfully into User table")

if __name__ == "__main__":
    # recods = select_user()
    # print(recods)
    # record = select_user_by_psuedo("testData2")
    # print(record)
    # date = datetime.now()
    # # datenow = date.strftime("%d/%m/%Y %H:%M:%S")
    # insertData('testData9',45,date)
    # recods = select_user()
    record = select_user_level('azerty')
    print(record)