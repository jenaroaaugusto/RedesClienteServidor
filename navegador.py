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

if __name__ == "__main__":
  while(1):
    main()
