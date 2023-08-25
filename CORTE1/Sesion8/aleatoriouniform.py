import random as r

def app():
    pal=''
    while pal != 'exit':
        x=r.uniform(100,180)
        print(x)
        pal=input('Para salir escriba exit')

if __name__ =="__main__":
    app() 