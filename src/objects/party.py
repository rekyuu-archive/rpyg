from objects import maze, town


class Party (object):

	def __init__ (self, members):

		self.members = members
		self.facing = None
		self.world_position = None
		self.area_position = None

	def move_world (self, position):

		self.world_position = position
		print('~ Set world position to', position)

		if type(self.world_position) is maze.Maze:
			self.area_position = position.entrance
			self.facing = 'east'

		if type(self.world_position) is town.Town:
			self.area_position = (0, 0)
			self.facing = None

		print('~ Set area position to', self.area_position)

	def move_position (self, position):

		self.area_position = position

	def now_facing (self, facing):

		self.facing = facing
