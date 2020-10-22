from socket import *
import os
import re
PORT = 8000
STR = "WORKED"


serverSocket = socket(AF_INET,SOCK_STREAM)
HOST = gethostbyname(gethostname())
serverSocket.bind((HOST,PORT))
serverSocket.listen(1)
print("The server is ready to receive")
print("Server Host: ", HOST)
print("Port: ", PORT)
try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        client = connectionSocket.recv(1024).decode()
        data = client.split("\n")
        path = re.search(' (.+?) ',data[0]).group(1)
        request = data[0].partition(' ')[0]
        ft = path.rpartition('.')[2]
        version = data[0].rpartition(' ')[2]
            
        # File requested does not exist
        if(os.path.isfile(path) != True):
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "\r\n"
            response += "<html><body><h1>Not Found</h1>The requested URL was not found on this server</body></html>\r\n\r\n"
            connectionSocket.send(response.encode())
        # File requested 
        elif(request != "GET"):
            response = "HTTP/1.1 501 Not Found\r\n"
            response = "\r\n"
            response += "<html><body><h1>Method Not Implemented</h1>Invalid method in request</body></html>\r\n\r\n"
            connectionSocket.send(response.encode())
        elif(version != 'HTTP/1.1\r'):
            response = "HTTP/1.1 501 Not Found\r\n"
            response = "\r\n"
            response += "<html><body><h1>Version Not Supported</h1>This web server only supports HTTP/1.1 </body></html>\r\n\r\n"
            connectionSocket.send(response.encode())
        else:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Length: "
            response += str(os.path.getsize(path))
            response += "\r\n"
            response += "Content-Type: "
            response += ft
            response += "\r\n\r\n"
            file = open(path, "rb")
            fb = file.read(os.path.getsize(path))
            response += str(fb)
            response += "\r\n\r\n"
            connectionSocket.send(response.encode())
        connectionSocket.close()
# Allow user to stop server on ctrl C or some other keyboard interrupt
except KeyboardInterrupt:
        print('\nServer Stopped')
        