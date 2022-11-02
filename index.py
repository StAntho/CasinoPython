from random import randrange
import db_connection
from datetime import datetime


# Initialisation de la mise de l'utilisateur
def set_mise(level = 1) :
	sold = 10 # TODO: Il faut récupérer le solde de l'utilisateur
	if level != 1 or sold != 10 :
		print("\nEntrez votre mise :")
		while True :
			try :
				mise = int(input(''))
				if mise > sold :
					print("Erreur, votre mise est plus elevé que votre solde.")
					print("Entrer une mise inférieure ou égale à " + sold + " € :")
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


# Inclusion du jeu
def game(name_user, level, mise) :
	while True :
		match level :
			case 1 :
				nb_ordi = randrange(0, 11, 1)
				nb_coup_max = 3
			case 2 :
				print("\nRappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et 20 et vous avez le droit à 5 essais !")
				mise = set_mise(level)
				nb_ordi = randrange(0, 21, 1)
				nb_coup_max = 5
			case 3 :
				print("\nRappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et 30 et vous avez le droit à 7 essais !")
				mise = set_mise(level)
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
					# TODO: Il faut enregistrer en base les stats (user_id, level, mise, gain, nb_coup)
					db_connection.insert_level(name_user, level , mise , gain, nb_coup)
					return True

				if nb_coup == nb_coup_max :
					print("Vous avez perdu ! Mon nombre est " + str(nb_ordi) + " !")
					# TODO: Il faut enregistrer en base les stats (nb_coup, gain, mise)
					return False
				else :
					print("Il vous reste " + str(nb_coup_max - nb_coup) + " chance(s) !")
					continue
			except ValueError :
				print("Je ne comprends pas ! Entrer SVP un nombre entre 1 et 10 :")
				continue


# Fonction affichant toutes les stats de l'utilisateur
def show_stat(level) :
	# TODO: Il faut récupérer toutes les stats
	print("Les statistiques du level " + str(level) + " sont les suivantes :")
	print("\n\t")
	return


# Fonction pour savoir si l'utilisateur souhaite quitter le jeu
def leave() :
	print("\n Souhaitez-vous continuer la partie (O/N) ?")
	while True :
		leave = input('')
		if leave.lower() == 'o' :
			return True
		elif leave.lower() == 'n' :
			return False
		else :
			print("Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?")


instruction_txt = """\nJe viens de penser à un nombre entre 1 et 10. Devinez lequel ?
Att : vous avez le droit à trois essais !
Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !
Si vous le devinez au 2è coup, vous gagnez exactement votre mise !
Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !
Si vous ne le devinez pas au 3è coup, vous perdez votre mise et vous avez le droit :
\t- de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu.
\t- de quitter le jeu.
Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU de continuer le jeu en passant au level supérieur."""


print("Je suis Python. Quel est votre pseudo ?")
name_user = input('')

while name_user :
	is_user = db_connection.select_user_by_psuedo(name_user)
	print(is_user)
	if not is_user :
		# Si nouvel utilisateur
		level = 1
		sold = 10
		db_connection.insertData(name_user,sold,level,datetime.now())
		print("\nHello " + name_user + ", vous avez 10 €, Très bien ! Installez vous SVP à la table de pari.")
		print("Je vous expliquerai le principe du jeu :\n")
		print(instruction_txt)
	else :
		# Si l'utilisateur est connnu alors demander s'il veut relire les règles
		print("\nVoulez-vous que j'explique les règles du jeu (O/N) ?")
		while True:
			instruction = input('')
			if instruction.lower() == 'o' :
				print(instruction_txt)
				break
			elif instruction.lower() == 'n' :
				break
			else :
				print("Je ne comprends pas ! Voulez-vous que j'explique les règles du jeu (O/N) ?")
		
		print("\nVoulez-vous recommencer au level 1 (O/N) ?")
		while True :
			level_statement = input('')
			if level_statement.lower() == 'o' :
				level = 1
				break
			elif level_statement.lower() == 'n' :
				level = db_connection.select_user_level(name_user)
				# level = 2
				break
			else :
				print('Je ne comprends pas ! Voulez-vous recommencer au level 1 (O/N) ?')

	# Insertion de la mise
	print("\nLe jeu commence, entrez votre mise :")
	mise = set_mise(level)

	# Début du jeu
	print("\nLevel " + str(level))
	while True :
		game_ret = game(name_user, level, mise)
		if game_ret :
			if level != 3 :
				show_stat(level)
				level += 1
			else :
				show_stat(level)
				break
		else :
			if level != 1 :
				level -= 1

		if leave() :
			if game_ret :
				print("\nSuper ! Vous passez au Level " + str(level) + ".")
			else :
				print("\nVous passez au Level " + str(level) + ".")
			continue
		print("\nAu revoir ! Vous finissez la partie avec " + str(mise) + " €.")
		break
	break