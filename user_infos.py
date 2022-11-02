import db_connection


def user_informations(pseudo):
    user = db_connection.select_user_by_psuedo(pseudo)
    for row in user:
        print("id: ", row[0])
        print("Pseudo: ", row[1])
        print("Sold: ", row[2])
        print("Current level: ", row[3])
        print("First connection: ", row[4])

if __name__ == '__main__':
    user_informations('testData4')
   