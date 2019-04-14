import socket
import sys
import threading
import copy
def atividadeconecao(cliente,con):
    print("Cliente conectado: IP ",cliente)
    while True:
        msg = con.recv(1024)
        msg=msg.decode()
        print("No mensagem",msg)
        auxmsg=msg.split()
        print("No aux2",auxmsg)
        # input()
        busca=copy.deepcopy(auxmsg[1])
        print("Copia",busca)
        # exit()
        if "Hello" in msg:
            arq = open("servidor/index.html",'r')
            informacao= arq.read()
            home=''.join(informacao)
            envio="Servidor NINA |"+home    
            envio=envio.encode()
            print(len (envio))
            con.sendall(envio)
            
            arq.close()
            # break
        elif "index" in msg:
            arq = open("servidor/index.html",'r')
            informacao= arq.read()
            home="Servidor NINA |"+''.join(informacao) 
            home=home.encode() 
            con.sendall(home)
            
            arq.close()
            # break
        arquivos=['/index.html','/logo.png','/casa.txt']
        if busca in arquivos:
            print("chegou aquiii....")
            arq = open("servidor"+busca,'r')
            informacao= arq.read()
            home="Servidor NINA |"+''.join(informacao) 
            home=home.encode() 
            con.sendall(home)
            
            arq.close()
            # break


        
        if msg =="exit":
            # break 
            exit()
        print (cliente, msg)
    print ('Finalizando conexao do cliente', cliente )
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
