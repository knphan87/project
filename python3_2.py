import socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('www.pythonlearn.com', 80))
mySocket.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    myData = mySocket.recv(512)
    if(len(myData) < 1):
        break
    print myData
mySocket.close()
