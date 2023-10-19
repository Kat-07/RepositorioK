def main_read():
    f=open('wcm.csv','r',encoding="utf8")
    documento=f.readlines()
    f.close()
    print(documento)

def lectura():
    f=open('wcm.csv','r',encoding="utf8")
    documento=f.readlines()
    f.close()
    copamundial=[]
    for i in documento:
        copamundial.append(i.rstrip('\n').split(','))
    return copamundial

def imprimir(x):
    for i in x:
        print(i)

def main():
    lecturadoc=lectura()
    imprimir(lecturadoc)

if __name__=="__main__":
    main()