# Default datasets for dungeon tiles.
walls =	{
	'north' 	: True,
	'east'		: True,
	'south'		: True,
	'west'		: True
}

entities = {
	'items'		: [],
	'objects'	: [],
	'enemies'	: [],
	'npcs'		: []
}

# Defines a series of tiles with walls.
class DungeonTile (object):

	def __init__ (self, walls=walls, entities=entities):

		# Indentifies an identified tile for maze generation.
		self.visited = False

		# Tile walls definitions, defined by a dictionary of booleans or definitions.
		self.wall_north	= walls['north']
		self.wall_east	= walls['east']
		self.wall_south	= walls['south']
		self.wall_west	= walls['west']

		# Defines if the tile is an entrance or exit.
		self.entrance	= False
		self.exit		= False

		# Lists of various entities on the tile.
		self.items 		= entities['items']
		self.objects 	= entities['objects']
		self.enemies 	= entities['enemies']
		self.npcs 		= entities['npcs']

	# Removes walls during generation.
	def remove_wall (self, wall):

		if wall == 'north':
			self.wall_north = False
		elif wall == 'east':
			self.wall_east = False
		elif wall == 'south':
			self.wall_south = False
		elif wall == 'west':
			self.wall_west = False

	# Marks a tile as processed during generation.
	def visit (self):

		self.visited = True

	# Sets the tile as the entrance.
	def set_entrance (self):

		self.entrance = True

	# Sets the tile as the exit.
	def set_exit (self):

		self.exit = True

	# Sets a list of items on the tile.
	def set_items (self, items):

		self.items = items

	# Sets a list of interactable objects on the tile.
	def set_objects (self, objects):

		self.objects = objects

	# Sets a list of enemies on the tile.
	def set_enemies (self, enemies):

		self.enemies = enemies

	# Sets a list of npcs on the tile.
	def set_npcs (self, npcs):

		self.npcs = npcs

	# Text that displays as the player(s) enter the tile.
	def enter_text (self):

		pass
