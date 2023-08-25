#Realizar un programa que muestre el producto entre dos números enteros 
#(negativos o positivos), realizando sumas sucesivas.

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








