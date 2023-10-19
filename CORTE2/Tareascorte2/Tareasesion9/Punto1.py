#1. Realice un programa donde se cree una matriz de 5x10, después se imprima en pantalla la matriz creada,
#indicando cuál es el número más alto y más bajo dentro de la lista, incluyendo su respectiva posición. 
#Finalmente se organice la matriz del número mayor al menor, empezando desde la posición [0,0].

import random as r

def Matriz():
    matriz=[]
    print('Bienvenido:''\n'
           'Matriz 5*10, que muetra el número mayor y menor con su respectiva posición')
    for i in range(5):
        matriz.append([])
        for j in range(10):            
            matriz[i].append(r.randint(1,10))
        n1=(max(matriz[i]))
        n2=(min(matriz[i]))
        p1=matriz[i].index(n1)
        p2=matriz[i].index(n2)
        print(matriz[i], 'Numero mayor:',n1,', posicion:',p1, 'y numero menor:',n2,', posicion:',p2 )
        
        matriz[i].sort(reverse=True)
    print('Matriz ordenada:','\n',matriz)       
        

if __name__=="__main__":
    Matriz()