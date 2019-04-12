#encoding: utf-8

import socket
import re 
import select
# http://127.0.0.1:5000
def servidorconect(host,path,porta):
    host,porta=host.split(':')
    print("Aqui")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,int(porta)))
    auxipath="Hello"
    host, auxipath = host.encode(), auxipath.encode()
    s.send(b'GET /%b HTTP/1.1\r\nHost:%b\r\n\r\n'%(auxipath,host))
    print("Passou ")
    estado=s.recv(1024)
    estado=estado.decode()
    print("Passou 2 ")
    print("Conexão",estado,"\nDigite a solicitação:")
    requisitado=input("Exemplo: index.html\n")
    requisitado=requisitado.encode()
    path=requisitado
    s.send(b'GET /%b HTTP/1.1\r\nHost:%b\r\n\r\n'%(path,host))
    resposta=s.recv(2048)
    print(resposta)

    s.send(b'GET /%b HTTP/1.1\r\nHost:%b\r\n\r\n'%(auxipath,host))
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
            # print(arquivo[-4:])
            
            return '-'.join(path[0:len(auxipath)-5])+arquivo[-4:]
    posi=len(auxipath)
    # print(posi)
    # print(path)
    # input()
    # posi=auxipath.index("/")
    # nome=auxipath[posi:len(auxipath)]
    return "-".join(path)+".html"
def CaminhosSemArquivo(mensagem,host):    
    
    host=host.decode()
    posi=host.index("www")
    
    nome=host[posi:len(host)] 
    

    return "Downloads-"+nome+".html"
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
