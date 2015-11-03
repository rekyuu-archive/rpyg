from definitions import classes, races
from objects import tiles
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
def character (seed=None):

	random.seed(seed)

	random_race = race_list[random.randint(0, len(race_list) - 1)]
	random_class = random.choice(sorted(list(class_list.keys())))
	return {'race': random_race, 'class': random_class}


# Generates a random dungeon map.
def dungeon (x, y, seed=None):

	"""
	Example of intended generation:

	world = dungeon(3,3)
	[
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]
	world[0][1] = 2

	@ = Player
	X = Enemy
	& = Boss
	$ = Loot
	~ = Key
	% = NPC
	# = Locked door (requires key)
	: = Entrance / Exit (randomly placed)
		- Exit should be locked until the boss is destroyed

	+---+---+---+
	| $   X | ~ |
	+---+   +   +
	: @   %     :
	+   +---+   +
	| X | & #   |
	+---+---+---+
	"""

	random.seed(seed)
	dungeon_map = []

	for i in range(y):

		row = []

		for j in range(x):

			walls = {
				'north' 	: False,
				'east'		: False,
				'south'		: False,
				'west'		: False
			}

			entities = {
				'items' = [],
				'objects' = [],
				'enemies' = [],
				'npcs' = []
			}

			row.append(tiles.DungeonTile(walls, entities))

		dungeon_map.append(row)
