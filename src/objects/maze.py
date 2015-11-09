from objects import tiles
import random


class Maze (object):

	def __init__ (self, width, height, seed):

		self.seed = seed
		self.width = width
		self.height = height
		self.tiles = self.generate_maze(self.seed)
		self.biome = 'castle'
		self.entrance = None
		self.exit = None

	def generate_maze (self, seed):

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

		x = self.width
		y = self.height

		random.seed(self.seed)

		# Generates the initial map grid.
		grid = []

		for i in range(y):
			row = []
			for j in range(x):
				walls =	{
					'north' 	: True,
					'east'		: True,
					'south'		: True,
					'west'		: True
				}
				entities = {
					'items': [],
					'objects': [],
					'enemies': [],
					'npcs': []
				}
				row.append(tiles.DungeonTile(walls, entities))
			grid.append(row)

		# Picks a random starting entrance tile along the western ([0]) side.
		row = random.randint(0, len(grid) - 1)
		col = 0

		self.entrance = (row, col)
		entrance = grid[row][col]
		entrance.set_entrance()
		entrance.visit()

		# Defines the selected tile and starts the stack.
		stack = [(row, col)]

		while len(stack) > 0:
			directions 	= ['north', 'east', 'south', 'west']

			while len(directions) > 0:
				direction = random.choice(directions)

				if direction == 'north':
					if row - 1 >= 0:
						if grid[row - 1][col].visited == False:
							grid[row][col].remove_wall('north')
							row -= 1
							grid[row][col].remove_wall('south')
							grid[row][col].visit()
							stack.append((row, col))
							break
						else:
							directions.remove('north')
					else:
						directions.remove('north')

				elif direction == 'east':
					if col + 1 <= len(grid[row]) - 1:
						if grid[row][col + 1].visited == False:
							grid[row][col].remove_wall('east')
							col += 1
							grid[row][col].remove_wall('west')
							grid[row][col].visit()
							stack.append((row, col))
							break
						else:
							directions.remove('east')
					else:
						directions.remove('east')

				elif direction == 'south':
					if row + 1 <= len(grid) - 1:
						if grid[row + 1][col].visited == False:
							grid[row][col].remove_wall('south')
							row += 1
							grid[row][col].remove_wall('north')
							grid[row][col].visit()
							stack.append((row, col))
							break
						else:
							directions.remove('south')
					else:
						directions.remove('south')

				elif direction == 'west':
					if col - 1 >= 0:
						if grid[row][col - 1].visited == False:
							grid[row][col].remove_wall('west')
							col -= 1
							grid[row][col].remove_wall('east')
							grid[row][col].visit()
							stack.append((row, col))
							break
						else:
							directions.remove('west')
					else:
						directions.remove('west')

			if len(directions) == 0:
				stack.pop()

				if len(stack) > 0:
					row = stack[-1][0]
					col = stack[-1][1]

		# Picks a random exit tile along the eastern ([-1]) side.
		row = random.randint(0, len(grid) - 1)
		self.exit = (row, -1)
		exit = grid[row][-1]
		exit.set_exit()

		return grid

	def __str__ (self):

		maze = self.tiles

		width = len(maze[0])
		height = len(maze)

		x_border = [' ']
		for i in range(width):
			x_border.append('+---')
		x_border.append('+\n')
		x_border = ''.join(x_border)

		inner = []
		for row in maze:
			if row[0].entrance == True:
				inner.append('  ')
			else:
				inner.append(' |')
			for tile in row:
				if tile.wall_east == True:
					if tile.exit == True:
						inner.append('    ')
					else:
						inner.append('   |')
				else:
					inner.append('    ')
			inner.append('\n')
			inner.append(' +')
			for tile in row:
				if tile.wall_south == True:
					inner.append('---+')
				else:
					inner.append('   +')
			inner.append('\n')

		inner = ''.join(inner)

		return (
			x_border
			+ inner
		)
