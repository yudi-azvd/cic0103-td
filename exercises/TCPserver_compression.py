import socket

def compress(message):
  compression = []
  counter = 1
  old_char = '\0'
  
  for i, char in enumerate(message):
    if char != old_char:
      compression.append((old_char, counter))
      counter = 1
      old_char = char
    else:
      counter += 1

  compression.append((old_char, counter))

  compression = compression[1:]
  compressed = ''
  for c in compression:
    compressed += c[0] + str(c[1])
  return compressed

def TCPserver(host, port):
  tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  tcp_server.bind((host, port))
  tcp_server.listen()
  conn, addr = tcp_server.accept()

  while True:
    data = conn.recv(1024)
    message = data.decode('utf8')

    if not data:
      break

    compressed = compress(message)
    conn.sendall(compressed.encode('utf8'))

  conn.close()
  return


def main():
  # print(compress('AAAAAAAAAAAABBCCCCCC'))
  assert compress('AAAAAAAAAAAABBCCCCCC') == 'A12B2C6'

  # print(compress('AAABBBBBBFFFFFFFF'))
  assert compress('AAABBBBBBFFFFFFFF') == 'A3B6F8'

  # print(compress('AAAAAAAAAAAAAAAABBBB'))
  assert compress('AAAAAAAAAAAAAAAABBBB') == 'A16B4'

  # print(compress('GGGGGHH'))
  assert compress('GGGGGHH') == 'G5H2'

  return


main()    
