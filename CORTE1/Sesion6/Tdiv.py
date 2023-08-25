n=int(input('Por favor, ingrese un numero'))
if n!=0:
    print('El número 1 es divisible entre', n)
    for i in range(2,n+1,1):
        div=n%i
        if div==0:
                print('El número',i, 'es divisible entre', n)
else:
     print('Ningun numero es divisible entre cero')
        
                
                

