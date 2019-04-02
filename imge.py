import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# http:///
s.connect(('www.opopularjm.com.br', 80))
s.sendall(b'GET /wp-content/uploads/2019/03/54730591_2023596907688141_5192235201639481344_n.jpg HTTP/1.1\r\nHOST: www.opopularjm.com.br\r\n\r\n')

reply = b''

while select.select([s], [], [], 3)[0]:
    data = s.recv(2048)
    if not data: break
    reply += data

headers =  reply.split(b'\r\n\r\n')[0]
image = reply[len(headers)+4:]

# save image
f = open('image5.jpg', 'wb')
f.write(image)
f.close()