print('menú:\n',\
'1.Muestre los divisores positivos de un número.\n',\
'2.Calcular el producto entre dos números mediante sumas sucesivas.\n',\
'3.Muestre la cantidad de digitos deseados de la serie de Fibbonacci.\n')
prog=int(input('Seleccione un programa (1-3):'))

if(prog==1):

    n=int(input('Por favor, ingrese un numero'))
    if n!=0:
        print('El número 1 es divisible entre', n)
        for i in range(2,n+1,1):
            div=n%i
            if div==0:
                print('El número',i, 'es divisible entre', n)
    else:
        print('Ningun numero es divisible entre cero')

elif(prog==2):
    num1=int(input('Por favor, ingrese el primer numero: '))
    num2=int(input('Por favor, ingrese el segundo numero: '))
    
    if (num1<0) and (num2<0):
        num2=num2*-1
        num1=num1*-1

        resultado=0
        for i in range(1,num1+1):
            resultado=resultado+num2
        print('-',resultado)
            
    elif num1<0:
        resultado=0
        for i in range(1,num2+1):
            resultado=resultado+num1
        print(resultado)
        
    elif num2<0:
        resultado=0
        for i in range(1,num1+1):
            resultado=resultado+num2
        print(resultado)
    
    else:
        resultado=0
        for i in range(1,num2+1):
            resultado=resultado+num1
        print(resultado)

elif(prog==3):
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

else:
    print('Opcion invalida, por favor ingrese un número valido del menú')