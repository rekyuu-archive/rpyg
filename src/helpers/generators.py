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

	# Generates the initial map grid.
	grid = []

	for i in range(y):
		row = []
		for j in range(x):
			walls =
			{
				'north' 	: True,
				'east'		: True,
				'south'		: True,
				'west'		: True
			}
			entities =
			{
				'items': [],
				'objects': [],
				'enemies': [],
				'npcs': []
			}
			row.append(tiles.DungeonTile(walls, entities))
		grid.append(row)

	# Picks a random starting entrance tile along the eastern ([0]) side.
	row = random.randint(0, len(maze) - 1)
	col = 0

	entrance = grid[row][col]
	entrance.visited()

	# Defines the selected tile and starts the stack.
	current = entrance
	stack = [(row, col)]

	while len(stack) > 0:
		directions 	= ['north', 'east', 'south', 'west']

		while len(directions) > 0:
			direction = random.choice(directions)
			
			if direction == 'north':
				if row - 1 >= 0:
					if grid[row - 1][col].VISITED == False:
						grid[row][col].remove_wall('north')
						row -= 1
						grid[row][col].remove_wall('south')
						grid[row][col].visted()
						stack.append((row, col))
					else:
						directions.remove('north')

			elif direction == 'east':
				if col + 1 <= len(grid[row]):
					if grid[row][col + 1].VISITED == False:
						grid[row][col].remove_wall('east')
						col += 1
						grid[row][col].remove_wall('west')
						grid[row][col].visted()
						stack.append((row, col))
					else:
						directions.remove('east')

			elif direction == 'south':
				if row + 1 <= len(grid):
					if grid[row + 1][col].VISITED == False:
						grid[row][col].remove_wall('south')
						row += 1
						grid[row][col].remove_wall('north')
						grid[row][col].visted()
						stack.append((row, col))
					else:
						directions.remove('south')

			elif direction == 'west':
				if col - 1 >= 0:
					if grid[row][col - 1].VISITED == False:
						grid[row][col].remove_wall('west')
						col -= 1
						grid[row][col].remove_wall('east')
						grid[row][col].visted()
						stack.append((row, col))
					else:
						directions.remove('west')

		if len(directions) == 0:
			stack.pop()
			row = stack[-1][0]
			col = stack[-1][1]
