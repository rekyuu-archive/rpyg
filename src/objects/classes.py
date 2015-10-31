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
class Class (object):

	def __init__ (self, name, ivs, attack, intel, defense, speed):

		self.NAME 				= name

		# Base stats.
		self.IV					= ivs
		self.LV					= 1
		self.XP					= 1
		self.BASE_HP			= 20
		self.BASE_ATTACK		= attack
		self.BASE_INTEL 		= intel
		self.BASE_MP	 		= 10
		self.BASE_DEFENSE		= defense
		self.BASE_SPEED 		= speed

		self.update_stats()

	def update_stats (self):

		self.HP			= get_stat(self.BASE_HP, self.IV[0], self.LV) + self.LV
		self.ATTACK		= get_stat(self.BASE_ATTACK, self.IV[1], self.LV)
		self.INTEL 		= get_stat(self.BASE_INTEL, self.IV[2], self.LV)
		self.MP	 		= get_mp_stat(self.BASE_INTEL, self.LV)
		self.DEFENSE	= get_stat(self.BASE_DEFENSE, self.IV[3], self.LV)
		self.SPEED 		= get_stat(self.BASE_SPEED, self.IV[4], self.LV)

	def earn_xp (self, xp):

		self.XP += xp
		if get_level(self.XP) > self.LV:
			self.level_up()

	def level_up (self):

		self.LV = get_level(self.XP)
		self.update_stats()

	def get_stats (self):

		print(
			'\n'
			+ '-- Level ' + str(self.LV) + ' --\n'
			+ 'Class: ' + self.NAME + '\n'
			+ '   HP: ' + str(self.HP) + '\n'
			+ '   MP: ' + str(self.MP) + '\n'
			+ '  ATK: ' + str(self.ATTACK) + '\n'
			+ '  INT: ' + str(self.INTEL) + '\n'
			+ '  DEF: ' + str(self.DEFENSE) + '\n'
			+ '  SPD: ' + str(self.SPEED) + '\n'
		)


class Warrior (Class):

	def __init__ (self, seed):

		self.seed = seed
		self.ivs = get_ivs(self.seed)
		Class.__init__(self, 'Warrior', self.ivs, 20, 10, 15, 15)


class Rogue (Class):

	def __init__ (self, seed):

		self.seed = seed
		self.ivs = get_ivs(self.seed)
		Class.__init__(self, 'Rogue', self.ivs, 20, 15, 10, 15)


class Barbarian (Class):

	def __init__ (self, seed):

		self.seed = seed
		self.ivs = get_ivs(self.seed)
		Class.__init__(self, 'Barbarian', self.ivs, 20, 15, 15, 10)


class Mage (Class):

	def __init__ (self, seed):

		self.seed = seed
		self.ivs = get_ivs(self.seed)
		Class.__init__(self, 'Mage', self.ivs, 10, 20, 15, 15)


class Ranger (Class):

	def __init__ (self, seed):

		self.seed = seed
		self.ivs = get_ivs(self.seed)
		Class.__init__(self, 'Ranger', self.ivs, 15, 20, 10, 15)


class Bard (Class):

	def __init__ (self, seed):

		self.seed = seed
		self.ivs = get_ivs(self.seed)
		Class.__init__(self, 'Bard', self.ivs, 15, 20, 15, 10)


class Paladin (Class):

	def __init__ (self, seed):

		self.seed = seed
		self.ivs = get_ivs(self.seed)
		Class.__init__(self, 'Paladin', self.ivs, 10, 15, 20, 15)


class Juggernaut (Class):

	def __init__ (self, seed):

		self.seed = seed
		self.ivs = get_ivs(self.seed)
		Class.__init__(self, 'Juggernaut', self.ivs, 15, 10, 20, 15)


class Tinkerer (Class):

	def __init__ (self, seed):

		self.seed = seed
		self.ivs = get_ivs(self.seed)
		Class.__init__(self, 'Tinkerer', self.ivs, 15, 15, 20, 10)


class Theif (Class):

	def __init__ (self, seed):

		self.seed = seed
		self.ivs = get_ivs(self.seed)
		Class.__init__(self, 'Theif', self.ivs, 10, 15, 15, 20)


class Brawler (Class):

	def __init__ (self, seed):

		self.seed = seed
		self.ivs = get_ivs(self.seed)
		Class.__init__(self, 'Brawler', self.ivs, 15, 10, 15, 20)


class Hunter (Class):

	def __init__ (self, seed):

		self.seed = seed
		self.ivs = get_ivs(self.seed)
		Class.__init__(self, 'Hunter', self.ivs, 15, 15, 10, 20)


roster = [
	'Warrior',
	'Rogue',
	'Barbarian',
	'Mage',
	'Ranger',
	'Bard',
	'Paladin',
	'Juggernaut',
	'Tinkerer',
	'Theif',
	'Brawler',
	'Hunter'
]
