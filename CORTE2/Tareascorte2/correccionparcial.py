import random as r

def repartir_valor():
    baraja='2222AAAA'
    for i in range(1):
        Cartas=[]
        Cartas.append(r.choice(baraja))
        Cartas.append(r.choice(baraja))
        print(Cartas)

    valor_cartas=[]
    for i in range(len((Cartas))):
        valor_cartas.append(valor(Cartas[i]))
    print(valor_cartas)
    Conteo=sum(valor_cartas)
    print('conteo:',Conteo) 

    opc='y'
    while opc=='y':
        if Conteo==21:
            print('¡¡___BLACKJACK___!!')
            break
        con=len(Cartas)
        n=Cartas.count('A')
        n2=Cartas.count(1)
        if Conteo>21 and con==2 and n==2:
                    Devolver=Cartas.index('A')
                    Cartas.insert(Devolver,1)
                    Cartas.remove('A')
                    valor_cartas=[]
                    for i in range(len((Cartas))):
                        valor_cartas.append(valor(Cartas[i]))
                    print(valor_cartas)
                    Conteo=sum(valor_cartas)
                    print('conteo:',Conteo)
        elif Conteo>21 and n==1 and n2!=1:
                    Devolver=Cartas.index('A')
                    Cartas.insert(Devolver,1)
                    Cartas.remove('A')
                    valor_cartas=[]
                    for i in range(len((Cartas))):
                        valor_cartas.append(valor(Cartas[i]))
                    print(valor_cartas)
                    Conteo=sum(valor_cartas)
                    print('conteo:',Conteo)
                    if Conteo==21:
                        print('___BLACKJACK___')
                        break
        elif Conteo>21 and con>=3 and n==2:
                    if 1 in Cartas:
                        print('____Busted____')
                        break
                    else:
                        Devolver=Cartas.index('A')
                        Cartas.insert(Devolver,1)
                        Cartas.remove('A')
                        valor_cartas=[]
                        for i in range(len((Cartas))):
                            valor_cartas.append(valor(Cartas[i]))
                        print(valor_cartas)
                        Conteo=sum(valor_cartas)
                        print('conteo:',Conteo)
                        if Conteo==21:
                            print('___BLACKJACK___')
                            break
        x=Cartas.count(1)           
        if Conteo>21 or Conteo>21 and x==1:
            print('____Busted____')
            break
        opc=input('Quiere otra carta? (y/n)')                
        if opc=='y':            
            Cartas.append(r.choice(baraja))
            print(Cartas)
            valor_cartas=[]
            for i in range(len((Cartas))):
                valor_cartas.append(valor(Cartas[i]))
            print(valor_cartas)
            Conteo=sum(valor_cartas)
            print('conteo:',Conteo) 
        elif opc=='n':
            break
        else:
            print('opcion invalida')
            opc='y'

def valor(c):
    jack=['J','Q','K']
    if c in jack:
        c=10
    elif c =='A':
        c=11
    else:
        c=int(c)
    return c

if __name__=="__main__":
    print('Bienvenido a BLACKJACK')
    print('¡Que comience el juego!')
    repartir_valor()