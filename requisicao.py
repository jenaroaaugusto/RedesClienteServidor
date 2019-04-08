#encoding: utf-8

import socket
import re 
import ssl

def requisicaohost(host,path,porta):
    arq=[]
    arq2=[]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    s.connect((host,int(porta)))
    
    path=path+'/'
    host, path = host.encode(), path.encode()
 
    s.sendall(b'GET %b HTTP/1.1\r\nHost:%b\r\n\r\n'%(path,host))
    resposta=s.recv(65536)
    s.close()

    dados=str(resposta,'utf-8')
    
    print(dados,'\n')
    # dados
  
    # Verifica o codigodo de resposta
    arq=''+chr(resposta[9])+chr(resposta[10])+chr(resposta[11])
    if  arq == '301':
        print('ERRO 301')    
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

    f = open("index2.html", 'w')
    # f.write(str(corpo,'latin1'))
    # f.write(str(corpo))
    f.write(str(corpo))
    f.close()
    
# requisicao()   