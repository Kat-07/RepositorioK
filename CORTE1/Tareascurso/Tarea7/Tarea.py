import math

def calcular_modulo_vector(origen, fin):
    # Calcular las diferencias de coordenadas
    diferencia_x = fin[0] - origen[0]
    diferencia_y = fin[1] - origen[1]
    diferencia_z = fin[2] - origen[2]

    # Calcular las componentes rectangulares
    componente_x = diferencia_x
    componente_y = diferencia_y
    componente_z = diferencia_z

    # Calcular el módulo del vector
    modulo = math.sqrt(diferencia_x*2 + diferencia_y*2 + diferencia_z*2)

    return modulo, (componente_x, componente_y, componente_z)

# Solicitar las coordenadas del vector al usuario
origen_x = float(input("Ingrese la coordenada x del punto de origen: "))
origen_y = float(input("Ingrese la coordenada y del punto de origen: "))
origen_z = float(input("Ingrese la coordenada z del punto de origen: "))

fin_x = float(input("Ingrese la coordenada x del punto final: "))
fin_y = float(input("Ingrese la coordenada y del punto final: "))
fin_z = float(input("Ingrese la coordenada z del punto final: "))

# Crear las tuplas de origen y fin del vector
origen = (origen_x, origen_y, origen_z)
fin = (fin_x, fin_y, fin_z)

# Calcular el módulo y las componentes rectangulares del vector
modulo, componentes = calcular_modulo_vector(origen, fin)

# Imprimir los resultados
print("El modulo del vector es:", modulo)
print("Las componentes rectangulares del vector son:", componentes)