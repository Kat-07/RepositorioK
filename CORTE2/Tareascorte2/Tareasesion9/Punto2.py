#Realice un programa donde permita crear una lista de 10 numeros aleatorios entre 1 y 50(enteros)
#Despues cree tres funciones donde se reciba la lista como parametro para:
#mayor()- funcion que imprima el numero mayor de la lista(no usar max)
#minimo() - funcion que imprima el numero menor de la lista (no usar min)
#primos() - funcion que imprima los numeros de la lista que son primos

import random as r

def lista():
    print('Bienvenido','\n'
          'Lista de tamaño 1*10')
    Lista=[]
    for i in range(10):
        Lista.append(r.randint(1,50))
    #print(Lista)
    return Lista

def primos(lista):
    primos=[]
    for i in lista:
        if i==1:
            primos.append(i)
        primo=i%2
        if primo==0:
            continue
        elif primo!=0:
            j=3
            while primo!=0:
                primo=i%j
                if primo!=0:
                    j=j+1
                elif primo==0 and i==j:
                    primos.append(i)
                elif primo==0:
                    break
    Primos=[]
    n=len(primos)
    if n==0:
        Primos.append('No hay numeros primos en la lista')
    elif n>=1:
        for i in primos:
            con=primos.count(i)
            if con==1:
               Primos.append(i)
            elif con==2:
                Primos.append(i)
                primos.remove(i)
                primos.remove(i)
            elif con==3:
                Primos.append(i)
                primos.remove(i)
                primos.remove(i)
                primos.remove(i)
            else:
               continue
    return Primos

def mayor(x):
    x.sort(reverse=False)
    numero_mayor=x.pop(9)
    return numero_mayor

def menor(x):
    x.sort(reverse=False)
    numero_menor=x.pop(0)
    return numero_menor

def imprimir(nota):
    print(nota)

def main():
    listado=lista()
    imprimir(listado)
    nprimos=primos(listado)
    nmayor=mayor(listado)
    imprimir(f'El numero mayor es: {nmayor}')
    nmenor=menor(listado)
    imprimir(f'El numero menor es: {nmenor}')
    imprimir(f'Numeros primos: \n {nprimos}')

if __name__=="__main__":
    main()