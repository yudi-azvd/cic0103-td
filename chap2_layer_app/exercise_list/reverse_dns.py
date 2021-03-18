from socket import *

L = int(input())

for _ in range(L):
  ip = input()
  host = gethostbyaddr(ip)[0]
  print(host)
