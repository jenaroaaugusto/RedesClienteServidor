import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# http:///
host="www.opopularjm.com.br"
path='wp-content/uploads/2019/03/54730591_2023596907688141_5192235201639481344_n.jpg'
host, path = host.encode(), path.encode()
s.connect((host, 80))
s.sendall(b'GET /%b HTTP/1.1\r\nHOST: %b\r\n\r\n' % (path,host))

reply = b''

while select.select([s], [], [], 3)[0]:
    data = s.recv(2048)
    if not data: break
    reply += data

headers =  reply.split(b'\r\n\r\n')[0]
image = reply[len(headers)+4:]
print(headers)
input()
path=path.decode()
extensoes = ['.txt', '.mp3', '.pdf', '.html', '.jpg', '.png']
if len(path)!=0 :
    path=path.split('/')
    print("ok")
    for arquivo in path:
        if arquivo[-4:] in extensoes:
            A='Downloads/'
    B="Downloads/arquivo_generico"
    



input()

# save image
f = open('image6.jpg', 'wb')
f.write(image)
f.close()