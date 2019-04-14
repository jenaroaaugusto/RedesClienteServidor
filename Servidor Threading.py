import socket
import sys
import threading

def atividadeconecao(cliente,con):
    print(cliente)
    # input()
    while True:
        msg = con.recv(1024)
        print(msg)
        msg=msg.decode()
        print("Apos decode\n")
        print("Valor", msg)
    
        if "Hello" in msg:
            print("Aqui")
            arq = open("index.html",'r')
            informacao= arq.read()
            # print(informacao)
            home=''.join(informacao)
            # print(home)
            envio="Servidor NINA |"+home
            print("Tamanho envio",len(envio))
            
            envio=envio.encode()
            print(len (envio))
            con.sendall(envio)
            msg=''
        else:
            print("ok")
            
        if msg =="exit":
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
