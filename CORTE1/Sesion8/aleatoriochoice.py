import random as r

def app():
    pal=''
    nombre='kat'
    while pal != 'exit':
        x=r.choice(nombre)
        print(x)
        pal=input('Para salir escriba exit')

if __name__ =="__main__":
    app() 