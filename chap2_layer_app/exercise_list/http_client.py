import http.client

def HTTPclient(host,port):
  conn = http.client.HTTPConnection(host, port)
  L = int(input())

  for _ in range(L):
    content = input()
    conn.request("GET", content)
    response = conn.getresponse()
    headers = dict(response.getheaders())
    content_type = response.headers['Content-Type']

    if content_type == 'audio/mpeg':
      print('Playing audio:', content)
    elif content_type == 'text/html':
      print('Browsing:', content)
    elif content_type == 'video/x-msvideo':
      print('Playing media:', content)
    elif content_type == 'application/json':
      print('Processing JSON:', content)
    elif response.status == 404:
      print('Content not found')
    else:
      print('Unknown file/media:', '{}-{}'.format(content_type, content) )

  conn.close()
