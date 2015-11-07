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
		self.VISITED = False

		# Tile walls definitions, defined by a dictionary of booleans or definitions.
		self.WALL_NORTH	= walls['north']
		self.WALL_EAST	= walls['east']
		self.WALL_SOUTH	= walls['south']
		self.WALL_WEST	= walls['west']

		# Defines if the tile is an entrance or exit.
		self.ENTRANCE	= False
		self.EXIT		= False

		# Lists of various entities on the tile.
		self.ITEMS 		= entities['items']
		self.OBJECTS 	= entities['objects']
		self.ENEMIES 	= entities['enemies']
		self.NPCS 		= entities['npcs']

	# Removes walls during generation.
	def remove_wall (self, wall):

		if wall == 'north':
			self.WALL_NORTH = False
		elif wall == 'east':
			self.WALL_EAST = False
		elif wall == 'south':
			self.WALL_SOUTH = False
		elif wall == 'west':
			self.WALL_WEST = False

	# Marks a tile as processed during generation.
	def visited (self):

		self.VISITED = True

	# Sets the tile as the entrance.
	def set_entrance (self):

		self.ENTRANCE = True

	# Sets the tile as the exit.
	def set_exit (self):

		self.EXIT = True

	# Sets a list of items on the tile.
	def set_items (self, items):

		self.ITEMS = items

	# Sets a list of interactable objects on the tile.
	def set_objects (self, objects):

		self.OBJECTS = objects

	# Sets a list of enemies on the tile.
	def set_enemies (self, enemies):

		self.ENEMIES = enemies

	# Sets a list of npcs on the tile.
	def set_npcs (self, npcs):

		self.NPCS = npcs

	# Text that displays as the player(s) enter the tile.
	def enter_text (self):

		pass
