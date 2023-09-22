def main_read():
    f=open('matrizAsignacion.txt','rt')
    documento=f.read()
    f.close()
    print(documento)

def main_read2():
    f=open('matrizAsignacion.txt','rt')
    documento=f.readline().rstrip('\n').split(',')
    while documento != [""]:
        print(documento)
        #input('presione enter')
        documento=f.readline().rstrip('\n').split(',')
    f.close()

def suma(lista):
    salida=""
    for dato in lista:
        resulta=int(dato[0])+int(dato[1])+int(dato[3])
        salida+=str(resulta)+('\n')
    return salida

def main_read3():
    f=open('matrizAsignacion.txt','rt')
    documento=f.readlines()
    f.close()
    lista=[]
    for dato in documento:
        lista.append(dato.rstrip('\n').split(','))
    print(lista)
    a=suma(lista)
    print(a)


if __name__=="__main__":
    #main_read()
    #main_read2()
    main_read3()