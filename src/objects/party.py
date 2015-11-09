class Party (object):

	def __init__ (self, members):

		self.members = members
		self.position = None

	def move (self, position):

		self.position = position
