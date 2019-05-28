import socket
import sys
import threading
import copy
import os 
def tipo(requerido):
    if requerido.endswith(".jpg"):
        mimetype = 'image/jpg'
    elif requerido.endswith(".png"):
        mimetype = 'image/png'
    elif requerido.endswith(".txt"):
        mimetype = 'text/txt'
    elif requerido.endswith(".mp3"):
        mimetype = 'music/mp3'
    elif requerido.endswith(".pdf"):
        mimetype = 'text/pdf'
    elif requerido.endswith(".css"):
        mimetype = 'text/css'
    elif requerido.endswith(".gif"):
        mimetype= 'image/webp,image/apng,image/*,*/*'
    else:
        mimetype = 'text/html'
    return mimetype
def atividadeconecao(cliente,con):
    print("Cliente conectado: IP ",cliente)
    
    # print(diretorio)
    # exit()
    href=[]
    
    while True:
        diretorio=os.listdir("servidor")
        msg = con.recv(1024)
        estadonatural=copy.copy(msg)
        msg=msg.decode()
        print("No mensagem",msg)
        if msg =="":
            break
        print("i",msg.index("T"),'x',msg.index("HTTP"))
        print("Estado natural", estadonatural)
        auxmsg=msg.split()
        
        busca=copy.deepcopy(auxmsg[1])
        if busca == '/' or busca=='/index':
            print("Aqui")
            # arq = open("estouaqui.html",'r')
            # print(diretorio)
            # print(type(diretorio))
        
            # exit()
            # for j in range(len(diretorio)):
            for i in diretorio:
                print(i)
                ok="<li><a href=/"+i+">"+i+"/</a></li>"
                href.append(ok)
            lista=' '.join(href)
            lista="<ul>"+lista+"</ul>"
                 
            info="<html <head> <title>Index of /dist</title></head><body><h1>NINA Directory</h1><h2>Arquivos</h2><dl><dt>Trabalho Pratico para Disciplina de Redes de Computadores 2019/1 UFSJ</dt><dt>Para rodar o Servidor e o Cliente respectivamente:</dt><dd>python Threading Servidor.py</dd><dd>python navegador.py</dd></dl><pre><hr><p>"+lista+"</p></pre><hr><p> Redes Cliente Servidor Python</p></body></html>"
            
            cabeca="HTTP/1.1/ 200 OK\r\nHost:127.0.0.1:5000\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41\r\nAccept: text/html\r\nAccept-Encoding: deflate\r\nAccept-Language: en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7\r\n\r\n"
            cabeca=cabeca.encode('utf-8')
            
            info=info.encode('utf-8')
             
            cabeca=cabeca+info
            # cabeca=cabeca+informacao
            print("E a cabeça",cabeca)
            con.send(cabeca)
            
            break
        # print("Copia",busca)
        # # exit()
        elif msg!="":
            print("No mensagem")
            print("i",msg.index("T"),'x',msg.index("HTTP"))
            i=msg.index("/") 
            x=msg.index("HTTP")
            requerido=msg[i:x]
            print(requerido)
            try:
                arq = open("servidor"+requerido,'rb')
            
            except Exception as e:
                cabeca="HTTP/1.1/ 404 Not Found\r\nHost:127.0.0.1:5000\r\nUser-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41\r\nAccept:text/html\r\nAccept-Encoding: deflate\r\nAccept-Language: en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7\r\n\r\n"
                cabeca=cabeca.encode('utf-8')
                quatrocentos= open("servidor/morte.jpg",'rb')
                informacao=quatrocentos.read()
                cabeca=cabeca+informacao
                con.send(cabeca)
                break
            if arq is None:
                
                print("Erro")
            else:
                informacao=arq.read()

                mimetype=tipo(requerido)
                cabeca=''
                cabeca="HTTP/1.1/ 200 OK\r\nHost:127.0.0.1:5000\r\nUser-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41\r\nAccept:"+str(mimetype)+"\r\nAccept-Encoding: deflate\r\nAccept-Language: en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7\r\n\r\n"
                cabeca=cabeca.encode('utf-8')
                
                cabeca=cabeca+informacao
                con.send(cabeca)

                print("OK")
        
        print ("Sou eu",cliente, msg)
        break
    print ('Finalizando conexao do cliente', cliente )
    exit()
    con.close()
    # threading.exit()

def conectado(porta,caminho):
    print(caminho)
    PORT=porta

    serv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    orig = (HOST, PORT)

    serv.bind(orig)
    serv.listen(3)
    while True:
        con,cliente=serv.accept()
        conecoes=threading.Thread(
            target=atividadeconecao,
            args=(cliente,con)
        )
        conecoes.start()
        # exit()

if __name__ == "__main__":
    HOST='127.0.0.1'
    
    porta= 5000
    conectado(porta,HOST)
