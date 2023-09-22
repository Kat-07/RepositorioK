class Pokemon():
    def __init__(self):
        self.nombre=None
        self.color=None
        self.categoria=None
        self.tipo=None
        self.codigo=None
        self.region='Colombia'

    def correr(self):
        return 'estoy corriendo'

    def volar(self):
        return 'estoy volando'

    def quemar(self):
        return 'estoy quemando'

    def ataquePokemon(self):
        return 'estoy atacando'


def main():
    Pokemon1=Pokemon()
    Pokemon1.nombre='Pikachu'
    Pokemon1.color='Amarillo'
    Pokemon1.categoria='Raton'
    Pokemon1.tipo='Electrico'
    Pokemon1.codigo=25
    print(f'{Pokemon1.nombre}: {Pokemon1.correr()}\n'\
    f'region: {Pokemon1.region}')

    Charizard=Pokemon()
    Charizard.nombre='Charizard'
    Charizard.color='Naranja'
    Charizard.categoria='Dragon'
    Charizard.tipo='Fuego'
    Charizard.codigo=6
    print(f'{Charizard.nombre}: {Charizard.volar()}\n'\
    f'region: {Charizard.region}')

    Ninetales=Pokemon()
    Ninetales.nombre='Ninetales'
    Ninetales.color='Baige'
    Ninetales.categoria='Zorro'
    Ninetales.tipo='Fuego'
    Ninetales.codigo=38
    Ninetales.region='Peruano'
    print(f'{Ninetales.nombre}: {Ninetales.quemar()}\n'\
    f'region: {Ninetales.region}')


if __name__=="__main__":
    main()