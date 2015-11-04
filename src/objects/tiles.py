# Defines a series of tiles with walls.
class DungeonTile (object):

	def __init__ (self, walls, entities):

		# Indentifies an identified tile for maze generation.
		self.VISITED = False

		# Tile walls definitions, defined by a dictionary of booleans or definitions.
		self.WALL_NORTH	= walls['north']
		self.WALL_EAST	= walls['east']
		self.WALL_SOUTH	= walls['south']
		self.WALL_WEST	= walls['west']

		# Defines a list of items on the tile.
		self.ITEMS = entities['items']

		# Defines a list of interactable objects on the tile.
		self.OBJECTS = entities['objects']

		# Defines a list of enemies on the tile.
		self.ENEMIES = entities['enemies']

		# Defines a list of NPCs on the tile.
		self.NPCS = entities['npcs']

	def remove_wall (self, wall):

		if wall == 'north':
			self.WALL_NORTH = False
		elif wall == 'east':
			self.WALL_EAST = False
		elif wall == 'south':
			self.WALL_SOUTH = False
		elif wall == 'west':
			self.WALL_WEST = False

	def visited (self):

		self.VISITED = True

	def enter_text (self):

		pass


class TownTile (object):

	def __init__ (self):

		pass
