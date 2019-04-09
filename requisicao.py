#encoding: utf-8

import socket
import re 
import select
def tratamento(dados):
    informacao=str(dados,'utf-8')
    if (informacao.find("!DOCTYPE")!=-1):
        separador=informacao.index("!DOCTYPE")
    elif(informacao.find("!doctype")!=-1):
        separador=informacao.index("!doctype")
    print(separador,'\n')
    cabecalho=informacao[0:separador]
    fim=informacao.index("</html>")
    corpo=informacao[separador:fim]
    
    corpo=re.sub(r'[\\]+[n]'," ",corpo)
    corpo=re.sub(r'[\\]+[t]'," ",corpo)
    corpo=re.sub(r"[\\]+[']"," ",corpo)
    corpo=re.sub(r'[\\]+[r]'," ",corpo)
    return corpo

def caminho_comDados(path,headers):
    path=path.decode()
    auxipath=path
    extensoes = ['.txt', '.mp3', '.pdf', '.html', '.jpg', '.png']
    path=path.split('/')
    # print(path)
    # print("ok")
    # nome=host[posi:len(host)] 
    for arquivo in path:
        if arquivo[-4:] in extensoes:
            # print(arquivo[-4:])
            
            return '-'.join(path[0:len(auxipath)-5])+arquivo[-4:]
    posi=len(auxipath)
    print(posi)
    print(path)
    input()
    # posi=auxipath.index("/")
    # nome=auxipath[posi:len(auxipath)]
    return "-".join(path)+".html"
def CaminhosSemArquivo(mensagem,host):    
    print('Host',host)
    host=host.decode()
    posi=host.index("www")
    
    nome=host[posi:len(host)] 
    

    return "Downloads-"+nome+".html"
def requisicaohost(host,path,porta):
    arq=[]
    arq2=[]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    s.connect((host,int(porta)))
    auxipath=path
    path=path+'/'
    host, path = host.encode(), path.encode()
 
    s.sendall(b'GET %b HTTP/1.1\r\nHost:%b\r\n\r\n'%(path,host))
    if auxipath ==0 :
        resposta=s.recv(512000)
        corpo=tratamento(resposta)
    
    reply = b''

    while select.select([s], [], [], 3)[0]:
        data = s.recv(512000)
        if not data: break
        reply += data

    headers =  reply.split(b'\r\n\r\n')[0]
    corpoitens = reply[len(headers)+4:]
    print(corpoitens)
    input()

    s.close()
   

    if len(auxipath)!=0:
        arqnome = caminho_comDados(path,headers)
        saida = open(arqnome,'wb')
        saida.write(corpoitens)
        saida.close()
    else:
        arqnome= CaminhosSemArquivo(corpo,host)
        saida = open(arqnome,'w')
        print('ok') 
        # informacao=str(corpo, ' utf-8 ' ) 
        saida.write(str(corpo))
        saida.close()



#     dados = str (resposta, ' utf-8 ' )

#     print(dados,'\n')
#     # dados
  
#     # Verifica o codigodo de resposta
#     arq=''+chr(resposta[9])+chr(resposta[10])+chr(resposta[11])
#     if  arq == '301':
#         print('ERRO 301')    
#     elif arq != '200' :
#         print("erro")
#         exit()
#     print(arq,"\n")
#     input()

#     separador=0
#     for x in range(0,len(dados)):
#         if dados[x]=='<' and dados[x+1]=='!' and (dados[x+2]=='d' or dados[x+2]=='D') :  
#             print('ok')
#             separador=x

#             print(x)
#     print(separador,'\n')
#     cabecalho=dados[0:separador]
#     corpo=dados[separador:len(dados)]
    
#     corpo=re.sub(r'[\\]+[n]'," ",corpo)
#     corpo=re.sub(r'[\\]+[t]'," ",corpo)
#     corpo=re.sub(r"[\\]+[']"," ",corpo)
#     corpo=re.sub(r'[\\]+[r]'," ",corpo)
    

#     print(corpo)

#     f = open("index2.html", 'w')
#     # f.write(str(corpo,'latin1'))
#     # f.write(str(corpo))
#     f.write(str(corpo))
#     f.close()
    
# # requisicao()   