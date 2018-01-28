#!/usr/bin/python
__author__ = "mariana herzog & boris sarkisov"

"""Built on top of Dr. Dean Brock's Multiple Inheritance socket program"""

import SocketServer
import sys
import threading

PORT = int(sys.argv[1])
animal='bear'
color='brown'
linelock=threading.Lock()

def diff(input):
        global animal
        global color
        global linelock

        linelock.acquire()
        if input[0:7] == '?animal':
		input=animal
		clientout.write(input+"\r\n")
		print ("Sent: %s" % input)

	if input[0:6] == '?color':
		input=color
		clientout.write(input+"\r\n")
		print ("Sent: %s" % input)

	if input[0:7] == 'animal=':
		animal = input[7:-1]
		print ("Received: %s" % animal)

	if input[0:6] == 'color=':
		color = input[6:-1]
		print ("Received: %s" % color)

	linelock.release()

class EchoRequestHandler(SocketServer.BaseRequestHandler):

    """ client handler class """
    def handle(self):
	   global clientout

        """ client handler """
        clientsock = self.request
        print 'Connected to {0}'.format(clientsock.getpeername())


        clientin = clientsock.makefile('r')
        clientout = clientsock.makefile('w')

	data = clientin.readline()

        try:
	    while data:
		diff(data)
	        clientout.flush()
        	data = clientin.readline()

        except EOFError:
            pass
        clientin.close()
        clientout.close()

class EchoServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """ Threading echo server """
    pass

def main():
    """ main routine """
    try:
	   print 'Running on port %d'% (PORT)
        echoserverobj = EchoServer(('',PORT), EchoRequestHandler)
        echoserverobj.serve_forever()

    except (EOFError, KeyboardInterrupt, IOError):
        if PORT >= 0 and PORT <= 1023:
            print ("Exception: Reserved Port Number. Try Again.")
            pass

if __name__ == "__main__":
    main()
