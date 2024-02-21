from socket import *
serverPort = 14000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    received_message = message.decode()
    # Count the number of characters in the received message
    characters = len(received_message)
    print("Number of characters received:", characters)
    modifiedMessage = received_message.upper() + f" ({characters} characters)"
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
