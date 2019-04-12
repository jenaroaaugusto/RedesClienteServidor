import socket
import thread
# import threaded
# http://127.0.0.1:5000
HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

def conectado(con, cliente):

    print "Conectado por",cliente 

    while True:
        msg = con.recv(1024)
        print "Valor", msg
        if "Hello" in msg:
            print "Aqui"
            con.sendall("Servidor NINA ")
            msg=''
        # if not msg:break
        # con.settimeout()
        if "exit" in msg:
            break
        print cliente, msg

        if

    print 'Finalizando conexao do cliente', cliente 
    con.close()
    thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(5)

while True:
    con, cliente = tcp.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))

tcp.close()