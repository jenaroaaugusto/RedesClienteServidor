#coding: utf-8
import requisicao as ende
import re
def main():
    url=input("URL do Website:")
    if re.search(r'[http:]+[\\]+[\\]', url, re.IGNORECASE):
      busca(url)
    else: 
      print("Endereço Invalido")
      main()
    
    

def busca(url):
    print("Aqui estou")
    print(url,"\n")
    tipo=url.split('\\')
    print(tipo,"\n")
    print(len(tipo))
    print(tipo[2])
    
    if len(tipo)>3 :
      for i in range(3,len(tipo)):
        palavra .format(tipo[i])
      print(palavra)
    input()
    ende.requisicaohost(url)
    # erequisicao(url)
    
if __name__ == "__main__":
  main()





# busca(url)