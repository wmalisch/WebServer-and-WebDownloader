from socket import *
import sys

serverName = sys.argv[1]
port = int(sys.argv[2])
filePath = sys.argv[3]

# Set up the file name for the file to be downloaded, and the file to be sent to the server
if(filePath[0] =='/'):
    filePath = '.' + filePath
    newFile = filePath[1:len(filePath)-1]
if(filePath[0] != '.' and filePath[1] != '/'):
    filePath = './' + filePath
    newFile = filePath
if(filePath[0] == '.' and filePath[1] == '/'):
    newFile = filePath[2:len(filePath)-1]


clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,port))
request = "GET" + " " + filePath + " " + "HTTP/1.1" + "\r\n" + "Host:" + " " + serverName + "\r\n"
clientSocket.send(request.encode())
response = clientSocket.recv(1024).decode()
data = response.partition('\r\n\r\n')[0]
file = response.partition('\r\n\r\n')[2]
open(newFile,"wb")
print(data)

clientSocket.close()
