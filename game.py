from random import randrange
import db_connection

# Initialisation de la mise de l'utilisateur
def set_mise(level, user_sold) :
	if level != 1 or user_sold != 10 :
		print("\nEntrez votre mise :")
		while True :
			try :
				mise = int(input(''))
				if mise > user_sold or mise == 0 :
					print("Erreur, votre mise est plus elevé que votre solde.")
					print("Entrer une mise inférieure ou égale à {} € :".format(user_sold))
					continue
				return mise
			except ValueError :
				print("Le montant saisi n'est pas valide.")
				continue
	else :
		while True :
			try :
				mise = int(input(''))
				if mise > 0 and mise < 11 :
					return mise
				else :
					print("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et 10 € :")
			except ValueError :
				print("Le montat saisi n'est pas valide. Entrer SVP un montant entre 1 et 10 € :")

# Début du jeu
def game(user_id, user_sold, name_user, level) :
	while True :
		match level :
			case 1 :
				print("\nLe jeu commence, entrez votre mise :")
				nb_ordi = randrange(1, 11, 1)
				max = 10
				nb_coup_max = 3
			case 2 :
				print("\nRappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et 20 et vous avez le droit à 5 essais !")
				nb_ordi = randrange(1, 21, 1)
				max = 20
				nb_coup_max = 5
			case 3 :
				print("\nRappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et 30 et vous avez le droit à 7 essais !")
				nb_ordi = randrange(1, 31, 1)
				max = 30
				nb_coup_max = 7

		mise = set_mise(level, user_sold)
		nb_user = -1
		nb_coup = 0
		while nb_ordi != nb_user :
			# TODO: Timer de 10 secondes
			print("Alors mon nombre est ?")
			try :
				nb_user = int(input(''))
				nb_coup += 1
				if nb_user > nb_ordi :
					print("Votre nbre est trop grand !")
				elif nb_user < nb_ordi :
					print("Votre nbre est trop petit !")
				elif nb_user == nb_ordi :
					match nb_coup :
						case 1 :
							gain = mise * 2
						case 2 :
							gain = mise
						case 3 :
							gain = mise / 2
						case 4 :
							gain = mise / 3
						case 5 :
							gain = mise / 4
						case 6 :
							gain = mise / 5
						case 7 :
							gain = mise / 6
					print("Bingo " + name_user + ", vous avez gagné en {} coup(s) et vous avez emporté {} € !".format(nb_coup, gain))
					db_connection.insert_level(user_id, level , mise , gain, nb_coup)
					sold = user_sold - mise + gain
					print(sold)
					db_connection.update_user_sold(sold, user_id)
					return True

				if nb_coup == nb_coup_max :
					print("Vous avez perdu ! Mon nombre est {} !".format(nb_ordi))
					db_connection.insert_level(user_id, level , mise , 0, nb_coup)
					sold = user_sold - mise
					db_connection.update_user_sold(sold, user_id)
					return False
				else :
					print("Il vous reste {} chance(s) !".format(nb_coup_max - nb_coup))
					continue
			except ValueError :
				print("Je ne comprends pas ! Entrer SVP un nombre entre 1 et {} :".format(max))
				continue