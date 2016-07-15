import socket
import sys
mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostname = ''
portNumber = 12345
print >>sys.stderr, "connecting to address ",hostname, " on port ",portNumber
mySocket.connect((hostname,portNumber))
try:
    message = " This is the test message. It will be repeated!"
    print >>sys.stderr, "sending ",message
    mySocket.sendall(message)
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = mySocket.recv(16)
        amount_received += len(data)
        print >> sys.stderr, "recived ",data
finally:
    print >>sys.stderr,"closing socket"
    mySocket.close()
