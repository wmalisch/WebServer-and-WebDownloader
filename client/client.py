from socket import *
import sys

serverName = sys.argv[1]
port = int(sys.argv[2])
filePath = sys.argv[3]

# Set up the file name for the file to be downloaded, and the file to be sent to the server
if(filePath[0] =='/'):
    filePath = '.' + filePath
    newFile = filePath[1:len(filePath)]
if(filePath[0] != '.' and filePath[1] != '/'):
    filePath = './' + filePath
    newFile = filePath
if(filePath[0] == '.' and filePath[1] == '/'):
    newFile = filePath[2:len(filePath)]

# Make sure when we write new file, it is just the file name
newFile = newFile.rpartition('/')[2]


clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,port))
request = "GET" + " " + filePath + " " + "HTTP/1.1" + "\r\n" + "Host:" + " " + serverName + "\r\n"
clientSocket.send(request.encode())
response = clientSocket.recv(1024).decode()
data = response.partition('\r\n\r\n')[0]
file = response.partition('\r\n\r\n')[2]
print(data)
with open(newFile, "wb") as f:
    f.write(bytes(file, 'utf-8'))


clientSocket.close()
