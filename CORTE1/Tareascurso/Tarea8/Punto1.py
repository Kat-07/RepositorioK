import random as r

def Lista():
    lista=[]
    for i in range(15):
        lista.append(r.randint(1,100))
    print(lista)
    ordenados=sorted(lista)
    print(ordenados)

if __name__=="__main__":
    Lista()