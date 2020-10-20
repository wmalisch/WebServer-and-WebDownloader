from socket import *
serverName = 'localhost'
port = 8000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,port))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From server: ',modifiedSentence.decode())
clientSocket.close()