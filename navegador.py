#coding: utf-8
import requisicao as ende
import re
def main():
    url=input("URL do Website:")
    if re.search(r'[http:]+[//]+[//]', url, re.IGNORECASE):
      busca(url)
    else: 
      print("Endereço Invalido")
      main()
      url=''

    
    

def busca(url):
    # print("Aqui estou")
    # print(url,"\n")
    
    descarta,host=url.split('//')
    
    # print(host,"\n")
    # print(len(host))
    auxiliarcolculo=url.split('//')
    if len(auxiliarcolculo)>3:
      resultado=host.index('/')
      # print(resultado)
      # input()
      caminhoincompleto=host[resultado:len(host)]
      # print(caminhoincompleto,"\n")
      # input()
    else:
      # print('Chaguei')
      caminhoincompleto=''
    enderco=host.split('/')
    
    host=enderco[0]

    # print("O Host",host)
    # print('O path',caminhoincompleto)
    path=''.join(caminhoincompleto)
    # print(path)
    host='www.'+host
    # print(host)
    # input()
    # if len(host)>3 :
    #   print("E maior ")

    # input()
    ende.requisicaohost(host,path)
    # erequisicao(url)
    
if __name__ == "__main__":
  main()





# busca(url)