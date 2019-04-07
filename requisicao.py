#encoding: utf-8

import socket
import re 
import ssl

def requisicaohost(host,path,porta):
    arq=[]
    arq2=[]

    # print("Na requisição",host)
    # print('Host',type(host),'path',type(path))

    # rex busca apos o google.com\...[\\]+\w+\n
    # req = b"GET / HTTP/1.1\nHost: stackoverflow.com\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(("stackoverflow.com", 80))
    # www.opopularjm.com.br
    # http://www.gazetadesaojoaodelrei.com.br/site/categoria/cidade/   
    s.connect((host,int(porta)))
    # User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
    host, path = host.encode(), path.encode()
    s.sendall(b'GET /%b HTTP/1.1\r\nHost:%b\r\n\r\n'%(path,host))
    
    # 65536 francoerangelimoveis
    resposta=s.recv(65536)
    # print(resposta,'\n')
   
    # s.send(b"GET www.opopularjm.com.br/wp-content/uploads/2019/03/54730591_2023596907688141_5192235201639481344_n.jpg HTTP/1.1\r\nHost:www.opopularjm.com.br\r\n\r\n")
    # resposta2=s.recv(65536)
    # print(resposta2)
    # # resposta.decode('cp1252')
    # .encode('utf-8')
    s.close()
    input()

    dados=str(resposta,'utf-8')
    # dados=dados.encode('utf-8')
    # dados=dados.decode('cp1252').encode('utf-8') 
    # dados=dados.encode('utf-8')
    print(dados,'\n')
  
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

    f = open("index.html", 'w')
    # f.write(str(corpo,'latin1'))
    # f.write(str(corpo))
    f.write(str(corpo))
    f.close()
    
# requisicao()   