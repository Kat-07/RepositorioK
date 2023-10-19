#Realizar un ejercicio donde se calcule el IMC de las siguientes 4 personas, cuyos valores se ven en la tabla. 
#El sistema debe mostrar el valor de IMC obtenido para cada uno de las personas indicado su correspondiente escala.

#Nombre estatura peso
#Pedro Caceres 188 97
#Maria Pérez 160 47
#Julian Dominguez 158 58
#Jessica Fuentes 170 73

class Personas:
    def init(self):
        self.nombre=None
        self.estatura=None
        self.peso=None
    
    def IMC(self):
        IMC=self.peso/((self.estatura/100)**2)
        if IMC <= 18.5:
            return str('Por debajo')
        elif IMC <=24.9:
            return str('Saludable')
        elif IMC <=29.9:
            return str('Sobrepeso')
        elif IMC <=34.9:
            return str('Obesidad I')
        elif IMC <=39.9:
            return str('Obesidad II')
        elif IMC >40:
            return str('obesidad III')

def main():
    persona1 = Personas()
    persona1.nombre='Pedro Caceres'
    persona1.estatura=188
    persona1.peso=97

    persona2 = Personas()
    persona2.nombre='María Perez'
    persona2.estatura=160
    persona2.peso=47

    persona3 = Personas()
    persona3.nombre='Julian Dominguez'
    persona3.estatura=158
    persona3.peso=58

    persona4 = Personas()
    persona4.nombre='Jessica Fuentes'
    persona4.estatura=170
    persona4.peso=73
    
    print('--------------------------------IMC------------------------------')
    print(f'    Nombre         Estatura      Peso  ')
    print(f'{persona1.nombre}        188          97     resultado: {persona1.IMC()}')
    print(f'{persona2.nombre}          160          47     resultado: {persona2.IMC()}')
    print(f'{persona3.nombre}     158          58     resultado: {persona3.IMC()}')
    print(f'{persona4.nombre}      170          73     resultado: {persona4.IMC()}')
    print('-----------------------------------------------------------------')

if __name__=="__main__":
    main()