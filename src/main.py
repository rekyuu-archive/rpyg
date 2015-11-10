from definitions import directions
from helpers import seed_gen
from objects import characters, mazes, parties, towns, worlds
import pickle, socket

direction = directions.Facing


"""
TODO:
- Add items (weapons, armor, consumables, key)
- Add enemies
- Add item and enemy placement
- Add battle handling
- Add special moves
- Add database handling
- Add webui
"""


def listener (c):

	def decorator (fn):

		print('= Listening...')

		while True:

			# Receives data from the client.
			data = c.recv(4096)

			if data:
				data = pickle.loads(data)
				print('<', data['user'] + ':', data['msg'])

				message = fn(data)
				c.send(bytes(message, 'utf8'))
				print('>', message)

				break

	return decorator


def adventure (c):

	# Starts the game.
	@listener(c)
	def start_function (m):
		return 'Please enter your name.'


	# Starts party creation.
	members = {}
	party_done = False
	while True:

		if party_done == True:
			break

		@listener(c)
		def party_entry (m):

			nonlocal members
			nonlocal party_done

			user = m['user']
			msg = m['msg']

			if msg.lower() == 'done':
				party_done = True
				return (
					'Party created!\n'
					+ 'Send the extension of the base size of the world.\n'
					+ 'Default world size is 3 towns and 3 dungeons.'
				)

			else:
				if user in members:
					add_msg = 'Changed {}\'s name to {}.\n\n'.format(members[user]['name'], msg)
					members[user] = {'name': msg}
				else:
					members[user] = {'name': msg}
					add_msg = msg + ' has been added to the party.\n\n'

				return (
					add_msg
					+ 'If anyone else would like to join, type your names now.\n'
					+ 'You can also change your name if you want.\n'
					+ 'If you are finished adding party members, type "done".'
				)


	world_size = 3
	world_size_done = False
	# Determines base world size.
	while True:

		if world_size_done == True:
			break

		@listener(c)
		def world_size_definition (m):

			nonlocal world_size
			nonlocal world_size_done

			user = m['user']
			msg = m['msg']

			try:
				size = int(msg)
				world_size += size
				world_size_done = True
				return (
					'Now send an extension of the base size of the rooms.\n'
					+ 'Default base size is 3.'
				)
			except:
				return 'Please be sure to send a single number.'


	room_size = 1
	room_size_done = False
	# Determines base world size.
	while True:

		if room_size_done == True:
			break

		@listener(c)
		def world_size_definition (m):

			nonlocal room_size
			nonlocal room_size_done

			user = m['user']
			msg = m['msg']

			try:
				size = int(msg)
				room_size += size
				room_size_done = True
				return 'Please enter a seed, or type "none" to create a random seed.'
			except:
				return 'Please be sure to send a single number.'


	world = None
	# Generates characters and the world.
	@listener(c)
	def world_creation (m):

		nonlocal members
		nonlocal world

		user = m['user']
		msg = m['msg']

		if msg.lower() == 'none':
			seed = seed_gen.seed(None)
		else:
			seed = seed_gen.seed(msg)

		out = [
			'World created with seed ' + seed + '.\n\n',
			'Here are the party stats:'
		]

		# Party generation.
		for member in members:
			name = members[member]['name']
			stats = characters.Character(name, seed)
			members[member]['stats'] = stats
			out.append('\n\n' + str(stats))

		# World generation.
		world = worlds.World(world_size, room_size, seed)

		out.append('\n\n' + world.areas[0].text())

		out = ''.join(out)
		return out

	party = parties.Party(members)
	party.move_world(world.areas[0])

	adventure_done = False
	# Main adventure.
	while True:

		if adventure_done == True:
			break

		@listener(c)
		def adventure (m):

			nonlocal party
			nonlocal world
			nonlocal adventure_done

			msg = m['msg'].lower()
			user = m['user']
			out = ''

			if msg == 'help':
				out = 'Ha, you wish!'

			elif type(party.world_position) is towns.Town:

				if msg == 'leave':
					next_area = world.areas.index(party.world_position) + 1
					party.move_world(world.areas[next_area])
					out = party.world_position.text(party.area_position)

			elif type(party.world_position) is mazes.Maze:

				row = party.area_position[0]
				col = party.area_position[1]

				if msg == 'forward':
					if party.facing is direction.north:
						msg = 'north'
					if party.facing is direction.east:
						msg = 'east'
					if party.facing is direction.south:
						msg = 'south'
					if party.facing is direction.west:
						msg = 'west'

				if msg == 'backward':
					if party.facing is direction.north:
						msg = 'south'
					if party.facing is direction.east:
						msg = 'west'
					if party.facing is direction.south:
						msg = 'north'
					if party.facing is direction.west:
						msg = 'east'

				if msg == 'left':
					if party.facing is direction.north:
						msg = 'west'
					if party.facing is direction.east:
						msg = 'north'
					if party.facing is direction.south:
						msg = 'east'
					if party.facing is direction.west:
						msg = 'south'

				if msg == 'right':
					if party.facing is direction.north:
						msg = 'east'
					if party.facing is direction.east:
						msg = 'south'
					if party.facing is direction.south:
						msg = 'west'
					if party.facing is direction.west:
						msg = 'north'

				if msg == 'north':
					if party.world_position.tiles[row][col].wall_north:
						out = 'You cannot go that way.'
					else:
						party.move_position((row - 1, col))
						party.now_facing(direction.north)
						out = ['You moved north.\n']
						out.append(party.world_position.text(party.area_position))
						out = ''.join(out)

				if msg == 'east':
					if party.world_position.tiles[row][col].wall_east:
						out = 'You cannot go that way.'
					else:
						party.move_position((row, col + 1))
						party.now_facing(direction.east)
						out = ['You moved east.\n']
						out.append(party.world_position.text(party.area_position))
						out = ''.join(out)

				if msg == 'south':
					if party.world_position.tiles[row][col].wall_south:
						out = 'You cannot go that way.'
					else:
						party.move_position((row + 1, col))
						party.now_facing(direction.south)
						out = ['You moved south.\n']
						out.append(party.world_position.text(party.area_position))
						out = ''.join(out)

				if msg == 'west':
					if party.world_position.tiles[row][col].wall_west:
						out = 'You cannot go that way.'
					else:
						party.move_position((row, col - 1))
						party.now_facing(direction.west)
						out = ['You moved west.\n']
						out.append(party.world_position.text(party.area_position))
						out = ''.join(out)

				if msg in ['exit', 'leave']:
					if party.world_position.tiles[row][col].exit:
						next_area = world.areas.index(party.world_position) + 1
						party.move_world(world.areas[next_area])
						out = party.world_position.text(party.area_position)
					elif party.world_position.tiles[row][col].entrance:
						next_area = world.areas.index(party.world_position) - 1
						party.move_world(world.areas[next_area])
						out = party.world_position.text(party.area_position)
					else:
						out = 'You are not at an exit.'

			if out == '':
				out = 'I do not understand the command.'

			return out


# Runs the main program.
def main ():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	port = 7794

	# Binds the server to address and port.
	s.bind((host, port))

	# Listens for a client.
	s.listen(1)
	print('= Waiting for clients...')

	while True:

		# Accepts a connection.
		c, addr = s.accept()
		print('+', addr)

		try:
			adventure(c)

		except:
			print('!', 'Lost connection. Closing socket.')

		finally:
			# Closes the connection.
			c.close()
			print('-', addr)


if __name__ == '__main__':

	main()
