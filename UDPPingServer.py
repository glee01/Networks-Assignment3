# UDP Server side

from socket import *

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind('',12000)

while True:
    message, client_address = server_socket.recvfrom(2048)

    server_socket.sendto(message, client_address)