from definitions import names
from objects import tiles
import random


class Town (object):

	def __init__ (self, seed=None):

		self.seed = seed
		self.name = self.generate_name(self.seed)
		self.shop = False
		self.shop_items = []

	def generate_name (self, seed=None):

		random.seed(self.seed)

		name = []
		length = random.randint(3,5)

		for i in range(length):
			name.append(random.choice(names.characters))

		name.append(' Town')

		return ''.join(name).title()

	def add_shop (self):

		self.shop = True

	def text (self, position=None):

		out = ['You are in {}.\n'.format(self.name)]
		if self.shop == True:
			out.append('Among the tiny houses, you see a shop.\n')
		out.append('What would you like to do?')
		out = ''.join(out)

		return out

	def __str__ (self):

		return self.name
