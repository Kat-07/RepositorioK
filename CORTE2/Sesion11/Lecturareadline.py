
def main():
    f=open('matrizAsignacion.txt','rt')
    documento=f.read()
    f.close()
    print(documento)

def main_read2():
    f=open('matrizAsignacion.txt','rt')
    documento=f.readline().r
    while documento != " ":
        print(documento)
        input('presione enter')
        documento=f.readline()
    f.close()

if __name__=="__main__":
    main_read2()