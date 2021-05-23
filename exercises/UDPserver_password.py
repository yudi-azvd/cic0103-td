import socket

def is_password_valid(password):
  pass_len = len(password)
  has_valid_length = (6 <= pass_len) and (pass_len <= 32)
  has_lower_char = False
  has_upper_char = False
  has_number = False

  for char in password:
    if char.isupper():
      has_upper_char = True
    if char.islower():
      has_lower_char = True
    if char.isdigit():
      has_number = True
    if not char.isalnum() or char.isspace():
      return False

  return has_valid_length and has_lower_char and has_upper_char and has_number

def UDPserver (host,port):
  global udpd
  udpd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  server_info = (host, port)
  udpd.bind(server_info)

  while True:
    data, addr = udpd.recvfrom(1024)
    
    if not data:
      break

    password = data.decode('utf8')

    if is_password_valid(password):
      udpd.sendto('Senha valida.'.encode('utf8'), addr)
    else:
      udpd.sendto('Senha invalida!'.encode('utf8'), addr)

  udpd.close()
  return
