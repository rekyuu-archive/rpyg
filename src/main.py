from helpers import generators as gen
from helpers import debug
from objects import characters
import pickle, socket


"""
TODO:
- Add items (weapons, armor, consumables, key)
- Add enemies
- Add world generation
- Add battle handling
- Add specials
- Add initial generation and database handling
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


		# Starts the game.
		@listener(c)
		def start_function (m):
			return 'Please enter your name.'


		# Starts party creation.
		party = {}
		party_done = False
		while True:

			if party_done == True:
				break

			@listener(c)
			def party_entry (m):

				nonlocal party
				nonlocal party_done

				user = m['user']
				msg = m['msg']

				if msg.lower() == 'done':
					party_done = True
					return ( 'Party created!\n'
						+ 'Please enter a seed now, or type "none" to create a random seed.')
				else:
					if user in party:
						add_msg = 'Changed {}\'s name to {}.\n\n'.format(party[user]['name'], msg)
						party[user] = {'name': msg}
					else:
						party[user] = {'name': msg}
						add_msg = msg + ' has been added to the party.\n\n'

					return ( add_msg
						+ 'If anyone else would like to join, type your names now.\n'
						+ 'You can also change your name if you want.\n'
						+ 'If you are finished adding party members, type "done".'
						)


		# Generates characters and the world.
		@listener(c)
		def world_creation (m):

			nonlocal party

			user = m['user']
			msg = m['msg']

			if msg.lower() == 'none':
				seed = gen.seed(None)
			else:
				seed = gen.seed(msg)

			out = [
				'World created with seed ' + seed + '.\n\n',
				'Here are the party stats:\n\n'
			]

			for user in list(party.keys()):
				name = party[user]['name']
				char = gen.character(seed)
				stats = characters.Character(name, seed, char)
				party[user]['stats'] = stats
				out.append(str(stats))

			maze = gen.dungeon(3, 3, seed)
			print(debug.mazegen(maze))

			out = ''.join(out)
			return out


		# Closes the connection.
		c.close()
		print('-', addr)

		break


if __name__ == '__main__':

	main()
