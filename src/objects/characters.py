from definitions import classes, races, xp
import random


# Character creation class.
class Character (object):

	def __init__ (self, name, seed):

		self.name 		= name
		self.seed 		= seed
		self.race		= self.race_generation(self.name, self.seed)
		self.char_class	= self.class_generation(self.name, self.seed)
		self.title		= '{} the {} {}'.format(self.name, self.race, self.char_class)

		# Base stats.
		self.iv					= self.get_ivs(self.name, self.seed)
		self.lv					= 1
		self.xp					= 1
		self.base_hp			= 20
		self.base_attack		= classes.roster[self.char_class]['stats'][0]
		self.base_intel 		= classes.roster[self.char_class]['stats'][1]
		self.base_mp	 		= 10
		self.base_defense		= classes.roster[self.char_class]['stats'][2]
		self.base_speed 		= classes.roster[self.char_class]['stats'][3]

		# Decorative header for __str__().
		header = []
		i = len(list(self.title))
		while i > 0:
			header.append('=')
			i -= 1
		self.header = ''.join(header)

		# Initializes stats with IVs.
		self.update_stats()

	# Updates stats on __init__() and on level_up().
	def update_stats (self):

		self.hp			= self.get_stat(self.base_hp, self.iv[0], self.lv) + self.lv
		self.cur_hp		= self.hp
		self.attack		= self.get_stat(self.base_attack, self.iv[1], self.lv)
		self.intel 		= self.get_stat(self.base_intel, self.iv[2], self.lv)
		self.mp	 		= self.get_mp_stat(self.base_intel, self.lv) + self.lv
		self.cur_mp	 	= self.mp
		self.defense	= self.get_stat(self.base_defense, self.iv[3], self.lv)
		self.speed 		= self.get_stat(self.base_speed, self.iv[4], self.lv)

	# Called when XP is earned. Will cheack for level ups when called.
	def earn_xp (self, xp):

		self.xp += xp
		if xp.get_level(self.xp) > self.lv:
			self.level_up()

	# Levels the character and updates stats.
	def level_up (self):

		self.lv = get_level(self.xp)
		self.update_stats()

	# Provides a random class for the character.
	def class_generation (self, name, seed):

		random.seed(name + seed)

		random_class = random.choice(sorted(list(classes.roster.keys())))
		return random_class

	# Provides a random race for the character.
	def race_generation (self, name, seed):

		random.seed(name + seed)

		random_race = races.roster[random.randint(0, len(races.roster) - 1)]
		return random_race

	# Returns five Individual Values for each stat.
	def get_ivs (self, name, seed):

		random.seed(name + seed)
		ivs = []
		for i in range(5):
			ivs.append(random.randint(0,7))
		return ivs

	# Returns the final stat using the following equation.
	def get_stat (self, stat, iv, lv):

		return int((stat + iv) * 6 * lv / 10 + 5)

	# Returns the final stat using the following equation.
	def get_mp_stat (self, stat, lv):

		return int(self.get_stat(stat, 0, lv) / 3)

	# Class readability.
	def __str__ (self):

		return (
			self.title + '\n'
			+ self.header + '\n'
			+ 'Level: ' + str(self.lv) + '\n'
			+ 'HP: ' + str(self.cur_hp) + '/' + str(self.hp) + '\n'
			+ 'MP: ' + str(self.cur_mp) + '/' + str(self.mp) + '\n'
			+ 'ATK: ' + str(self.attack) + '\n'
			+ 'INT: ' + str(self.intel) + '\n'
			+ 'DEF: ' + str(self.defense) + '\n'
			+ 'SPD: ' + str(self.speed)
		)
