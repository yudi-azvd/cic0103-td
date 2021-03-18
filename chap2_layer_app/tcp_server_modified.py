# Tirado do livro do James Kurose
# Problema 11
'''
Esse post aqui ajudou
https://stackoverflow.com/questions/10114224/how-to-properly-send-http-response-with-python-using-socket-library-only
'''

from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)

print('The server is ready to receive')

http_response = '''
HTTP/1.1 200 OK
Date: Wed, 11 Apr 2012 21:29:04 GMT
Server: Python/6.6.6 (custom)
Content-Type: text/html

<html> <body> {} </body> </html>
'''

while True:
  connection_socket, addr = server_socket.accept() # servidor vai esperar handshake de um cliente
  http_req = connection_socket.recv(1024).decode()

  client_message = http_req.split()[1]

  # print('essa foi a frase:', http_req)
  print(client_message)

  message = http_response.format(client_message)

  capitalizedSentence = http_req.upper()
  # connectionSocket.send(capitalizedSentence.encode())
  connection_socket.send(message.encode())
  connection_socket.close()
