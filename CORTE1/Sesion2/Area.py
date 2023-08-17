

print('Seleccione una opcion:\n',\
      '1. Calcula el area de un circulo\n',\
      '2. Calcula el area de un rectangulo\n',\
      '3. Calcula el area de un triangulo')
      
fig=input('ingrese el nombre de la figura: ')

A='NAN'

if(fig=='Circulo'):
    r=int(input('ingrese el valor del radio: '))
    A=3.1416*r**2
elif(fig=='Rectangulo'):
    b=int(input('ingrese el valor de la base'))
    h=int(input('ingrese el valor de la altura'))
    A=b*h
elif(fig=='triangulo'):
     b=int(input('ingrese el valor de la base'))
     h=int(input('ingrese el valor de la altura'))
     A=b*h/2
else:
    print('ingreso una opcion invalida')
print('el valor del area es',A)

    

