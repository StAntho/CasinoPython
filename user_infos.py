import db_connection

# Affichage des statistiques de l'utilisateur user_id
def user_informations(pseudo, user_id) :
    user = db_connection.select_user_by_psuedo(pseudo)
    for row in user :
        print("--------------------------------------------")
        print("Voici les statistiques depuis la 1ère fois {}".format(row[4]))
        print("--------------------------------------------")

    user_stats = db_connection.get_all_stat_by_user_id(user_id)
    for row in user_stats :
        print("------------Vos meilleures statistiques-------------------")
        print("---- Level le plus élevé atteint est : {}".format(row[0]))
        print("---- Vous avez réussi à trouver le bon nombre dès le 1er coup {} fois.".format(db_connection.get_find_in_one_by_user_id(user_id)))
        print("---- Le gain le plus élevé est de : {}€".format(row[3]))
        print("---- La mise la plus élevée est de : {}€".format(row[6]))
        print("--------------------------------------------")
        print("------------Vos pires statistiques-------------------")
        print("---- Le gain le plus petit est de : {}€".format(row[1]))
        print("---- La mise la plus petite est de : {}€".format(row[4]))
        print("--------------------------------------------")
        print("------------Vos moyennes-------------------")
        print("---- Le gain moyen est de : {:.2f}€".format(row[2]))
        print("---- La mise moyenne est de : {:.2f}€".format(row[5]))
        print("---- Le nombre moyen de tentatives pour trouver le bon nombre est : {:.2f}".format(row[7]))
        print("--------------------------------------------")

def best_player() :
    best_player = db_connection.get_all_stat()
    print("--------------------- Top 3 des joueurs par solde-----------------------")
    print("------------------------------------------------------------------")
    for row in best_player :
        print("-------- {} avec un gain de {}€".format(row[0], row[1]))
