from socket import *
serverName = "192.168.0.103"
serverPort = 14000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Input lowercase sentence:")
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()