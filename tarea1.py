#Crear un programa basado en POO con las siguientes características:
#Crear una clase "Ciudadano" que incluya los campos privados Nombre, Cédula y Edad.
#Crear los setters y getters correspondientes a los campos, verificando que el número de cedula tenga
#entre 8 y 10 dígitos y que la edad ingresada sea un número positivo mayor que cero.
#Establecer un método "mostrar" que imprima la información, por ejemplo:
#Nombre: Nicolás - Edad: 28 - CC: 1289384734
#Establecer un método "esMayorDeEdad" que verifique si el ciudadano es o no mayor de edad.
#Realice el diagrama de clases (Representación UML)

# Diagrama UML
#-----------------------------------------------------
#                     Ciudadano                           -> Clase
#-----------------------------------------------------
#  -Nombre:str
#  -Cedula:int                                            -> Campos/constructor
#  -Edad:int
#-----------------------------------------------------
#  +Ciudadano()
#  +getNombre():str
#  +getCedula():int
#  +getEdad():int                                        -> setters y getters
#  +setNombre(nombre:str)
#  +setCedula(cedula:int)
#  +setEdad(edad:int)

#  -mostrar(nombre:str,cedula:int,edad:int):mostar
#  +getMostrar():str,int,int
#  -esMayorDeEdad(edad):esmayordeedad                    -> Metodos
#  +getEsMayorDeEdad(): int
#------------------------------------------------------

class Ciudadano:
    def __init__(self,nombre:str,cedula:int,edad:int):
        self.__nombre=nombre  #campo privado
        self.__cedula=cedula  #campo privado
        self.__edad=edad      #campo privado

    #-------------------setters------------------------

    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setCedula(self,cedula:int):
        if 8 <= len(str(cedula)) <=10:
            self.__cedula=cedula

    def setEdad(self,edad:int):
        if edad>0:
            self.__edad=edad

    #-------------------getters-------------------------

    def getNombre(self):
        return self.__nombre

    def getCedula(self):
        return self.__cedula
    
    def getEdad(self):
        return self.__edad
    
    #---------------------Metodos-----------------------

    def __mostrar(self):
        cedula=self.__cedula

        if 8<=len(str(cedula))<=10:
            return f'Nombre:{self.getNombre()} - Edad:{self.getEdad()} - CC:{cedula}'
        return  f'Nombre:{self.getNombre()} - Edad:{self.getEdad()} - CC: {cedula}-> cedula invalida'
    
    def getMostrar(self):
        ciudadano_datos=self.__mostrar()
        return ciudadano_datos 

    def __esMayorDeEdad(self):
        return self.getEdad()
    
    def getEsMayorDeEdad(self):
        edad=self.__esMayorDeEdad()
        if edad>=18:
            return f'{self.getNombre()} es mayor de edad'
        elif edad>0 and edad<18:
            return f'{self.getNombre()} es menor de edad'
        else:
            return f'Error, la edad no puede ser un numero negativo'
    #----------------------------------------------------

def main():
    while 1:
        nombre=input('Nombre: ')
        cedula=input('Cedula: ')
        edad=int(input('Edad: '))
        ciudadano=Ciudadano(nombre,cedula,edad)

        print('--------------------------------------------------------------------')
        print(f'{ciudadano.getMostrar()}')
        print(f'{ciudadano.getEsMayorDeEdad()}')
        print('--------------------------------------------------------------------')


if __name__=="__main__":
    main()