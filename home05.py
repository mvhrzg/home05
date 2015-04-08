#!/usr/bin/python
__author__ = "mariana herzog & boris sarkisov"

"""Built on top of Dr. Dean Brock's Multiple Inheritance socket program"""

import socket
import SocketServer
import sys
import threading

PORT = int(sys.argv[1])

animal='bear'
color='brown'
global data

def diff(input):
	global animal
	global color

	if input[0:7] == '?animal':
		input=animal
#		clientout.write(input+"\r\n")
		print input
#		clientout.flush()
	if input[0:6] == '?color':
		input=color
#		clientout.write(input+"\r\n")
		print input
#		clientout.flush()
	if input[0:7] == 'animal=':
		animal = input[7:-1]
	if input[0:6] == 'color=':
		color = input[6:-1]
	data = input

class EchoRequestHandler(SocketServer.BaseRequestHandler):

    """ client handler class """
    def handle(self):
        """ client handler """
        clientsock = self.request
        print 'Connected to {0}'.format(clientsock.getpeername())
#	global clientin
#	global clientout

        clientin = clientsock.makefile('r')
        clientout = clientsock.makefile('w')
	linelock = threading.Lock()
#	linelock.acquire()
	data = clientin.readline()
#	linelock.release()	
        try:
	    while data:
		linelock.acquire()
#		clientout.write(diff(data))
		print "diff(data): ", diff(data), "\r\n"
	        clientout.flush()
		linelock.release()
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
    global data
    global linelock
    try:
	print 'Running on port %d'% (PORT)
        echoserverobj = EchoServer(('',PORT), EchoRequestHandler)
        echoserverobj.serve_forever()
	echoserver.listen(1)
	clientconn, clientaddr = echoserverobj.accept()
	childthr = threading.Thread(target=EchoRequestHandler, 
					args=(self, linelock))
	childthr.daemon = True
	childthr.start()

    except (EOFError, KeyboardInterrupt, IOError):
	if PORT >= 0 and PORT <= 1023:
		print ("Exception: Reserved Port Number. Try Again.")
        pass

if __name__ == "__main__":
    main()
