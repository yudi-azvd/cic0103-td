from socket import *

server_name = 'localhost'
server_port = 1200

client_socket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence: ')

client_socket.sendto(message.encode(), (server_name, server_port))
modified_sentence, server_addr = client_socket.recvfrom(2048)

print(modified_sentence.decode()) 

client_socket.close()

