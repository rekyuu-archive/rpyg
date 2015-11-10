import pickle, socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 7794
connected = False

while True:
	if connected == False:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host, port))
			connected = True
		except:
			out = 'Error connecting to server. Is it running?'
			print('!', out)
			break

	elif connected == True:
		try:
			user = 'rekyuu'
			msg = input('> ')

			data = {'user': user, 'msg': msg}
			s.sendall(pickle.dumps(data))

			data = s.recv(4096).decode('utf8')
			print(data)
		except:
			connected = False
			out = 'Lost connection to server. Attempting to reconnect.'
			print('!', out)
