from classes import rand_class
from races import rand_race
from character import roll_ability_scores
import numpy as np

_class = rand_class()
race = rand_race()
print(race, _class)

init_scores = roll_ability_scores()
print(init_scores)
print(race.stat_bonus)
print(init_scores + race.stat_bonus)
