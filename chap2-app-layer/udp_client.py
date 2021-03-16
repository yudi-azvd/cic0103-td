from socket import *

server_name = 'localhost'
server_port = 12000

# A camada de transporte associa um numero de porta
# para o socket (1024 - 65535) do cliente automaticamente
# que nao esta sendo usado por nenhum outro processo UDP
# no host.
client_socket = socket(AF_INET, SOCK_DGRAM)
# client_socket.bind(('', 19157))

message = input('Input lowercase sentence: ')

client_socket.sendto(message.encode(), (server_name, server_port))

modified_sentence, server_addr = client_socket.recvfrom(2048)

print(modified_sentence.decode()) 

client_socket.close()

