#!/usr/bin/python3

import random
import socket
import calculadora



# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostname(), 1234))

# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        message = recvSocket.recv(2048)
        print('Request received:')
        print(message)

        try:
            [_ , s1, s2] = message.split()[1].decode("utf-8").split("/")
            s1_int = float(s1)
            s2_int = float(s2)
            error = 0
            c = calculadora.Calculadora(float(s1), float(s2))
        except ValueError:
            error = 1        
        if error == 0:
            c = calculadora.Calculadora(float(s1), float(s2))
            result = c.suma()
            aux = str(s1) + " + " + str(s2) + " = " + str(result) 
            answer = bytes('HTTP/1.1 200 OK\r\n\r\n' +
                     '<html><body><h1>sumApp</h1><a>' + aux +
                     '</a></body></html>\r\n', 'utf-8')
        else:
            answer = bytes('HTTP/1.1 400 Bad Request\r\n\r\n' +
                     '<html><body><h1>[Usage:] http://localhost:1234/"s1/s2"</h1><a>' +
                     '</a></body></html>\r\n', 'utf-8')

        print('Answering back...')
        recvSocket.send(answer)
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
