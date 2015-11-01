from definitions import classes as class_defs
from . import classes


class Character (object):

	def __init__ (self, name, seed, rand):

		self.NAME 	= name
		self.SEED 	= seed
		self.RACE	= rand['race']
		self.CLASS	= rand['class']
		self.TITLE	= '{0} the {1} {2}'.format(self.NAME, self.RACE, self.CLASS)
		self.STATS	= classes.BaseClass(self.CLASS, self.SEED, class_defs.roster[self.CLASS]['stats'])

		header = []
		i = len(list(self.TITLE))
		while i > 0:
			header.append('=')
			i -= 1
		self.header = ''.join(header)

	def __str__ (self):
		return (
			' ' + self.TITLE + '\n'
			+ ' '
			+ self.header
			+ '\n'
			+ str(self.STATS)
		)
