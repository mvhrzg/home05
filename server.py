#!/usr/bin/python
__author__ = "mariana herzog"

import socket
import sys
import threading
import select
from sys import stdin, stdout

connections = []
# animal = 'bear'
# color = 'brown'
BUFFER_SIZE = 4096
host = 'localhost'
port = int(5000)
linelock = threading.Lock()

def get_first_char(string):
    return string[0]

def get_last_index(string):
	return len(string)

def send_response(client_conn_tuple, msg):
	linelock.acquire()
	# server.sendto(msg.encode(), client_conn_tuple)
	client.sendto(msg.encode(), client_conn_tuple)
	linelock.release()

	stdout.write('<< outgoing %s\r\n' % msg)
	stdout.flush()

def server_out(msg):
	stdout.write(msg + '\r\n')
	stdout.flush()

def start_server():
	global server

	try:
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server.bind((host, port))
		server.listen(3)
		server_out('Server listening on port 5000\r\n')
	except:
		server_out('Error starting server socket.')
		sys.exit()

def handle_clients():
	global client
	animal = 'bear'
	color = 'brown'
	response = ''

	client, address = server.accept()
	server_out("Connection from: %d\r\n" % client.getpeername()[1])
	
	while True:
		data = client.recv(BUFFER_SIZE).decode()
		if not data:
			break
		server_out('from %d: %s \r\n' % (client.getpeername()[1], data))
		assignment = data.find('=')
		last = get_last_index(data)

		# server_out('h_i_d: tuple = ' + str(client_conn_tuple) + '\r\n')

		# what is current value
		if get_first_char(data) == '?':
			if data[1:last] == 'animal':
				response = animal
			if data[1:last] == 'color':
				response = color

		elif assignment > -1:
			response = 'assignment ok\r\n'
			# server_out('%s' % data[0:(assignment)])
			# stdout.write('h_i_d: elif\r\n')
			if data[0:(assignment)] == 'animal':
				animal = data[(assignment+1):last]
			if data[0:(assignment)] == 'color':
				color = data[(assignment+1):last]
		client.sendto(response.encode(), client.getpeername())

	client.close()

def main():
	start_server()
	handle_clients()

if __name__ == "__main__":
    main()