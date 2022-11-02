import os
from dotenv import load_dotenv
import mysql.connector as con
from mysql.connector import Error
load_dotenv()

# Connexion à la base de donnée
def connectDB() :
    connection_params = {
    'host': os.getenv('HOST_NAME'),
    'user': os.getenv('USER_NAME'),
    'password': os.getenv('PASSWORD'),
    'database': os.getenv('DATABASE_NAME'),
    }
    try :
        connection = con.connect(**connection_params)
        if connection and connection.is_connected():
            return connection
    except Error as e :
        print("Failed to connect: {}".format(e))

# Insertion d'un nouvel utilisateur
def insert_data(pseudo, sold, current_level, datetime) :
    db = connectDB()
    mySql_insert_query = """INSERT INTO User (pseudo, sold, current_level, first_connection) VALUES (%s, %s ,%s, %s) """
    cursor = db.cursor()
    record = (pseudo, sold,current_level ,datetime)
    cursor.execute(mySql_insert_query, record)
    db.commit()
    print(cursor.rowcount, "Record inserted successfully into User table")

# Récupère les informations de l'utilisateur pseudo
def select_user_by_psuedo(pseudo) :
    db = connectDB()
    mySql_select_query = """SELECT * FROM User WHERE pseudo = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (pseudo,))
    records = cursor.fetchall()
    return records

# Insertion d'une ligne après avoir fini un level
def insert_level(user_id, level, mise, gain, nb_coup) :
    db = connectDB()
    mySql_insert_query = """INSERT INTO Level (user_id, level, mise, gain, nb_coup) VALUES (%s, %s, %s, %s, %s) """
    cursor = db.cursor()
    record = (user_id, level, mise, gain, nb_coup)
    cursor.execute(mySql_insert_query, record)
    db.commit()
    print(cursor.rowcount, "Record inserted successfully into Level table")

# Récupère le dernier level atteint par l'utilisateur user_name
def select_user_level(user_name) :
    db = connectDB()
    mySql_select_query = """SELECT current_level FROM User WHERE pseudo = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (user_name,))
    records = cursor.fetchall()
    for row in records :
        return row[0]

# Update du level atteint de l'utilisateur user_id
def update_user_level(current_level, user_id) :
    db = connectDB()
    mySql_update_query = """UPDATE User SET current_level = %s WHERE id = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_update_query, (current_level, user_id))
    db.commit()
    print(cursor.rowcount, "Record updated successfully into User table")

# Update du sold de l'utilisateur user_id
def update_user_sold(sold, user_id) :
    db = connectDB()
    mySql_update_query = """UPDATE User SET sold = %s WHERE id = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_update_query, (sold, user_id))
    db.commit()
    print(cursor.rowcount, "Record updated successfully into User table")

# Retourne les statistiques de l'utilisateur user_id
def get_all_stat_by_user_id(user_id) :
    db = connectDB()
    mySql_select_query = """SELECT MAX(level) level_max
                                , MIN(gain) gain_min
                                , AVG(gain) gain_moy
                                , MAX(gain) gain_max
                                , MIN(mise) mise_min
                                , AVG(mise) mise_moy
                                , MAX(mise) mise_max
                                , AVG(nb_coup) nb_coup_moy
                            FROM Level
                            WHERE user_id = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (user_id,))
    records = cursor.fetchall()
    return records

# Retourne le nombre de fois où le user_id a trouvé dès le 1er coup
def get_find_in_one_by_user_id(user_id) :
    db = connectDB()
    mySql_select_query = """SELECT COUNT(*)
                            FROM Level
                            WHERE user_id = %s
                                AND nb_coup = 1"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (user_id,))
    records = cursor.fetchall()
    for row in records :
        return row[0]

# Retourne les statistiques de tous les utilisateurs
def get_all_stat() :
    db = connectDB()
    mySql_select_query = """SELECT user_id
                                , MAX(level) level_max
                                , MIN(gain) gain_min
                                , AVG(gain) gain_moy
                                , MAX(gain) gain_max
                                , MIN(mise) mise_min
                                , AVG(mise) mise_moy
                                , MAX(mise) mise_max
                                , AVG(nb_coup) nb_coup_moy
                            FROM Level
                            GROUP BY user_id"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query)
    records = cursor.fetchall()
    return records