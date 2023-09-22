class Pokemon():
    def __init__(self):
        self.nombre=None
        self.color=None
        self.categoria=None
        self.tipo=None
        self.codigo=None

    def ataquePokemon(self):
        return 'estoy atacando'


def main():
    pokemones=[]
    opc='n'
    while 1:
        pokemon=Pokemon()
        pokemon.nombre=input('Nombre del pokemon: ')
        pokemon.categoria=input('Categoria del pokemon: ')
        pokemon.color=input('Color del pokemon: ')
        pokemon.tipo=input('tipo del pokemon: ')
        pokemon.codigo=input('Codigo del pokemon: ')
        pokemones.append(pokemon)

        opc=input('Desea inscribir otro pokemon (y/n): ')
        if opc=='n':
            break
        elif opc!='y':
            print('Opcion invalida')

    print('\n---------Pokedex----------')
    for i in pokemones:
        print(f'Nombre: {i.nombre}\n'
            f'Tipo: {i.tipo}\n'
            f'Codigo: {i.codigo}\n'
            f'Ataca! ... {i.ataquePokemon()}\n'
            '--------------------------')


if __name__=="__main__":
    main()
