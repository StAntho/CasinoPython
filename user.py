from tokenize import PseudoExtras


class User:
    def __init__(self, id, pseudo, sold, current_level, first_connection):
        self.id = id
        self.pseudo = pseudo
        self.sold = sold
        self.current_level = current_level
        self.first_connection = first_connection

    def user_name():
        print('user')