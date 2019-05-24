import socket
import sys
import threading
import copy
def atividadeconecao(cliente,con):
    print("Cliente conectado: IP ",cliente)
    while True:
        msg = con.recv(1024)
        estadonatural=copy.copy(msg)
        msg=msg.decode()
        print("No mensagem",msg)
        print("i",msg.index("T"),'x',msg.index("HTTP"))
        print("Estado natural", estadonatural)
        auxmsg=msg.split()
        
        busca=copy.deepcopy(auxmsg[1])
        if busca == '/' :
            arq = open("estouaqui.html",'r')
            
            informacao=arq.read()
            cabeca="HTTP/1.1/ 200 OK\r\nHost:127.0.0.1:5000\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41\r\nAccept: text/html\r\nAccept-Encoding: deflate\r\nAccept-Language: en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7\r\n\r\n"
            cabeca=cabeca.encode('utf-8')
            informacao=informacao.encode('utf-8')
            cabeca=cabeca+informacao
            con.send(cabeca)
            
            break
        # print("Copia",busca)
        # # exit()
        else:
            print("No mensagem")
            print("i",msg.index("T"),'x',msg.index("HTTP"))
            i=msg.index("/") 
            x=msg.index("HTTP")
            requerido=msg[i:x]
            print(requerido)
            cabeca=''
            cabeca="HTTP/1.1/ 200 OK\r\nHost:127.0.0.1:5000\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41\r\nAccept:  image/webp,image/apng,image/*,*/*\r\nAccept-Encoding: deflate\r\nAccept-Language: en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7\r\n\r\n"
            cabeca=cabeca.encode('utf-8')
            arq = open("servidor"+requerido,'rb')
            informacao=arq.read()
            cabeca=cabeca+informacao
            con.send(cabeca)

            print("OK")

            
        if "Hello" in msg:
            arq = open("servidor/index.html",'r')
            informacao= arq.read()
            home=''.join(informacao)
            envio="Servidor NINA: 200 OK|"+home    
            envio=envio.encode()
            print(len (envio))
            con.sendall(envio)
            
            arq.close()
            break
        elif "index" in msg:
            arq = open("servidor/index.html",'r')
            informacao= arq.read()
            home="Servidor NINA :200 OK |"+''.join(informacao) 
            home=home.encode() 
            con.sendall(home)
        
            arq.close()
            break
        arquivos=['/index.html','/logo.png','/casa.txt','/icons/blank.gif']
        
        if busca in arquivos:
            
            arq = open("servidor"+busca,'r')
            informacao= arq.read()
            home="Servidor NINA 200 OK|"+''.join(informacao) 
            home=home.encode() 
            con.sendall(home)
            arq.close()
            break

        if msg =="exit": 
            break 
            exit()
        
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

if __name__ == "__main__":
    HOST='127.0.0.1'
    
    porta= 5000
    conectado(porta,HOST)
