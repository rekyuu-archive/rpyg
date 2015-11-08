import auth, pickle, socket, telebot, time

# Telegram Bot API Key.
bot = telebot.TeleBot(auth.telegram)


# Socket definitions.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 7794
connected = False


@bot.message_handler(commands=['r', 'rp', 'rpg'])
def rpg_handler (m):
	global connected
	global s

	while True:
		if connected == False:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((host, port))
				connected = True
			except:
				out = 'Error connecting to server. Is it running?'
				bot.send_message(m.chat.id, out)
				print('!', out)
				break

		elif connected == True:
			try:
				msg = m.text.split(' ', 1)[1]
				user = m.from_user.username
				if user is None:
					user = m.from_user.first_name

				data = {'user': user, 'msg': msg}
				s.sendall(pickle.dumps(data))
				print('>', user + ':', msg)

				data = s.recv(4096).decode('utf8')
				print('<', data)
				bot.send_message(m.chat.id, data)
				break
			except:
				connected = False
				out = 'Lost connection to server. Attempting to reconnect.'
				bot.send_message(m.chat.id, out)


bot.polling(none_stop=True)
print('Kuma! Kuma~!')
while True:
	time.sleep(100)
