from factorial1 import factorial1 as f

def combinaciones():
    n=int(input('Ingrese el numero de elementos: '))
    m=int(input('Ingrese el numero de grupos: '))
    cmb=(f(n)/f(m)*f(n-m))
    print(f'el numero de combinaciones posibles es: {cmb}') 

if __name__=="__main__":
    combinaciones()
