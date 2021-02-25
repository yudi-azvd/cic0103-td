# Tirado do livro do James Kurose
# Problema 11
'''
Esse post aqui ajudou
https://stackoverflow.com/questions/10114224/how-to-properly-send-http-response-with-python-using-socket-library-only
'''

from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

http_response = '''
HTTP/1.1 200 OK
Date: Wed, 11 Apr 2012 21:29:04 GMT
Server: Python/6.6.6 (custom)
Content-Type: text/html

<html> <body> {} </body> </html>
'''

while True:
  connectionSocket, addr = serverSocket.accept()
  http_req = connectionSocket.recv(1024).decode()

  client_message = http_req.split()[1]

  # print('essa foi a frase:', http_req)
  print(client_message)

  message = http_response.format(client_message)

  capitalizedSentence = http_req.upper()
  # connectionSocket.send(capitalizedSentence.encode())
  connectionSocket.send(message.encode())
  connectionSocket.close()
