import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# http:///
host="www.gazetadesaojoaodelrei.com.br"
path='/site'
path=path+'/'
host, path = host.encode(), path.encode()
# print(path)
# input()
s.connect((host, 80))
s.sendall(b'GET %b HTTP/1.1\r\nHOST: %b\r\n\r\n' % (path,host))

reply = b''

while select.select([s], [], [], 3)[0]:
    data = s.recv(65536)
    if not data: break
    reply += data

headers =  reply.split(b'\r\n\r\n')[0]
image = reply[len(headers)+4:]
dados=str(image, ' utf-8 ' )
print(dados)
# print(image)
print('\n')
# print('\n apos o texto')



# path=path.decode()
# extensoes = ['.txt', '.mp3', '.pdf', '.html', '.jpg', '.png']
# if len(path)!=0 :
#     path=path.split('/')
#     print("ok")
#     for arquivo in path:
#         if arquivo[-4:] in extensoes:
#              'Downloads/'
#     return "Downloads/arquivo_generico"
    





# save image
f = open('image7.html', 'wb')
f.write(image)
f.close()