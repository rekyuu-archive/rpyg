from helpers import generators as gen
from helpers import debug
from objects import characters


"""
TODO:
- Add items (weapons, armor, consumables, key)
- Add enemies
- Add world generation
- Add battle handling
- Add specials
- Add initial generation and database handling
- Port to some sort of netsocket API or something???
- Add webui
"""


# Runs the main program.
def main ():

	print('Name your character.')
	name = input('> ')
	print('How long should the dungeon be?')
	maze_x = int(input('> '))
	print('How tall should the dungeon be?')
	maze_y = int(input('> '))
	print('Seed? (Leave blank for a random seed)')
	io_seed = input('> ')

	seed = gen.seed(io_seed)
	char = gen.character(seed)

	print('Generating character {} with seed {}...'.format(name, seed))
	player = characters.Character(name, seed, char)
	print('Generating world with seed {}...\n'.format(seed))
	maze = gen.dungeon(maze_x, maze_y, seed)

	print('Character created. Here are your stats:\n')
	print(player, '\n')
	print('Here is the dungeon:\n')
	print(debug.mazegen(maze))


if __name__ == '__main__':

	main()
