#!/usr/bin/python
__author__ = "mariana herzog"

import socket
import sys
import threading
from sys import stdin, stdout

port = int(5000) #int(sys.argv[1])
host = 'localhost'
server = (host, port)
color='brown'
animal='bear'
linelock=threading.Lock()


def handle_data():
    global clientout

    message = input("-> ")
    while message != 'q':
        client.sendto(message.encode(), server)
        data = client.recv(1024).decode()
        print ('Received from server: ' + data)
        message = input(" -> ")
    # client.close()
    sys.exit()


def main():
    global client
    """ main routine """
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(server)
    except :
        # this means could not resolve the host
        stdout.write('there was an error resolving the host.\r\nexiting...')
        stdout.flush()
        sys.exit()
    print('Sucessfully connected to server\r\n')
    handle_data()

if __name__ == "__main__":
    main()