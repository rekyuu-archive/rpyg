from definitions import classes, races
from objects import characters
import random


"""
TODO:
- Add items (weapons, armor, consumables, key)
- Add enemies
- Add world generation
- Add battle handling
- Add specials
- Add initial generation and database handling
- Port to Telegram
- Add webui
"""


class_list 	= classes.roster
race_list 	= races.roster


# Generates a 8-digit seed if one was not provided.
def seed_gen (seed=None):

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


# Runs the main program.
def main ():

	print('Name your character.')
	name = input('> ')
	print('Seed? (Leave blank for a random seed)')
	io_seed = input('> ')

	seed = seed_gen(io_seed)
	rand = randomizer(seed)

	print('Generating character {} with seed {}...'.format(name, seed))
	char = characters.Character(name, seed, rand)

	print('Character created. Here are your stats:')
	print()
	print(char)


if __name__ == '__main__':

	main()
