import sys

# Import socket library
from socket import *

# Set hostname or IP address from command line or default to localhost
# Set port number by converting argument string to integer or use default
# Use defaults
if sys.argv.__len__() != 3:
    serverName = 'localhost'
    serverPort = 5555
# Get from command line
else:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])

# Choose SOCK_STREAM, which is TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server using hostname/IP and port
clientSocket.connect((serverName, serverPort))

log_in = True

while log_in == True:
    #Get input and send it into socket to server
    userInput = input('Input command (deposit, withdraw, balance, logout): ')
    userInput = userInput.lower().strip()

    toServer = userInput.encode('utf-8')
    clientSocket.send(toServer)

    if userInput == "logout":
            clientSocket.close()
            exit()

    #Deposit money 
    elif userInput == "deposit":
        amountInput = input('Input amount to deposit (integer): ')
        amountToServer = amountInput.encode('utf-8')
        clientSocket.send(amountToServer)


    elif userInput == "withdraw":
        amountInput = input('Input amount to deposit (integer): ')
        amountToServer = amountInput.encode('utf-8')
        clientSocket.send(amountToServer)

    elif userInput == "balance":
        print("Getting balance")
 
    # Receive response from server via socket
    modifiedSentence = clientSocket.recv(1024)
    print('ATM: {0}'.format(modifiedSentence.decode('utf-8')))