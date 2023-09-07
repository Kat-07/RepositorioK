
import random as r

def cartas():
    baraja='A23456789QJK'
    for i in range(1):
        C1=r.choice(baraja)
        C2=r.choice(baraja)
        cartas=[C1,C2]
        print(cartas)
        conteo(cartas)

def valor(c):
    jack=['J','Q','K']
    if c in jack:
        c=10
    elif c =='A':
        c=11
    else:
        c=int(c)
    return c

def conteo(cartas):
    valor_cartas=[]
    for i in range(len((cartas))):
        valor_cartas.append(valor(cartas[i]))
    print(valor_cartas)
    conteo=sum(valor_cartas)
    print('Conteo:',conteo)




if __name__=="__main__":
    print('Bienvenido a BLACKJACK')
    print('¡Que comience el juego!')
    cartas()
