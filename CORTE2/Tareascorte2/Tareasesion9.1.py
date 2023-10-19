#2. Escribir una funcion recursiva que encuentre el mayor elemento de una lista.
#3. Escribir una funcion recursiva que reciba como parámetros dos strings a y b,
#y devuelva una lista con las posiciones en donde se encuentra b dentro de a. Ejemplo:

import random as r

def lista(x):
    lista=[]
    for i in range(x):
        lista.append(r.randint(1,10))
    return lista
        
def recursiva(lista):
    if lista[0]>lista[1]:
        lista.pop(1)
        if len(lista)==1:
            mayor=lista[0]
            return mayor
        else:
            recursiva(lista)
    elif lista[0]<lista[1]:
        lista.pop(0)
        if len(lista)==1:
            mayor=lista[0]
            return mayor
        else:
            recursiva(lista)
    elif lista[0] == lista[1]:
        lista.pop(0)
        if len(lista)==1:
            mayor=lista[0]
            return mayor
        else:
            recursiva(lista)
    
  
def strings(a,b):
    posicion=[]
    for i in range(len(a)):
        if a[i]==b:
            posicion.append(i)
    return posicion

    
def main():
    print('-------------------------------menú----------------------------------')
    print('1. Encontrar el mayor elemento de una lista')
    print('2. Devolver las posiciones de dos strings a y b dentro de una lista')
    opc=int(input('Por favor seleccione un programa (1 o 2): '))
    print('---------------------------------------------------------------------')
    if opc==1:
        n = int(input("Ingrese la cantidad de elementos de la lista:  "))
        nlista = lista(n)
        print("Lista:", nlista)
        mayor = recursiva(nlista)
        nmayor=nlista
        print("El mayor elemento de la lista es:",nmayor )
    elif opc==2:
            a=str(input('Por favor ingrese una palabra: '))
            b=str(input('Por favor ingrese una letra de esa palabra: '))
            posicion=strings(a,b)
            if len(posicion)>=1:
                print(f"Las posiciones de '{b}' dentro de '{a}' son: {posicion}")
            else:
                print(f"la letra '{b}' no se encuentra en la palabra '{a}'")
         
    else:
        print('opcion invalida')
    

if __name__=='__main__':
    main()