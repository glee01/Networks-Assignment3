# UDP Client side
from socket import *
import sys
from time import time

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)

server_ip = sys.argv[1]
server_port = sys.argv[2]
n = int(sys.argv[3])
print("Pinging {}".format(server_ip))

count = 1
success = 0
fail = 0
min_time = 500.0
max_time = 0.0
sum_time = 0.0
while count <= n:
    try:
        message = "Ping {} This is a test message".format(count)
        send_time = time()
        client_socket.sendto(message.encode(), (server_ip, int(server_port)))

        recv_message, server_address = client_socket.recvfrom(2048)
        receive_time = time()
        elapsed_time = round((receive_time - send_time) * 1000,1)
        if elapsed_time <= min_time:
            min_time = elapsed_time
        if elapsed_time > max_time:
            max_time = elapsed_time
        sum_time += elapsed_time

        print("Reply from {}: {} time={}ms TTL=1".format(server_ip,recv_message.decode(),elapsed_time))
        success += 1
    except:
        print("Request timed out")
        fail +=1
    count +=1

print("\nPing Statistics for {}".format(server_ip))
lost = (float((fail))/float(n))*100.0
lost = str(lost) + "%"
print("\tSegments: Sent: {}, Received: {}, Lost: {} ({} Loss)".format(n,success,fail,lost))
print("Approximate round trip times in ms:\n\tMinimum = {}ms, Maximum = {}ms, Average = {}ms".format(min_time,max_time,sum_time/success))


client_socket.close()