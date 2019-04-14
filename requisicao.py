#encoding: utf-8

import socket
import re 
import select
# http://127.0.0.1:5000
def status_code(headers):
    print("aqui1")
    situacao = {"302": "302 Found",
             "404": "404 Not Found",
             "301": "301 Moved Permanently",
             "401": "401 Unauthorized",
             "400": "400 Bad Request",
             "403": "403 Forbidden",
             "500": "500 Internal Server Error",
             "504": "504 Gateway Timeout",
             "501": "501 Not Implemented",
             "502": "502 Bad Gateway",
             "503": "503 Service Unavailable"}
    status=headers.split()
    if status[1] in situacao.keys():
        print(situacao[status[1]])
        exit()
def servidorconect(host,path,porta):
    print("Host",host,"Caminho",path,"Porta",porta)
    auxurl,auxport=path.split(":")
    print(auxurl,"e",auxport)
    porta=auxport
    path=auxurl
    print("Host",host,"Caminho",path,"Porta",porta)
    print("Aqui")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,int(porta)))
    if len(path)==0:
        auxipath="Hello"
    else:
        auxipath=path

    host, auxipath = host.encode(), auxipath.encode()
    s.send(b'GET %b HTTP/1.1\r\nHost:%b\r\n\r\n'%(auxipath,host))
    print("Passou ")

    reply = b''

    while select.select([s], [], [], 3)[0]:
        data = s.recv(512000)
        if not data: break
        reply += data
    headers =  reply.split(b'|')[0]
    corpoitens = reply[len(headers)+1:]

    print("aqui",len(reply))
    if len(reply)==0:
        print("ERRO 404")
        exit()
    corpoitens= corpoitens.decode()
    headers=headers.decode()
    print(headers)
    input()
    print(corpoitens)
    exit()

def tratamento(dados):
    informacao=str(dados,'utf-8')
    if (informacao.find("!DOCTYPE")!=-1):
        separador=informacao.index("!DOCTYPE")
    elif(informacao.find("!doctype")!=-1):
        separador=informacao.index("!doctype")
    # print(separador,'\n')
    cabecalho=informacao[0:separador]
    fim=informacao.index("</html>")
    corpo=informacao[separador:fim]
    
    corpo=re.sub(r'[\\]+[n]'," ",corpo)
    corpo=re.sub(r'[\\]+[t]'," ",corpo)
    corpo=re.sub(r"[\\]+[']"," ",corpo)
    corpo=re.sub(r'[\\]+[r]'," ",corpo)
    return corpo
def caminho_comDados(path,headers):
    path=path.decode()
    auxipath=path
    extensoes = ['.txt', '.mp3', '.pdf', '.html', '.jpg', '.png']
    path=path.split('/')
    # print(path)
    # print("ok")
    # nome=host[posi:len(host)] 
    for arquivo in path:
        if arquivo[-4:] in extensoes:
            
            return 'Sites/'+''.join(path[0:len(auxipath)-5])+arquivo[-4:]
    posi=len(auxipath)
   
    return 'Sites/'+''.join(path)+".html"
def CaminhosSemArquivo(mensagem,host):    
    
    host=host.decode()
    posi=host.index("www")
    
    nome=host[posi:len(host)] 
    
    return "Sites/"+nome+".html"
def requisicaohost(host,path,porta):
  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    s.connect((host,int(porta)))
    
    auxipath=path
    path=path+'/'
    host, path = host.encode(), path.encode()
    
    s.sendall(b'GET %b HTTP/1.1\r\nHost:%b\r\n\r\n'%(path,host))
  
    if len(auxipath) == 0 :
        resposta=s.recv(512000)
        corpo=tratamento(resposta)

    reply = b''

    while select.select([s], [], [], 3)[0]:
        data = s.recv(512000)
        if not data: break
        reply += data

    headers =  reply.split(b'\r\n\r\n')[0]
    corpoitens = reply[len(headers)+4:]
    a=headers.decode()
    status_code(a)
    s.close()
   

    if len(auxipath)!=0:
        arqnome = caminho_comDados(path,headers)
        saida = open(arqnome,'wb')
        saida.write(corpoitens)
        saida.close()
    else:
        arqnome=CaminhosSemArquivo(corpo,host)
        saida = open(arqnome,'w') 
        saida.write(str(corpo))
        saida.close()
