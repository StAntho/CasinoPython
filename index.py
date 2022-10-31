from user import User
import stat as s
# int(input("Montant ?  : "))

# from random import randrange
# nb_ordi = randrange(0, 11, 1)
# print("Mon choix = ", nb_ordi)
# nb_user = -1
# nb_coup = 0
# while nb_ordi != nb_user :
# 	nb_user = int(input("Devine le nombre auquel je pense qui est compris entre 0 et 10\n"))
# 	if nb_user > nb_ordi :
# 		print ('Votre nbre est trop grand')
# 	elif nb_user < nb_ordi :
# 		print ('Votre nbre est trop petit')
# 	nb_coup += 1
# print("Bingo ! Vous avez gagné en {} coup(s) !".format(nb_coup))

if __name__ == '__main__':
    print("hello world")

    toto = User(1, "toto", "10/11/2022 14:25")
    print(toto)
    print(toto.first_connection)
    