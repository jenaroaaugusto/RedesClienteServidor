#encoding: utf-8

import socket
import re 
import ssl

def requisicao():
    arq=[]
    arq2=[]
    # req = b"GET / HTTP/1.1\nHost: stackoverflow.com\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(("stackoverflow.com", 80))   
    s.connect(("www.youtube.com", 80))
    # User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
    s.sendall(b"GET / HTTP/1.1\r\nHost:www.youtube.com\r\n\r\n")
    # 65536 francoerangelimoveis
    resposta=s.recv(65536)
    # resposta.decode('cp1252')
    # .encode('utf-8')
    s.close()

    dados=str(resposta,'utf-8')
    # dados=dados.encode('utf-8')
    # dados=dados.decode('cp1252').encode('utf-8') 
    # dados=dados.encode('utf-8')
    print(dados,'\n')
  
    # Verifica o codigodo de resposta
    arq=''+chr(resposta[9])+chr(resposta[10])+chr(resposta[11])
    if  arq == '301':
        print('ok')
        # for i in range(0, len(dados)):
        #     if dados[i]=='L' and dados[i+1]=='o' and dados[i+2] =='c' and dados[i+1] == 'a ' and dados[i+1]=='t'and dados[i+1] == 'i' and dados[i+1] == 'o' and dados[i+1] =='n'
        x=dados.index('https://')
        # print(dados)
        # print(x)
        # for i in range(x,len(dados)):
        #     if dados[i] =="\n":
        #         print(dados[i],"Valor I",i)
            
        #         print ('aqui')
        HOST = "www.youtube.com"
        PORT = 443

        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_sock = context.wrap_socket(s, server_hostname=HOST)
        s_sock.connect((HOST, 443))
        s_sock.send(" GET / HTTP/1.1\r\nHost: www.youtube.com\r\n\r\n ".encode())

        while True:
            data = s_sock.recv(2048)
            if ( len(data) < 1 ) :
                break
            print(data)

        s_sock.close()    
        
    elif arq != '200' :
        print("erro")
        exit()
    print(arq,"\n")
    input()
    




    separador=0
    # z= len(dados)
    for x in range(0,len(dados)):
        if dados[x]=='<' and dados[x+1]=='!' and (dados[x+2]=='d' or dados[x+2]=='D') :  
            print('ok')
            separador=x

            print(x)
    print(separador,'\n')
    cabecalho=dados[0:separador]
    corpo=dados[separador:len(dados)]
    # print(cabecalho,"\n")    
    
    # print(corpo,"\n")
    # input() 
    # dados.replace("\n"," ")
    corpo=re.sub(r'[\\]+[n]'," ",corpo)
    corpo=re.sub(r'[\\]+[t]'," ",corpo)
    corpo=re.sub(r"[\\]+[']"," ",corpo)
    corpo=re.sub(r'[\\]+[r]'," ",corpo)
    # corpo=corpo.decode('utf-8')

    print(corpo)

    f = open("index.html", 'w')
    # f.write(str(corpo,'latin1'))
    # f.write(str(corpo))
    f.write(str(corpo))
    f.close()
    
requisicao()   