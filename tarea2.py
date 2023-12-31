#Continúe el ejercicio de la tarea anterior con las siguientes características:
#Cree tres clases heredadas de la clase "Ciudadano", basadas en tres profesiones, 
#que incluyan mínimo 2 campos propios cada una.
#Cree por lo menos un método único para cada clase heredada, 
#que tenga relación con cada una de las profesiones seleccionadas.
#En una de las tres clases heredadas, sobrecargue un método.

class Ciudadano:
    def __init__(self,nombre:str,cedula:str,edad:int):
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
        
    def __medallas(self):
        return 'Ha ganado 3 medallas'

    def getMedallas(self):
        medallas=self.__medallas()
        return f'{medallas}'

    #----------------------------------------------------

class Ingeniero(Ciudadano):
    def __init__(self, nombre: str, edad: int, cedula: str,robotsRealizados:int,proyectosCumplidos:int):
        super().__init__(nombre, edad, cedula)
        self.__robotsRealizados=robotsRealizados
        self.__proyectosCumplidos=proyectosCumplidos

    #-------Setters----------
    def setRobotsRealizados(self,robotsRealizados:int):
        self.__robotsRealizados=robotsRealizados
    def setProyectosCumplidos(self,proyectosCumplidos:int):
        self.__proyectosCumplidos=proyectosCumplidos
    
    #--------Getters---------
    def getRobotsRealizados(self):
        return self.__robotsRealizados
    def getProyectosCumplidos(self):
        return self.__proyectosCumplidos
    
    #--------Metodo----------
    def robots(self):
        return f'el ingeniero {self.getNombre()} ha realizado {self.getRobotsRealizados()} robots'

class Futbolista(Ciudadano):
    def __init__(self, nombre: str, edad: int, cedula: str,\
        goles:int,equipo:str):
        super().__init__(nombre, edad, cedula)
        self.__goles=goles
        self.__equipo=equipo

    #-------Setters----------
    def setGoles(self,goles:int):
        self.__goles=goles
    def setEquipo(self,equipo:str):
        self.__equipo=equipo
    
    #--------Getters---------
    def getGoles(self):
        return self.__goles
    def getEquipo(self):
        return self.__equipo
    
    #--------Metodo----------
    def anotar(self):
        return f'el jugador {self.getNombre()} ha anotado {self.getGoles()} goles'
    
    def medallas(self):
        return 'ha ganado 7 medallas'
    
class Neurocirujano(Ciudadano):
    def __init__(self, nombre: str, edad: int, cedula: str,\
        cirugiasOctubre:int,añosFormacion:int):
        super().__init__(nombre, edad, cedula)
        self.__cirugiasOctubre=cirugiasOctubre
        self.__añosFormacion=añosFormacion

    #-------Setters----------
    def setCirugiasOctubre(self,cirugiasOctubre:int):
        self.__cirugiasOctubre=cirugiasOctubre
    def setAñosFormacion(self,añosFormacion:int):
        self.__añosFormacion=añosFormacion
    
    #--------Getters---------
    def getCirugiasOctubre(self):
        return self.__cirugiasOctubre
    def getAñosFormacion(self):
        return self.__añosFormacion
    
    #--------Metodo----------
    def cirugias(self):
        return f'el Neurocirujano {self.getNombre()} ha realizado {self.getCirugiasOctubre()} cirugías en el mes de octubre '

def main():
    
    print('\n--------------------------------------------------------------------')
    inscrito1=Ingeniero('Kevin Warwick','3456738',37,27,32)
    print(f'Nombre: {inscrito1.getNombre()}\n',\
        f'Edad: {inscrito1.getEdad()}\n',\
            f'Cedula: {inscrito1.getCedula()}\n',\
                f'#Robots hechos: {inscrito1.getRobotsRealizados()}\n',\
                f'#Proyectos hechos: {inscrito1.getProyectosCumplidos()}\n')
    print(inscrito1.robots())
   
    print('\n------------------------------------')
    inscrito2=Futbolista('Falcao García','387632894',35,34,'Seleccion Colombia')
    print(f'Nombre: {inscrito2.getNombre()}\n',\
        f'Edad: {inscrito2.getEdad()}\n',\
            f'Cedula: {inscrito2.getCedula()}\n',\
                f'#Goles: {inscrito2.getGoles()}\n',\
                f'Equipo: {inscrito2.getEquipo()}\n')
    print(inscrito2.anotar())
    print(inscrito2.medallas())

    print('\n------------------------------------')
    inscrito3=Neurocirujano(' Derek Shepherd','1045682',42,39,25)
    print(f'Nombre: {inscrito3.getNombre()}\n',\
        f'Edad: {inscrito3.getEdad()}\n',\
            f'Cedula: {inscrito3.getCedula()}\n',\
                f'#Cirugias en octubre 2023: {inscrito3.getCirugiasOctubre()}\n',\
                f'#Años de formación: {inscrito3.getAñosFormacion()}\n')
    print(inscrito3.cirugias())

    print('--------------------------------------------------------------------')     
    ciudadano=Ciudadano('Kat','1067839962',19)
    print(f'{ciudadano.getMostrar()}')
    print(f'{ciudadano.getEsMayorDeEdad()}')
    print(f'{ciudadano.getMedallas()}')
    print('--------------------------------------------------------------------')


if __name__=="__main__":
    main()