import socket, threading, sys

class Server(object):

	def __init__(self, address, port):
		self.address = address		# ip address of server
		self.port = port			# port number of server
		self.connections = []		# list of all connected players
		self.sock = None			# initialize socket

	def create_socket(self):											# create socket and bind to server address
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = (self.address, self.port)
		print("Binding to {}".format(server_address))
		self.sock.bind(server_address)


	def handle_data(self, connection):									# takes data from player, sends it back to each player.
		data = connection.recv(4096).decode("utf-8")					# get data from player
		while True:
			if data == "disconnect":									# remove player from player_list when they enter "disconnect"
				self.connections.remove(connection)
				print("Player disconnected from server")
				break
			else:														# Otherwise take the data and send it back to all players
				for conn in self.connections:
					conn.sendall(bytes(str(data), "utf-8"))
					print(data)
				data = connection.recv(4096).decode("utf-8")

		if len(self.connections) == 0:									# If the last player has disconnected, close the socket and end server
			print("Game over")
		self.sock.close()
		#sys.exit()


	def listen_for_connections(self):									# listen for players trying to connect to the server
		while True:
			try:
				self.sock.listen(4)
				connection, client_addresss = self.sock.accept()		
				print("New connection from {}".format(client_addresss))
				self.connections.append(connection)

				t = threading.Thread(target=self.handle_data, args=(connection,))
				t.start()

				if len(self.connections) == 4:							# if 4 players connect, stop accepting connection requests
					print("Game is now full, stop accepting connections")
					break
			except:
				pass

def main():
	server = Server("localhost", 10000)
	server.create_socket()
	server.listen_for_connections()

if __name__ == "__main__":
	main()
