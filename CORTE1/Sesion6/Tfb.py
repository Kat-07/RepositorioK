#Realizar un programa que muestre en pantalla 
#la cantidad de dígitos solicitada por el usuario de la serie de Fibbonacci.
n=int(input('ingrese la cantidad de digitos de la seria Fibbonacci que desea obtener'))
a=0
b=1

if n==1:
        print('0')
elif n==2:
        print('0','1')
else:
        print(a)
        for i in range(n-1):
            total = a + b
            b=a
            a= total
            print(total)