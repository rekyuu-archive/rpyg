from objects import mazes, towns


class Party (object):

	def __init__ (self, members):

		self.members = members
		self.world_position = None
		self.area_position = None

	def move_world (self, position):

		self.world_position = position
		print('~ Set world position to', position)

		if type(self.world_position) is mazes.Maze:
			self.area_position = position.entrance
			self.facing = 'east'

		if type(self.world_position) is towns.Town:
			self.area_position = (0, 0)
			self.facing = None

		print('~ Set area position to', self.area_position)

	def move_position (self, position):

		self.area_position = position

	def now_facing (self, facing):

		self.facing = facing
