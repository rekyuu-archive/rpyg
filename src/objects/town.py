from definitions import names
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

		return ''.join(name).title()

	def add_shop (self):

		self.shop = True

