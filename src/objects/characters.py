import classes, races
import random


class_list 		= classes.roster

class_obj		= {
	'Warrior'		: classes.Warrior,
	'Rogue'			: classes.Rogue,
	'Barbarian'		: classes.Barbarian,
	'Mage'			: classes.Mage,
	'Ranger'		: classes.Ranger,
	'Bard'			: classes.Bard,
	'Paladin'		: classes.Paladin,
	'Juggernaut'	: classes.Juggernaut,
	'Tinkerer'		: classes.Tinkerer,
	'Theif'			: classes.Theif,
	'Brawler'		: classes.Brawler,
	'Hunter'		: classes.Hunter
}

race_list 		= races.roster


def seed_gen (seed=None):

	if seed == None:
		seed = []
		i = 8
		while i >= 0:
			seed.append(str(random.randint(0,9)))
			i -= 1
		return int(''.join(seed))
	else:
		return seed


def randomizer (seed):

	random.seed(seed)

	random_race = race_list[random.randint(0, len(race_list) - 1)]
	random_class = class_list[random.randint(0, len(class_list) - 1)]
	return {'race': random_race, 'class': random_class}


class Character (object):

	def __init__ (self, name, seed=None):

		self.seed	= seed_gen(seed)
		self.char	= randomizer(self.seed)

		self.NAME 	= name
		self.RACE	= self.char['race']
		self.CLASS	= self.char['class']
		self.TITLE	= '{0} the {1} {2}'.format(self.NAME, self.RACE, self.CLASS)
		self.STATS	= class_obj[self.CLASS](self.seed)
