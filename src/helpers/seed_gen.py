import random


# Generates a 8-digit seed if one was not provided.
def seed (seed=None):

	if seed == None or seed == '':
		seed = []
		for i in range(8):
			seed.append(str(random.randint(0,9)))
		return ''.join(seed)
	else:
		return seed

