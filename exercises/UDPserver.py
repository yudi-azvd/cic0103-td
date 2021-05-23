import socket

def UDPserver(host, port):
  udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  server_info = (host, port)
  udp_server.bind(server_info)

  expected_msg = f'Hello, world! From {host}:{port}'

  while True:
    data, addr = udp_server.recvfrom(1024)

    got_message = data.decode('utf8')

    if not data:
      break

    if expected_msg != got_message:
      print('Servidor nao recebeu a mensagem correta')
      udp_server.sendto('Erro'.encode('utf8'), addr)
      break
  
    print('Servidor recebeu a mensagem correta')
    udp_server.sendto('Sucesso'.encode('utf8'), addr)
  
  udp_server.close()
  return