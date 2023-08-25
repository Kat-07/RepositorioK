import Fcn_ext

def main(): #se define una funcion
    a=int(input('ingrese un numero: '))
    b=int(input('ingrese otro numero: '))
    Fcn_ext.suma(a,b) #se invoca la otra funcion suma
    print(f'Ejecutado desde{__name__}')

if __name__=="__main__":
    main() #el programa inicia en la linea 9, se invoca la funcion