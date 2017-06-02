
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'www.liaoxuefeng.com'
s.connect((host, 80))

s.send('GET / HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n' % host)

buffer = []

while True:
  d = s.recv(1024)
  if d:
    buffer.append(d)
  else:
    break

data = ''.join(buffer)

s.close()

header, html = data.split('\r\n\r\n', 1)

print header
# print html

