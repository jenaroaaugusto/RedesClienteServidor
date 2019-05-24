#coding: utf-8
import requisicao as ende
import re
import copy
# http://127.0.0.1:5000
def main():
    url=input("URL do Website:")
    if re.search(r'[http:]+[//]+[//]', url, re.IGNORECASE):
      busca(url)
    else: 
      print("Endereço Invalido")
      main()
      url=''
def busca(url):
    padrao,link=url.split("//")
    print(padrao,"E",link)
    
    if ":"in link:
      linkcompleto,porta=link.split(":")
      print("Aqui",linkcompleto,"e",porta)
    else:
      linkcompleto=copy.copy(link)
      porta='80' 

    # validacao=linkcompleto[0:4] 
    # print(linkcompleto[0:4])  
    if "127."in linkcompleto[0:4]:
      print(linkcompleto)
      if '/' in linkcompleto:
        local=linkcompleto.index('/')
        host=copy.copy(linkcompleto[0:local])
        path=copy.copy(linkcompleto[local:len(linkcompleto)])
      else:
        host=copy.copy(linkcompleto)
        path=''
      
      print("Funciona",host,"e",path)
      ende.servidorconect(host,path,porta)

    elif "/" in linkcompleto:
      local=linkcompleto.index('/')
      host=copy.copy(linkcompleto[0:local])
      if "www."not in host: host="www."+host
      path=copy.copy(linkcompleto[local:len(linkcompleto)])
      ende.requisicaohost(host,path,porta)
      # print(host ,"e",path)
    elif "/" not in linkcompleto:
      path=""
      host=copy.copy(linkcompleto)
      if "www."not in host: host="www."+host
      ende.requisicaohost(host,path,porta)


    # exit()
    # if ":" in url:
    #   a1=url.index(':')
    #   if url[a1+1]!='/':
    #     print('Tem : pontos')
    #     a=url.index(':',5)
    #     a=a+1
    #     porta=url[a:len(url)]
    #   # elif:
    #   else:
    #     print(url)
    #     porta='80'
      
    # else:
    #     porta='80'
    # descarta,host=url.split('//')
    # auxiliarcolculo=url.split('/')

    # if len(auxiliarcolculo)>3:
    #   resultado=host.index('/')
    #   caminhoincompleto=host[resultado:len(host)]
      
    # else:
     
    #   caminhoincompleto=''
    # enderco=host.split('/')
    
    # host=enderco[0]
  
    # path=''.join(caminhoincompleto)
    
  
    # if(host[0]!='1'):
    #   pattern="www."
    #   if pattern not in host:
    #     host='www.'+host
        
    # else:
    #   print("Antes de", path)
    #   exit()
    #   ende.servidorconect(host,path,porta)
      
    # ende.requisicaohost(host,path,porta)
if __name__ == "__main__":
  while(1):
    main()
