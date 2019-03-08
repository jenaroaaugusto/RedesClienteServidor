#coding: utf-8

def main():
    url=input("URL do Website:")
    busca(url)

def busca(url):
    print("Aqui estou")
    print(url,"\n")
    tipo=url.split('\\')
    print(tipo,"\n")
    print(len(tipo))
    
if __name__ == "__main__":
  main()





# busca(url)