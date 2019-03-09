#coding: utf-8

import socket
import re 

def requisicao():
    arq=[]
    arq2=[]
    # req = b"GET / HTTP/1.1\nHost: stackoverflow.com\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(("stackoverflow.com", 80))   
    s.connect(("example.com", 80))
    # User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
    s.sendall(bytes("GET / HTTP/1.1\r\nHost:example.com\r\n\r\n",'utf8'))
        # ,'utf8'
    # print("passou\n",s.proto)
    # input()
    # 65536
    resposta=s.recv(65536)
    # while True:
    # 'utf-8'
    #     if resposta:
    s.close()
    dados=str(resposta)
   
    
    print(dados,'\n')

    
    # .decode('utf8')
    # arq2.append(dados)
    # #     # else:
    # #     #     break 
    # print(arq2,"\n")
    # input()
    # print(type(resposta),"\n")
     
    # Verifica o codigodo de resposta
    arq=''+chr(resposta[9])+chr(resposta[10])+chr(resposta[11])
    if  arq == '301':
        print("Aqui")
        input()
    elif arq != '200' :
        print("erro")
        exit()
    print(arq,"\n")
    
    separador=0
    # z= len(dados)
    for x in range(0,len(dados)):
        if dados[x]=='<' and dados[x+1]=='!':  
            print('ok')
            separador=x

            print(x)
    print(separador,'\n')
    # input() 
    # dados.replace("\n"," ")
    dadosf=re.sub(r'[\\]+[n]'," ",dados)
    print(dadosf)
    input()

    # j = ''
    # k = ''
    # for i in dados:
    #     if '<!DOCTYPE' in i:
    #         print("aqui\n")
    #         input()
    #         aux = i.split('\n')
            
    #         for t in aux:
    #             k += t
    #         j += k
    #         continue
    #     j += i

    # f = open("index.html", 'w')
    # # j.replace("\n"," ")
    # f.write(str(j.replace('\n',' ')))
    
    
requisicao()   