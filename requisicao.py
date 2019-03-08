import socket 

def requisicao():
    # req = b"GET / HTTP/1.1\nHost: stackoverflow.com\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(("stackoverflow.com", 80))   
    s.connect(("www.google.com.br", 80))
    s.sendall(b"GET / HTTP/1.1\r\nHost:www.google.com.br\r\n\r\n")
    resposta=s.recv(10000)
    print(type(resposta),"\n")
    print(chr(resposta[9]),"\n")
    print(resposta,"\n")
    

    s.close()
requisicao()   