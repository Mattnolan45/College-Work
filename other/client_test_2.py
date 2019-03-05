import socket, threading, time


class Client(object):
	def __init__(self, name, address, port):
		self.name = name
		self.address = address
		self.port = port
		self.sock = None
		self.hand = []


	def create_socket(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = (self.address, self.port)
		print("Connecting to {}".format(server_address))
		self.sock.connect(server_address)

	def start(self):
		t1 = threading.Thread(target=self.receive_data, daemon=True)
		t2 = threading.Thread(target=self.send_data)
		t1.start()
		t2.start()

	def do_something(self):
		message = input("Enter something to send: ")
		return message

	def send_data(self):
		message = str(self.do_something())
		while True:
			if message == "disconnect":
				print("Disconnecting from server")
				self.sock.sendall(bytes(message, "utf-8"))
				self.sock.close()
				break
			else:
				self.sock.sendall(bytes(message, "utf-8"))
			message = str(self.do_something())


	def receive_data(self):
		while True:
			data = self.sock.recv(4096).decode("utf-8")

			print("\nRecieved {}\nEnter something to send: ".format(data))

def main():
	client = Client("Davy", "localhost", 10000)
	client.create_socket()
	client.start()

if __name__ == "__main__":
	main()
