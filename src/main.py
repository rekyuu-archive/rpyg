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
- Port to some sort of JSON API or something???
- Add webui
"""


# Runs the main program.
def main ():

	print('Name your character.')
	name = input('> ')
	print('Seed? (Leave blank for a random seed)')
	io_seed = input('> ')

	seed = gen.seed(io_seed)
	char = gen.character(seed)

	print('Generating character {} with seed {}...'.format(name, seed))
	player = characters.Character(name, seed, char)

	print('Character created. Here are your stats:')
	print()
	print(player)


if __name__ == '__main__':

	main()
