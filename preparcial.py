class Producto:
    def __init__(self,nombre:str,precio:float, cantidad_disponible:int):
        self.__nombre=nombre  #campo privado
        self.__precio=precio #campo privado
        self.__cantidad_disponible=cantidad_disponible #campo privado

    #-------------------setters------------------------

    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setPrecio(self,precio:float):
        self.__precio=precio

    def setCantidad_disponible(self,cantidad_disponible:int):
        self.__cantidad_disponible=cantidad_disponible

    #-------------------getters-------------------------

    def getNombre(self):
        return self.__nombre

    def getPrecio(self):
        return self.__precio
   
    def getCantidad_disponible(self):
        return self.__cantidad_disponible
   
    #-----------------------metodos----------------------------
    def info_producto(self):
        return self.__nombre, self.__precio, self.__cantidad_disponible

    def verificar_disponibilidad(self):
        if self.__cantidad_disponible>0:
            return True
        return False
   
    def restar_cantidad(self, cantidad:int): #Como envio la cantidad ingresada por el cliente a este parametro
        disponible=self.verificar_disponibilidad()
        if disponible:
            cantidad_restante=self.getCantidad_disponible()-cantidad
            self.setCantidad_disponible=cantidad_restante
            if cantidad_restante==0 or cantidad_restante>0:
                return True
            return False
   
#-------------------subclase1----------------------

class Snack(Producto):
    def __init__(self, nombre: str, precio: float,cantidad_disponible:int, tipo:str):
        super().__init__(nombre, precio, cantidad_disponible)
        self.__tipo=tipo

    #-------Setters----------
    def setTipo(self,tipo:str):
        self.__tipo=tipo

    #--------Getters---------
    def getTipo(self):
        return self.__tipo

    #--------Metodo----------
    def info_producto(self):
        return self.__nombre, self.__precio,self.__cantidad_disponible,self.__tipo
   
#-----------------subclase2--------------------------
class Bebidas(Producto):
    def __init__(self, nombre: str, precio: float,cantidad_disponible:int, clase:str, tamaño:str):
        super().__init__(nombre, precio, cantidad_disponible)
        self.__clase=clase
        self.__tamaño=tamaño

    #-------Setters----------
    def setClase(self,clase:str):
        self.__clase=clase
    def setTamaño(self,tamaño:str):
        self.__tamaño=tamaño

    #--------Getters---------
    def getClase(self):
        return self.__clase
    def getTamaño(self):
        return self.__tamaño

    #--------Metodo----------
    def info_producto(self):
        return self.__nombre, self.__precio,self.__cantidad_disponible,self.__clase,self.__tamaño
   
#--------------------------------------------------------------------------------------------

class Dispensadora:
    def __init__(self):
        self.__producto=[]  #campo privado
        self.__total_ventas=0 #campo privado

    #-------Setters----------
    def setProducto(self,producto):
        self.__producto.append(producto)
    def setTotal_ventas(self,total_ventas):
        self.__total_ventas=total_ventas

    #--------Getters---------
    def getProducto(self):
        return self.__producto
    def getTotal_ventas(self):
        return self.__total_ventas

    #--------Metodo----------
    def agregar_producto(self,item:object):
        self.setProducto(item)
           
    def obtener_total_venta(self,item:object,cantidad:int):
        total=item.getPrecio()*cantidad
        print(f'Total: {total}')

    def realizar_venta(self,item:object, cantidad:int):
        item.restar_cantidad(cantidad)
        if item.restar_cantidad(cantidad):
            self.__total_ventas += item.getPrecio() * cantidad
            return print('venta realizada')
        return print('venta no realizada')

        
def main():

    while 1:
        snack1=Snack('chocorramo',2700,5,'dulce')
        snack2=Snack('papas',2000,10,'salado')
        bebida1=Bebidas('cristal', 2800,6,'agua', '250ml')
        bebida2=Bebidas('coca cola', 4000,8,'gaseosa','600ml')
        item = Dispensadora()
        item.agregar_producto(snack1)
        item.agregar_producto(snack2)
        item.agregar_producto(bebida1)
        item.agregar_producto(bebida2)

        print('---------------------Bienvenido-----------------------')
        print('Snack:')
        print(f'1. {snack1.getNombre()}' )
        print(f'2. {snack2.getNombre()}')
        print('Bebidas:')
        print(f'3. {bebida1.getNombre()}' )
        print(f'4. {bebida2.getNombre()}')
        opc=int(input('Ingrese una opción:'))
        if opc==1 or opc==2 or opc==3 or opc==4:
            cantidad=int(input('Ingrese cantidad deseada: '))
            if cantidad>0:
                if opc==1:
                    item.obtener_total_venta(snack1,cantidad)
                    item.realizar_venta(snack1,cantidad)
                    
                elif opc==2:
                    item.obtener_total_venta(snack2,cantidad)
                    item.realizar_venta(snack2,cantidad)
                    
                elif opc==3:
                    item.obtener_total_venta(bebida1,cantidad)
                    item.realizar_venta(bebida1,cantidad)
                   
                elif opc==4:
                    item.obtener_total_venta(bebida2,cantidad)
                    item.realizar_venta(bebida2,cantidad)     
            else:
                print('Error la cantidad debe ser mayor a 0')
        else:
            break

if __name__=="__main__":
    main()