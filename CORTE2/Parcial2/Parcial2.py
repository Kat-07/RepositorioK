
#Programa que calcule valor de resistencia
#banda1, banda2, banda3 multiplica, banda 4 tolerancia
def resistencia(colores):
    banda1=colores[0]
    banda2=colores[1]
    banda3=colores[2]

    Banda12=[]
    Banda12.append(banda1)
    Banda12.append(banda2)

    Banda=[0,1,2,3,4,5,6,7,8,9]
    Banda3=[1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]

    print('-----------Bandas-----------')
    print(f'Color banda 1: {banda1}')
    print(f'Color banda 2: {banda2}')
    print(f'Color banda 3: {banda3}')

    print('----------------------------')

    Digitos=[]
    for i in Banda12:
        if i=='negro':
            banda=Banda[0]
            Digitos.append(banda)
        elif i=='cafe':
            banda=Banda[1]
            Digitos.append(banda)
        elif i=='rojo':
            banda=Banda[2]
            Digitos.append(banda)
        elif i=='naranja':
            banda=Banda[3]
            Digitos.append(banda)
        elif i=='amarillo':
            banda=Banda[4]
            Digitos.append(banda)
        elif i=='verde':
            banda=Banda[5]
            Digitos.append(banda)
        elif i=='azul':
            banda=Banda[6]
            Digitos.append(banda)
        elif i=='morado':
            banda=Banda[7]
            Digitos.append(banda)
        elif i=='gris':
            banda=Banda[8]
            Digitos.append(banda)
        elif i=='blanco':
            banda=Banda[9]
            Digitos.append(banda)

    if banda3=='negro':
        B1=Digitos[0]
        B2=Digitos[1]
        valor=B1+(B2*0.1)*10
        print(f'Respuesta: {valor} Ohms')

    elif banda3=='cafe':
        B1=Digitos[0]
        B2=Digitos[1]
        valor=(B1*100)+(B2*10)
        print(f'Respuesta: {valor} Ohms')        
    
    elif banda3=='rojo':
        B1=Digitos[0]
        B2=Digitos[1]
        valor=B1+(B2*0.1)
        print(f'Respuesta: {valor} *10^2 Ohms')        

    elif banda3=='naranja':
        B1=Digitos[0]
        B2=Digitos[1]
        valor=B1+(B2*0.1)
        print(f'Respuesta: {valor} *10^3 Ohms')      

    elif banda3=='amarillo':
        B1=Digitos[0]
        B2=Digitos[1]
        valor=B1+(B2*0.1)
        print(f'Respuesta: {valor} *10^4 Ohms')  

    elif banda3=='verde':
        B1=Digitos[0]
        B2=Digitos[1]
        valor=B1+(B2*0.1)
        print(f'Respuesta: {valor} Mega-Ohms')  

    elif banda3=='azul':
        B1=Digitos[0]
        B2=Digitos[1]
        valor=B1+(B2*0.1)
        print(f'Respuesta: {valor} *10^6 Ohms')  

    elif banda3=='morado':
        B1=Digitos[0]
        B2=Digitos[1]
        valor=B1+(B2*0.1)
        print(f'Respuesta: {valor} *10^7 Ohms')    

    elif banda3=='gris':
        B1=Digitos[0]
        B2=Digitos[1]
        valor=B1+(B2*0.1)
        print(f'Respuesta: {valor} *10^8 Ohms')  

    elif banda3=='blanco':
        B1=Digitos[0]
        B2=Digitos[1]
        valor=B1+(B2*0.1)
        print(f'Respuesta: {valor} *10^9 Ohms')  

def main():
    banda1=input('Por favor ingrese el color de la banda 1')
    banda2=input('Por favor ingrese el color de la banda 2')
    banda3=input('Por favor ingrese el color de la banda 3')
    colores=[banda1,banda2,banda3]
    Resistencia=resistencia(colores)

if __name__=="__main__":
    main()
