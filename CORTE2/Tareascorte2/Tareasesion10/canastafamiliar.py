#Realice un programa para calcular el valor bruto de un producto alimenticio 
#según la última reforma tributaria del IVA de la canasta familiar del año 2023.
#"Primero se debe leer el archivo Alimentos.txt, 
#para organizar cada uno de los artículos según el valor del IVA. 
#El usuario ingresará un producto del listado, junto con el valor neto del mercado actual, 
#entonces el programa retornará el valor base del producto y el valor del iva discriminados.
#El programa funcionará continuamente hasta que el usuario escriba "salir""

#procedimiento=> PB=PF/1+IVA

def main_read():
    L=open('Alimentos.txt','rt')
    documento=L.read()
    L.close()
    print(documento)

def lectura():
    L=open('Alimentos.txt','rt')
    documento=L.readlines()
    L.close()
    Alimentos=[]
    for i in documento:
        Alimentos.append(i.rstrip('\n').split(','))
    for i in Alimentos:
        print(i)
    return documento

def proceso(documento):
    while 1:
        opc=input('¿Quieres saber el valor bruto de un producto? (si/no)')
        if opc=='si':   
            codigo=int(input('Por favor ingresa el codigo del alimento'))    
            for lista in documento:
                lista = lista.strip().split(",")
                valor2 =lista[2]
                if int(lista[0]) == codigo and valor2=='0':
                   precio=int(input('Por favor, ingresa el valor del producto'))
                   print(f'El valor bruto del producto ingresado es:{precio}')  
                if int(lista[0]) == codigo and valor2=='0.05':                  
                   precio=int(input('Por favor, ingresa el valor del producto'))
                   iva=precio/1.05
                   print(f'El valor bruto del producto ingresado es:{iva}')
                if int(lista[0]) == codigo and valor2=='0.19':                  
                   precio=int(input('Por favor, ingresa el valor del producto'))
                   iva=precio/1.19
                   print(f'El valor bruto del producto ingresado es:{iva}')
        elif opc=='no':
            break
        else:
            print('opcion invalida')

def main():
    lecturad=lectura()
    proceso(lecturad)

if __name__=="__main__":
    main()