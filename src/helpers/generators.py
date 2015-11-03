from definitions import classes, races
import random


class_list 	= classes.roster
race_list 	= races.roster


# Generates a 8-digit seed if one was not provided.
def seed (seed=None):

	if seed == None or seed == '':
		seed = []
		for i in range(8):
			seed.append(str(random.randint(0,9)))
		return ''.join(seed)
	else:
		return seed


# Provides a random race and class for the character.
def randomizer (seed=None):

	random.seed(seed)

	random_race = race_list[random.randint(0, len(race_list) - 1)]
	random_class = random.choice(sorted(list(class_list.keys())))
	return {'race': random_race, 'class': random_class}
