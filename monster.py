import numpy as np


class RoundOfCombat(object):

    def __init__(self, monster_list):
        self.monster_list = monster_list


class Monster(object):

    def __init__(self, dexterity_mod, size):
        self.dex_mod = dexterity_mod
        self.initiative_roll = None
        self._speed_factor_sizes = {
            'tiny': 5,
            'small': 2,
            'medium': 0,
            'large': -2,
            'huge': -5,
            'gargantuan': -8}
        self.size_mod = self._speed_factor_sizes[size]

    @property
    def dexterity_mod(self):
        return self.dex_mod

    @dexterity_mod.setter
    def dexterity_mod(self, modifier):
        self.dex_mod = modifier

    def roll_initiative(self):
        self.initiative_roll = round(np.random.uniform(1, 12))

    @property
    def initiative(self):
        return self.initiative_roll + self.dexterity_mod + self.size_mod

