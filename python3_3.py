import socket
import sys
mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostname = ''
portNumber = 12345
print >>sys.stderr, "Starting up on ",hostname," on port ",portNumber
mySocket.bind((hostname,portNumber))
mySocket.listen(5)
while True:
    print >>sys.stderr, "Waiting for a connection"
    c,address = mySocket.accept()
    try:
        print "Got the address from", address
        while True:
            data = c.recv(16)
            print >>sys.stderr, " received ",data
            if data:
                print >>sys.stderr, "Sending data back to client"
                c.sendall(data)
            else:
                print >>sys.stderr, "No more data from ",address
                break
    finally:
        c.close()
