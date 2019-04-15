#coding: utf-8
import requisicao as ende
import re
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
    
    # dois=':'
    if ":" in url:
      a1=url.index(':')
      if url[a1+1]!='/':
        print('Tem : pontos')
        a=url.index(':',5)
        a=a+1
        porta=url[a:len(url)]
      # elif:
      else:
        print(url)
        porta='80'
      
    else:
        porta='80'
    descarta,host=url.split('//')
  
    auxiliarcolculo=url.split('/')

    if len(auxiliarcolculo)>3:
      resultado=host.index('/')
      caminhoincompleto=host[resultado:len(host)]
      
    else:
     
      caminhoincompleto=''
    enderco=host.split('/')
    
    host=enderco[0]
  
    path=''.join(caminhoincompleto)
    
  
    if(host[0]!='1'):
      pattern="www."
      if pattern not in host:
        host='www.'+host
        
    else:
      
      ende.servidorconect(host,path,porta)
      
    ende.requisicaohost(host,path,porta)
if __name__ == "__main__":
  main()
