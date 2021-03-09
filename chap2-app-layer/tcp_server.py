# -*- coding: utf-8 -*-
# Tirado do livro do James Kurose
# Problema 11

from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)  # stream de bits/socket TCP 
server_socket.bind(('', server_port))
server_socket.listen(1)

print('The server is ready to receive\n')

while True:
  # um novo socket é criado para cada comunicação com o cliente
  print('server waiting client...')
  connection_socket, addr = server_socket.accept() # servidor vai esperar handshake de um cliente
  print('client connected')

  sentence = connection_socket.recv(1024).decode()
  print('msg received:', sentence, '\n')

  capitalized_sentence = sentence.upper()

  connection_socket.send(capitalized_sentence.encode())
  connection_socket.close()
