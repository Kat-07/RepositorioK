from random import choice as c


def repartir():
    deck='A23456789JQK'
    return c(deck)

def valor(card):
    jack=['J','Q','K']

    if card in jack:
        card=10
    elif card =='A':
        card=11
    else:
        card=int(card)
    return card

def conteo(mano):
    cartas=[]
    for i in range(len(mano)):
        cartas.append(valor(mano[i]))
    print(cartas)
    print(f'Conteo: {sum(cartas)}')

def inicio():
    mano=[]
    mano.append(repartir())
    mano.append(repartir())
    print(mano)
    conteo(mano)

    opc='y'
    while opc=='y':
        opc=input('Quiere otra carta? (y/n) ')
        if opc=='y':
            mano.append(repartir())
            conteo(mano)
            print(mano)
        elif opc=='n':
            break
        else:
            print('opcion invalida')
            opc='y'
    



if __name__=="__main__":
    inicio()
    