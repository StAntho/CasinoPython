class Stat:
    def __init__(self, id, user_id, level_max=0, gain_max=0, gain_min=0, gain_moy=0, mise_max=0, mise_min=0, mise_moy=0, nb_coup_moy=0):
        self.id = id
        self.user_id = user_id
        self.level_max = level_max
        self.gain_max = gain_max
        self.gain_min = gain_min
        self.gain_moy = gain_moy
        self.mise_max = mise_max
        self.mise_min = mise_min
        self.mise_moy = mise_moy
        self.nb_coup_moy = nb_coup_moy