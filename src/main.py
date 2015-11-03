from helpers import generators as gen
from objects import characters


"""
TODO:
- Add items (weapons, armor, consumables, key)
- Add enemies
- Add world generation
- Add battle handling
- Add specials
- Add initial generation and database handling
- Port to Telegram
- Add webui
"""


# Runs the main program.
def main ():

	print('Name your character.')
	name = input('> ')
	print('Seed? (Leave blank for a random seed)')
	io_seed = input('> ')

	seed = gen.seed(io_seed)
	rand = gen.randomizer(seed)

	print('Generating character {} with seed {}...'.format(name, seed))
	char = characters.Character(name, seed, rand)

	print('Character created. Here are your stats:')
	print()
	print(char)


if __name__ == '__main__':

	main()
