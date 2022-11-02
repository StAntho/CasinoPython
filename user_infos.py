import db_connection


def user_informations(pseudo,user_id):
    user = db_connection.select_user_by_psuedo(pseudo)
    for row in user:
        print("--------------------------------------------")
        print("------------Information---------------------")
        print("---- id: ", row[0])
        print("---- Pseudo: ", row[1])
        print("---- Sold: ", row[2])
        print("---- Current level: ", row[3])
        print("---- First connection: ", row[4])
        print("--------------------------------------------")
        print("--------------------------------------------")

    user_stats = db_connection.get_all_stat_by_user_id(10)
    for row in user_stats:
        print("------------Statistiques-------------------")
        print("---- Level max: ", row[0])
        print("---- Gain min: ", row[1])
        print("---- Gain moy: ", row[2])
        print("---- Gain max: ", row[3])
        print("---- Mise min: ", row[4])
        print("---- Mise moy: ", row[5])
        print("---- Mise max: ", row[6])
        print("---- Nb coup moy: ", row[7])
        print("--------------------------------------------")
        print("--------------------------------------------")

if __name__ == '__main__':
    user_informations('azerty',10)
   