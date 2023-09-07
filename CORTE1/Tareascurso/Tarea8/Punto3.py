#Realice un programa que almacene diferentes numeros escritos por el usuario dentro de una lista 
#hasta que se incluya un numero negativo, muestre la lista resultante y despues elimine los numeros duplicados

import random as r

def Lista():
        lista=[]
        opc='y'
        while opc=='y':
            for i in range(1):
                n=int(input('por favor ingrese un numero'))
                if n>0:
                    lista.append(n)
                    continue
                
                elif n<0:
                    print(lista)
                    print(set(lista)) #Elimina los valores duplicados de una lista
                    break

if __name__=="__main__":
    Lista()