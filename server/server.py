from socket import *
port = 8000
str = "WORKED"


serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',port))
serverSocket.listen(1)
print("The server is ready to receive")
try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        sentenceNew = sentence.upper()
        connectionSocket.send(sentenceNew.encode())
        connectionSocket.close()
except KeyboardInterrupt:
    print('Server stoped')