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
    dois=':'
    if dois in url:
      a1=url.index(':')
      if url[a1+1]!='/':
        print('Tem : pontos')
        a=url.index(':',5)
        a=a+1
        porta=url[a:len(url)]
      else:
        porta='80'
    else:
        porta='80'
    descarta,host=url.split('//')
    
    # print(descarta,'e',host)
    # input()
    # print(host,"\n")
    # print(len(host))
    auxiliarcolculo=url.split('/')

    # print(auxiliarcolculo)
    # input()
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
    # print("Foi aqui",host)
    # input()
    # print("O Host",host)
    # print('O path',caminhoincompleto)
    path=''.join(caminhoincompleto)
    
    # print(path)
    pattern="www."
    if pattern not in host:
      host='www.'+host
      
    # print(host)
    # input()
    # if len(host)>3 :
    #   print("E maior ")

    # input()
    ende.requisicaohost(host,path,porta)
    # erequisicao(url)
    
if __name__ == "__main__":
  main()
