import socket
import datetime
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    while True:
        msg= con.recv(1024)
        print msg
        # if not msg: break
        # resposta=input()
        if msg == 'd':
            # x= datetime.datetime.now()
            # print (x)
            # h=str(x)
            h="jenaro" 
            con.sendall(h)
        elif msg  =='a':
            print cliente, msg
    print 'Finalizando conexao do cliente', cliente
con.close()