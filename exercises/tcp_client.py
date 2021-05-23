import socket

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def TCPclient(host, port):
  global tcp_client
  tcp_client.connect((host, port))

  message = f'Hello, world! From {host}:{port}'
  tcp_client.send(message.encode('utf-8'))

  response = tcp_client.recv(1024)
  tcp_client.close()

  print('Saida:', response.decode('utf-8'))
