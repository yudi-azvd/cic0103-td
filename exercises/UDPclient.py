import socket

def UDPclient(host, port):
  udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  server_info = (host, port)

  message = f'Hello, world! From {host}:{port}'
  udp_client.sendto(message.encode('utf8'), server_info)

  response, _ = udp_client.recvfrom(1024)

  print(response.decode('utf8'))

  udp_client.close()

  return