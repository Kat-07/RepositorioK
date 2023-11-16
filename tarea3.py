# Con base en un ejercicio anterior, para calcular el precio bruto de un elemento de la canasta familiar de acuerdo al IVA.
# Cree una SuperClase llamada articulos, con los parámetros (nombre, precio)
# Cree tres subClases para organizar los tres tipos de artículos de la canasta familiar de acuerdo al IVA aplicado(0%, 5% o 19%),
# que heredan los parámetros del padre.
# Utilice una función para calcular el precio bruto y su respectivo 
# valor de IVA de acuerdo a la lista de alimentos de la canasta familiar.

class Articulos:
    def __init__(self,nombre:str,precio:float):
        self.__nombre=nombre  #campo privado
        self.__precio=precio #campo privado

    #-------------------setters------------------------

    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setPrecio(self,precio:float):
        self.__precio=precio

    #-------------------getters-------------------------

    def getNombre(self):
        return self.__nombre

    def getPrecio(self):
        return self.__precio

class IvaCero(Articulos):
    def __init__(self, nombre: str, precio: float):
        super().__init__(nombre, precio)

    #--------Metodo----------
    def __calculo(self):
        iva=0
        return f'Valor base: {self.getPrecio()}, Iva={iva}'
    
    def getCalculo(self):
        datos=self.__calculo()
        return f'{datos}'

class IvaCinco(Articulos):
    def __init__(self, nombre: str, precio: float):
        super().__init__(nombre, precio)
       
    #--------Metodo----------
    def __calculo(self):
        valor_base=self.getPrecio()/1.05
        iva=self.getPrecio()-valor_base
        return f'Valor base: {valor_base}, Iva={iva}'
    
    def getCalculo(self):
        return self.__calculo()

class IvaDiecinueve(Articulos):
    def __init__(self, nombre: str, precio: float):
        super().__init__(nombre, precio)
 
    #--------Metodo----------
    def __calculo(self):
        valor_base=self.getPrecio()/1.19
        iva=self.getPrecio()-valor_base
        return f'Valor base: {valor_base}, Iva={iva}' 
    
    def getCalculo(self):
        return self.__calculo()
    
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
        print('--------------------------------------------------------------------')
        nombre=input('Por favor ingresa el nombre del alimento: ')
        precio=input('Precio: ')
        producto=Articulos(nombre,float(precio))
        for lista in documento:
                lista = lista.strip().split(",")
                valor2=lista[2]
                if lista[1] == nombre and valor2=='0':
                   iva_cero=IvaCero(nombre,float(precio)) 
                   print(f'{iva_cero.getCalculo()}')
            
                elif lista[1] == nombre and valor2=='0.05':   
                   iva_cinco=IvaCinco(nombre,float(precio)) 
                   print(f'{iva_cinco.getCalculo()}')

                elif lista[1] == nombre and valor2=='0.19':                  
                   iva_diecinueve=IvaDiecinueve(nombre,float(precio)) 
                   print(f'{iva_diecinueve.getCalculo()}')
        print('--------------------------------------------------------------------')

def main():
    lecturad=lectura()
    proceso(lecturad)
    
if __name__=="__main__":
    main()