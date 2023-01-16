# UDP Server side

from socket import *
from random import randint

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('',12000))

while True:
    message, client_address = server_socket.recvfrom(2048)
    r = randint(1,10)
    if r > 4:
        server_socket.sendto(message, client_address)