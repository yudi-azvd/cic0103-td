import socket

def TCPserver(host, port):
  tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  tcp_server.bind((host, port))
  tcp_server.listen()
  conn, addr = tcp_server.accept()

  expected_message = f'Hello, world! From {host}:{port}'

  while True:
    data = conn.recv(1024)
    got_message = data.decode('utf8')

    if not data:
      break

    if expected_message != got_message:
      print('Servidor nao recebeu a mensagem correta')
      conn.sendall('Erro'.encode('utf8'))
      break
  
    print('Servidor recebeu a mensagem correta')
    conn.sendall('Sucesso'.encode('utf8'))

  conn.close()
  return
