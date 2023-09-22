def factorial(x):
    if x>0:
        fac=x*factorial(x-1)
        print(fac)
    else:
        return 1
    return fac


def main():
    num=int(input('Ingrese un numero: '))
    resultado=factorial(num)
    print(f'El resultado es: {resultado}')

if __name__=="__main__":
    main()