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
def get_ivs (seed):

	random.seed(seed)
	ivs = []
	for i in range(5):
		ivs.append(random.randint(0,7))
	return ivs


# Returns the final stat using the following equation.
def get_stat (stat, iv, lv):

	return int(((((stat + iv) * 6) * lv) / (10)) + 5)


# Returns the final stat using the following equation.
def get_mp_stat (stat, lv):

	return int(get_stat(stat, 0, lv) / 3)


class Character (object):

	def __init__ (self, name, seed, rand):

		self.NAME 	= name
		self.SEED 	= seed
		self.RACE	= rand['race']
		self.CLASS	= rand['class']
		self.TITLE	= '{} the {} {}'.format(self.NAME, self.RACE, self.CLASS)

		# Base stats.
		self.IV					= get_ivs(self.SEED)
		self.LV					= 1
		self.XP					= 1
		self.BASE_HP			= 20
		self.BASE_ATTACK		= classes.roster[self.CLASS]['stats'][0]
		self.BASE_INTEL 		= classes.roster[self.CLASS]['stats'][1]
		self.BASE_MP	 		= 10
		self.BASE_DEFENSE		= classes.roster[self.CLASS]['stats'][2]
		self.BASE_SPEED 		= classes.roster[self.CLASS]['stats'][3]

		# Decorative header for __str__().
		header = []
		i = len(list(self.TITLE))
		while i > 0:
			header.append('=')
			i -= 1
		self.header = ''.join(header)

		# Initializes stats with IVs.
		self.update_stats()

	# Updates stats on __init__() and on level_up().
	def update_stats (self):

		self.HP			= get_stat(self.BASE_HP, self.IV[0], self.LV) + self.LV
		self.CUR_HP		= self.HP
		self.ATTACK		= get_stat(self.BASE_ATTACK, self.IV[1], self.LV)
		self.INTEL 		= get_stat(self.BASE_INTEL, self.IV[2], self.LV)
		self.MP	 		= get_mp_stat(self.BASE_INTEL, self.LV) + self.LV
		self.CUR_MP	 	= self.MP
		self.DEFENSE	= get_stat(self.BASE_DEFENSE, self.IV[3], self.LV)
		self.SPEED 		= get_stat(self.BASE_SPEED, self.IV[4], self.LV)

	# Called when XP is earned. Will cheack for level ups when called.
	def earn_xp (self, xp):

		self.XP += xp
		if get_level(self.XP) > self.LV:
			self.level_up()

	# Levels the character and updates stats.
	def level_up (self):

		self.LV = get_level(self.XP)
		self.update_stats()

	# Class readability.
	def __str__ (self):

		return (
			' ' + self.TITLE + '\n'
			+ ' ' + self.header	+ '\n'
			+ ' Level: ' + str(self.LV) + '\n'
			+ '    HP: ' + str(self.CUR_HP) + '/' + str(self.HP) + '\n'
			+ '    MP: ' + str(self.CUR_MP) + '/' + str(self.MP) + '\n'
			+ '   ATK: ' + str(self.ATTACK) + '\n'
			+ '   INT: ' + str(self.INTEL) + '\n'
			+ '   DEF: ' + str(self.DEFENSE) + '\n'
			+ '   SPD: ' + str(self.SPEED)
		)
