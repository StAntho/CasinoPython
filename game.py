from random import randrange
import db_connection

# Initialisation de la mise de l'utilisateur
def set_mise(level, user_sold) :
	# sold = 10 # TODO: Il faut récupérer le solde de l'utilisateur
	if level != 1 or user_sold != 10 :
		print("\nEntrez votre mise :")
		while True :
			try :
				mise = int(input(''))
				if mise > user_sold :
					print("Erreur, votre mise est plus elevé que votre solde.")
					print("Entrer une mise inférieure ou égale à " + user_sold + " € :")
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
def game(user_id, user_sold, name_user, level, mise) :
	while True :
		match level :
			case 1 :
				nb_ordi = randrange(0, 11, 1)
				nb_coup_max = 3
			case 2 :
				print("\nRappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et 20 et vous avez le droit à 5 essais !")
				mise = set_mise(level, user_sold)
				nb_ordi = randrange(0, 21, 1)
				nb_coup_max = 5
			case 3 :
				print("\nRappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et 30 et vous avez le droit à 7 essais !")
				mise = set_mise(level, user_sold)
				nb_ordi = randrange(0, 31, 1)
				nb_coup_max = 7

		nb_user = -1
		nb_coup = 0
		print("Mon choix : " + str(nb_ordi))
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
					if nb_coup == 1 :
						gain = mise * 2
					elif nb_coup == 2 :
						gain = mise
					elif nb_coup == 3 :
						gain = mise / 2
					print("Bingo " + name_user + ", vous avez gagné en " + str(nb_coup) + " coup(s) et vous avec emporté " + str(gain) + " € !")
					# TODO: Il faut enregistrer en base les stats (nb_coup, gain, mise)
					db_connection.insert_level(user_id, level , mise , gain, nb_coup)
					sold = user_sold - mise + gain
					print(sold)
					db_connection.update_user_sold(sold, user_id)
					return True

				if nb_coup == nb_coup_max :
					print("Vous avez perdu ! Mon nombre est " + str(nb_ordi) + " !")
					# TODO: Il faut enregistrer en base les stats (nb_coup, gain, mise)
					db_connection.insert_level(user_id, level , mise , 0, nb_coup)
					sold = user_sold - mise
					db_connection.update_user_sold(sold, user_id)
					return False
				else :
					print("Il vous reste " + str(nb_coup_max - nb_coup) + " chance(s) !")
					continue
			except ValueError :
				print("Je ne comprends pas ! Entrer SVP un nombre entre 1 et 10 :")
				continue