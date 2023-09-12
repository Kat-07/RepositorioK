import random as r

def repartir():
    baraja='A23456789JQK'
    carta=r.choice(baraja)
    return carta

def contador(mano):
    cartas=[]
    for i in range(len(mano)):
        cartas.append(valor(mano[i]))
    print(cartas)
    if 'A' in mano:
        conteo=sum(cartas)
        while conteo>21 and 'A' in mano:
            indise=mano.index('A')
            cartas[indise] = 1
            conteo=sum(cartas)
    return sum(cartas)
   
def valor(baraja):
    jack=['J','Q','K']
    if baraja in jack:
        baraja=10
    if baraja=='A':
        baraja=11
    else:
        baraja=int(baraja)
    return baraja

def inicio():
    mano=[]
    mano.append(repartir())
    mano.append(repartir())
    print (mano)
    total=contador(mano)
    print(f'contador: {total}')
    if total>21:
        print('__busted__')
    
    opc='y'
    while opc=='y':
        
        opc=input('Quiere otra carta? (y/n) ')
        if opc=='y':
            mano.append(repartir())
            print(mano)
            total=contador(mano)
            print(f'contador: {total}')
            if total>21:
                print('__busted__')
                break
        elif opc=='n':
            break
        else:
            print('opcion invalida')
            opc='y'

if __name__=='__main__':
    inicio()

    