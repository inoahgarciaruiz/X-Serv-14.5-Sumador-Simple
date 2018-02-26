#!/usr/bin/python3

import random
import socket
import calculadora


"""
____________________________ Calculadora.py ____________________________

   Make a web app that makes a two-step sum.

   The program must be able to execute as:
      python sumApp.py

________________________________________________________________________

Author: Ainhoa Garcia-Ruiz Fuentes.       Date: 25/02/2018
Course: Servicios y Aplicaciones en Redes de Ordenadores.
Partially based on Simple HTTP Server by Jesus M. Gonzalez-Barahona
and Gregorio Robles:
https://github.com/CursosWeb/X-Serv-14.1-WebServer
"""

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

counter = 0
error = 0
try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        message = recvSocket.recv(2048)
        print('Request received:')
        print(message)

        resource = message.split()[1].decode("utf-8").split("/")[1]
        if resource != 'favicon.ico':
            try:
                if counter == 0:
                    s1 = float(resource)
                elif counter == 1:
                    s2 = float(resource)

            except ValueError:
                error = 1

        if resource != 'favicon.ico':
            if (error == 0 and counter == 0):
                answer = bytes('HTTP/1.1 200 OK\r\n\r\n' +
                               '<html><body><h1>Give me another one</h1>' +
                               '</body></html>\r\n', 'utf-8')
                counter = 1

            elif (error == 0 and counter == 1):
                c = calculadora.Calculadora(s1, s2)
                result = c.suma()
                aux = str(s1) + " + " + str(s2) + " = " + str(result)
                answer = bytes('HTTP/1.1 200 OK\r\n\r\n' +
                               '<html><body><h1>sumApp</h1><a>' + aux +
                               '</a></body></html>\r\n', 'utf-8')
                counter = 0

            elif (error == 1):
                answer = bytes('HTTP/1.1 400 Bad Request\r\n\r\n<html>' +
                               '<body><h1>[Usage:] http://localhost:1234/' +
                               '"s1/s2"</h1></body></html>\r\n', 'utf-8')
                counter = 0
                error = 0

        print('Answering back...')
        recvSocket.send(answer)
        recvSocket.close()


except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
