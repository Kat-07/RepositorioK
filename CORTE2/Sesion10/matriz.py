from random import randint as r

def main(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(r(1,10))
    
        print(matriz[i])
    #print(matriz)
    return matriz

def escalar(matriz):
    esc=int(input('ingrese el escalar: '))
    for i in matriz:        #for i in range(len(matriz)):
        for j in range(len(i)):
            i[j]*=esc
        print(i)

if __name__=="__main__":
    filas = int(input('Ingrese el numero de filas: '))
    columnas= int(input('Ingrese el numero de columnas: '))
    print('------ORIGINAL--------')
    matriz=main(filas, columnas)
    print('-------ESCALADA-------')
    escalar(matriz)