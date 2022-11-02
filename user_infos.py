import db_connection


def user_informations(pseudo):
    user = db_connection.select_user_by_psuedo(pseudo)
    return user

if __name__ == '__main__':
    user = user_informations('')
    print(user)