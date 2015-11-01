import random


# Determines the level depending on the amount of experience.
def get_level (exp):

	if exp >= 10000:
		return 20
	elif exp >= 8410:
		return 19
	elif exp >= 7009:
		return 18
	elif exp >= 5782:
		return 17
	elif exp >= 4716:
		return 16
	elif exp >= 3798:
		return 15
	elif exp >= 3015:
		return 14
	elif exp >= 2353:
		return 13
	elif exp >= 1802:
		return 12
	elif exp >= 1350:
		return 11
	elif exp >= 985:
		return 10
	elif exp >= 696:
		return 9
	elif exp >= 473:
		return 8
	elif exp >= 306:
		return 7
	elif exp >= 186:
		return 6
	elif exp >= 104:
		return 5
	elif exp >= 52:
		return 4
	elif exp >= 22:
		return 3
	elif exp >= 7:
		return 2
	elif exp >= 1:
		return 1


# Returns five Individual Values for each stat.
def get_ivs (seed):

	random.seed(seed)
	ivs = []
	i = 4

	while i >= 0:
		ivs.append(random.randint(0,7))
		i -= 1

	return ivs


# Returns the final stat using the following equation.
def get_stat (stat, iv, lv):

	return int(((((stat + iv) * 6) * lv) / (10)) + 5)


# Returns the final stat using the following equation.
def get_mp_stat (stat, lv):

	return int(get_stat(stat, 0, lv) / 3)


# Blank class.
class BaseClass (object):

	def __init__ (self, name, seed, stat_list):

		self.NAME 				= name
		self.SEED				= seed

		# Base stats.
		self.IV					= get_ivs(self.SEED)
		self.LV					= 1
		self.XP					= 1
		self.BASE_HP			= 20
		self.BASE_ATTACK		= stat_list[0]
		self.BASE_INTEL 		= stat_list[1]
		self.BASE_MP	 		= 10
		self.BASE_DEFENSE		= stat_list[2]
		self.BASE_SPEED 		= stat_list[3]

		self.update_stats()

	def update_stats (self):

		self.HP			= get_stat(self.BASE_HP, self.IV[0], self.LV) + self.LV
		self.CUR_HP		= self.HP
		self.ATTACK		= get_stat(self.BASE_ATTACK, self.IV[1], self.LV)
		self.INTEL 		= get_stat(self.BASE_INTEL, self.IV[2], self.LV)
		self.MP	 		= get_mp_stat(self.BASE_INTEL, self.LV) + self.LV
		self.CUR_MP	 	= self.MP
		self.DEFENSE	= get_stat(self.BASE_DEFENSE, self.IV[3], self.LV)
		self.SPEED 		= get_stat(self.BASE_SPEED, self.IV[4], self.LV)

	def earn_xp (self, xp):

		self.XP += xp
		if get_level(self.XP) > self.LV:
			self.level_up()

	def level_up (self):

		self.LV = get_level(self.XP)
		self.update_stats()

	def __str__ (self):

		return (
			' Level: ' + str(self.LV) + '\n'
			+ '    HP: ' + str(self.CUR_HP) + '/' + str(self.HP) + '\n'
			+ '    MP: ' + str(self.CUR_MP) + '/' + str(self.MP) + '\n'
			+ '   ATK: ' + str(self.ATTACK) + '\n'
			+ '   INT: ' + str(self.INTEL) + '\n'
			+ '   DEF: ' + str(self.DEFENSE) + '\n'
			+ '   SPD: ' + str(self.SPEED)
		)
