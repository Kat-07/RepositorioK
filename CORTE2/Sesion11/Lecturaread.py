
def main():
    f=open('matrizAsignacion.txt','rt')
    documento=f.read()
    f.close()
    print(documento)

if __name__=="__main__":
    main()