''' 
Name: Rylan McAlister
UA ID: 010794211
'''

import sys

# Import socket library
from socket import *

# Set port number by converting argument string to integer
# If no arguments set a default port number
# Defaults
if sys.argv.__len__() != 2:
    serverPort = 5555
# Get port number from command line
else:
    serverPort = int(sys.argv[1])

# Choose SOCK_STREAM, which is TCP
# This is a welcome socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# The SO_REUSEADDR flag tells the kernel to reuse a local socket
# in TIME_WAIT state, without waiting for its natural timeout to expire.
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Start listening on specified port
serverSocket.bind(('', serverPort))

# Listener begins listening
serverSocket.listen(1)

#set initial balance to 100
balance = 100
print("The server is ready to receive")
connectionSocket, addr = serverSocket.accept()
while 1:


    #Recv and decode
    incomingInput = connectionSocket.recv(1024)
    userInput = incomingInput.decode('utf-8')
    print("Command: "+userInput)

    #Deposit money
    if userInput == "deposit":
        #Recv Decode and Cast
        incomingAmount = connectionSocket.recv(1024)
        userAmount = incomingAmount.decode('utf-8')
        try:
            userAmount = int(userAmount)
        except ValueError:
            error = "Error: Invalid number input"
            connectionSocket.send(error.encode('utf-8'))
        else: 
            #Negative Numbers 
            if userAmount < 0:
                error = "Error: Cannot deposit negative numbers"
                connectionSocket.send(error.encode('utf-8'))
            #Success
            else: 
                balance += userAmount
                connectionSocket.send(("Success! Deposited "+str(userAmount)+" dollars").encode('utf-8'))

    #Withdraw money
    elif userInput == "withdraw":
        #Recv Decode and Cast
        print("waiting for withdraw input...")
        incomingAmount = connectionSocket.recv(1024)
        userAmount = incomingAmount.decode('utf-8')

        try:
            userAmount = int(userAmount)
        except ValueError:
            error = "Error: Invalid number input"
            connectionSocket.send(error.encode('utf-8'))
        else: 
            #Negative Numbers
            if userAmount < 0:
                error = "Error: Cannot withdraw negative numbers"
                connectionSocket.send(error.encode('utf-8'))
            #Overdraft
            elif userAmount > balance:
                error = "Error: Cannot overdraft your account"
                connectionSocket.send(error.encode('utf-8'))
            #Success
            else: 
                balance -= userAmount
                connectionSocket.send(("Success! Withdrew "+str(userAmount)+" dollars").encode('utf-8'))

    #Checking balance
    elif userInput == "balance": 
        print("Retriving balance")
        connectionSocket.send(("Your current balance is: "+str(balance)+ " dollars").encode('utf-8'))
    
    #Log out user
    #Close connection to client but do not close welcome socket
    elif userInput == "logout":
        connectionSocket.close()
        connectionSocket, addr = serverSocket.accept()
        
    #Error
    else:
        connectionSocket.send("Error, please enter a proper command".encode('utf-8'))
  


