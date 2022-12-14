import db_connection
from datetime import datetime
from sys import exit
from game import game
import user_infos

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
	if not is_user :
		# Si nouvel utilisateur
		level = 1
		sold = 10
		db_connection.insert_data(name_user, sold, level, datetime.now())
		is_user = db_connection.select_user_by_psuedo(name_user)
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
				break
			else :
				print('Je ne comprends pas ! Voulez-vous recommencer au level 1 (O/N) ?')

	# Récupération de l'id et du solde de l'utilisateur
	for data in is_user :
		user_id = data[0]
		user_sold = data[2]

	# Début du jeu
	print("\nLevel {}".format(level))
	while True :
		game_ret = game(user_id, user_sold, name_user, level)
		if game_ret :
			if level != 3 :
				level += 1
		else :
			if level != 1 :
				level -= 1
		# Update du level atteint par l'utilisateur
		db_connection.update_user_level(level, user_id)	

		# Récupération du nouveau solde
		user_data = db_connection.select_user_by_psuedo(name_user)
		for data in user_data :
			user_sold = data[2]

		if user_sold == 0 :
			db_connection.delete_user(user_id)
			print("Vous n'avez plus d'argent à miser. Au revoir !")
			exit()

		# Si l'utilisateur veut s'arrêter ici
		if leave() :
			if game_ret :
				print("\nSuper ! Vous passez au Level {}.".format(level))
			else :
				print("\nVous passez au Level {}.".format(level))
			continue
		user_infos.user_informations(name_user, user_id)
		user_infos.best_player()
		print("\nAu revoir ! Vous finissez la partie avec {} €.".format(user_sold))
		exit()