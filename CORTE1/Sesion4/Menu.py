print('menú:\n',\
'1.Verifique si una letra es vocal o consonante.\n',\
'2.Calcular el costo de parqueo.\n',\
'3.Verificar si se puede formar un triangulo.\n')
prog=int(input('Seleccione un programa (1-3):'))
if(prog==1):
    L=input('por favor ingrese una letra del abecedario')
    if L=='a'or L=='e' or L=='i' or L=='o' or L=='u':
        print('La letra',L,'es vocal')
    else:
        print('La letra',L,'es consonante')
elif(prog==2):
    T=float(input('ingrese el tiempo de parqueo en minutos:'))
    costo=T*139
    IVA=costo*0.19
    Total=costo+IVA
    CTA=round(Total/50)*50
    print('Total a pagar:', CTA)
elif(prog==3):
    Lado1=float(input('Por favor, ingrese la longitud del primer lado:'))
    Lado2=float(input('Por favor, ingrese la longitud del segundo lado:'))
    Lado3=float(input('Por favor, ingrese la longitud del tercer lado:'))

    if Lado1+Lado2>Lado3 and Lado1+Lado3>Lado2 and Lado2+Lado3>Lado1:
        if Lado1==Lado2 and Lado2==Lado3:
            print('Se puede formar un triangulo equilatero')
        elif(Lado1==Lado2 or Lado2==Lado3 or Lado3==Lado1):
            print('Se puede formar un triangulo isosceles')
        else:
            print('Se puede formar un triangulo escaleno')
    else:
        print('No se puede formar un triangulo con las longitudes dadas')
else:
    print('Opcion invalida, por favor ingrese un número valido del menú')