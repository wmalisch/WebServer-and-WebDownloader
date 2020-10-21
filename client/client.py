from socket import *
import sys

serverName = sys.argv[1]
port = int(sys.argv[2])
filePath = sys.argv[3]

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,port))
request = "GET" + " " + filePath + " " + "HTTP/1.1" + "\r\n" + "Host:" + " " + serverName + "\r\n"
clientSocket.send(request.encode())
modifiedSentence = clientSocket.recv(5000)
print('From server: ',modifiedSentence.decode())
clientSocket.close()