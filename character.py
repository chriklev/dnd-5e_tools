import numpy as np


class Character(object):
    def __init__(self, name, _class, race, level, alignment, hp_max, stats):
        self.name = name
        self._class = _class
        self.race = race
        self.level = level
        self.alignment = alignment
        self.background = background
        self.hp_max = hp_max
        self.hp_current = hp_max
        self.armor_class = armor_class


def roll_ability_scores():
    scores = np.sum(
        np.sort(
            np.random.randint(1, 7, size=(6, 4)),
            axis=1)[:, 1:],
        axis=1)
    return(scores)
