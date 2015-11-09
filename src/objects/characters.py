from definitions import classes
import random


# Determines the level depending on the amount of experience.
def get_level (xp):

	if xp >= 10000:
		return 20
	elif xp >= 8410:
		return 19
	elif xp >= 7009:
		return 18
	elif xp >= 5782:
		return 17
	elif xp >= 4716:
		return 16
	elif xp >= 3798:
		return 15
	elif xp >= 3015:
		return 14
	elif xp >= 2353:
		return 13
	elif xp >= 1802:
		return 12
	elif xp >= 1350:
		return 11
	elif xp >= 985:
		return 10
	elif xp >= 696:
		return 9
	elif xp >= 473:
		return 8
	elif xp >= 306:
		return 7
	elif xp >= 186:
		return 6
	elif xp >= 104:
		return 5
	elif xp >= 52:
		return 4
	elif xp >= 22:
		return 3
	elif xp >= 7:
		return 2
	elif xp >= 1:
		return 1


# Returns five Individual Values for each stat.
def get_ivs (name, seed):

	random.seed(name + seed)
	ivs = []
	for i in range(5):
		ivs.append(random.randint(0,7))
	return ivs


# Returns the final stat using the following equation.
def get_stat (stat, iv, lv):

	return int((stat + iv) * 6 * lv / 10 + 5)


# Returns the final stat using the following equation.
def get_mp_stat (stat, lv):

	return int(get_stat(stat, 0, lv) / 3)


# Character creation class.
class Character (object):

	def __init__ (self, name, seed, rand):

		self.name 		= name
		self.seed 		= seed
		self.race		= rand['race']
		self.char_class	= rand['class']
		self.title		= '{} the {} {}'.format(self.name, self.race, self.char_class)

		# Base stats.
		self.iv					= get_ivs(self.name, self.seed)
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

		self.hp			= get_stat(self.base_hp, self.iv[0], self.lv) + self.lv
		self.cur_hp		= self.hp
		self.attack		= get_stat(self.base_attack, self.iv[1], self.lv)
		self.intel 		= get_stat(self.base_intel, self.iv[2], self.lv)
		self.mp	 		= get_mp_stat(self.base_intel, self.lv) + self.lv
		self.cur_mp	 	= self.mp
		self.defense	= get_stat(self.base_defense, self.iv[3], self.lv)
		self.speed 		= get_stat(self.base_speed, self.iv[4], self.lv)

	# Called when XP is earned. Will cheack for level ups when called.
	def earn_xp (self, xp):

		self.xp += xp
		if get_level(self.xp) > self.lv:
			self.level_up()

	# Levels the character and updates stats.
	def level_up (self):

		self.lv = get_level(self.xp)
		self.update_stats()

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
