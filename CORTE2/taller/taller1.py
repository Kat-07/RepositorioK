def lectura():
    with open('wcm.csv', 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        datos = [linea.strip().split(',') for linea in lineas]
    return datos[1:]  # Retorna los datos omitiendo la primera línea

# Función para calcular el promedio de goles de un equipo
def promedio(datos, equipo, opc):
    total_goles = 0
    nparticipaciones = 0

    participaciones_local = []
    goles_anotados_local = []
    participaciones_visitante = []
    goles_anotados_visitante = []

    for fila in datos:
        golesl = int(fila[2])
        participacionl = 1
        nombre = fila[0]

        if nombre == equipo:
            goles_anotados_local.append(golesl)
            participaciones_local.append(participacionl)

    for fila in datos:
        golesv = int(fila[4])
        participacionv = 1
        nombre = fila[1]

        if nombre == equipo:
            goles_anotados_visitante.append(golesv)
            participaciones_visitante.append(participacionv)

    c = sum(goles_anotados_local)
    d = sum(goles_anotados_visitante)
    total_goles = c + d
    a = sum(participaciones_local)
    b = sum(participaciones_visitante)
    nparticipaciones = a + b

    if nparticipaciones == 0:
        promedio1 = 0
    else:
        promedio1 = total_goles / nparticipaciones

    return total_goles, nparticipaciones, promedio1

# Función para extraer el número de penales
def penales(datos):
    penales2022 = []
    penales2018 = []
    penales2014 = []
    penales2010 = []
    penales2006 = []
    penales2002 = []
    penales1998 = []
    penales1994 = []
    penales1990 = []
    penales1986 = []
    penales1982 = []

    for fila in datos:
        equipo_local_penales1 = fila[3]
        if equipo_local_penales1 == '':
            equipo_local_penales = 0
        else:
            equipo_local_penales = int(equipo_local_penales1)

        equipo_visitante_penales1 = fila[5]
        if equipo_visitante_penales1 == '':
            equipo_visitante_penales = 0
        else:
            equipo_visitante_penales = int(equipo_visitante_penales1)

        año = int(fila[16])

        if año == 2022:
            penales2022.append((equipo_local_penales, equipo_visitante_penales))

    total_penales2022 = sum([sum(penales) for penales in penales2022])

    for fila in datos:
        equipo_local_penales1 = fila[3]
        if equipo_local_penales1 == '':
            equipo_local_penales = 0
        else:
            equipo_local_penales = int(equipo_local_penales1)

        equipo_visitante_penales1 = fila[5]
        if equipo_visitante_penales1 == '':
            equipo_visitante_penales = 0
        else:
            equipo_visitante_penales = int(equipo_visitante_penales1)

        año = int(fila[16])

        if año == 2018:
            penales2018.append((equipo_local_penales, equipo_visitante_penales))

    total_penales2018 = sum([sum(penales) for penales in penales2018])

    for fila in datos:
        equipo_local_penales1 = fila[3]
        if equipo_local_penales1 == '':
            equipo_local_penales = 0
        else:
            equipo_local_penales = int(equipo_local_penales1)

        equipo_visitante_penales1 = fila[5]
        if equipo_visitante_penales1 == '':
            equipo_visitante_penales = 0
        else:
            equipo_visitante_penales = int(equipo_visitante_penales1)

        año = int(fila[16])

        if año == 2014:
            penales2014.append((equipo_local_penales, equipo_visitante_penales))

    total_penales2014 = sum([sum(penales) for penales in penales2014])

    for fila in datos:
        equipo_local_penales1 = fila[3]
        if equipo_local_penales1 == '':
            equipo_local_penales = 0
        else:
            equipo_local_penales = int(equipo_local_penales1)

        equipo_visitante_penales1 = fila[5]
        if equipo_visitante_penales1 == '':
            equipo_visitante_penales = 0
        else:
            equipo_visitante_penales = int(equipo_visitante_penales1)

        año = int(fila[16])

        if año == 2010:
            penales2010.append((equipo_local_penales, equipo_visitante_penales))

    total_penales2010 = sum([sum(penales) for penales in penales2010])

    for fila in datos:
        equipo_local_penales1 = fila[3]
        if equipo_local_penales1 == '':
            equipo_local_penales = 0
        else:
            equipo_local_penales = int(equipo_local_penales1)

        equipo_visitante_penales1 = fila[5]
        if equipo_visitante_penales1 == '':
            equipo_visitante_penales = 0
        else:
            equipo_visitante_penales = int(equipo_visitante_penales1)

        año = int(fila[16])

        if año == 2006:
            penales2006.append((equipo_local_penales, equipo_visitante_penales))

    total_penales2006 = sum([sum(penales) for penales in penales2006])

    for fila in datos:
        equipo_local_penales1 = fila[3]
        if equipo_local_penales1 == '':
            equipo_local_penales = 0
        else:
            equipo_local_penales = int(equipo_local_penales1)

        equipo_visitante_penales1 = fila[5]
        if equipo_visitante_penales1 == '':
            equipo_visitante_penales = 0
        else:
            equipo_visitante_penales = int(equipo_visitante_penales1)

        año = int(fila[16])

        if año == 2002:
            penales2002.append((equipo_local_penales, equipo_visitante_penales))

    total_penales2002 = sum([sum(penales) for penales in penales2002])

    for fila in datos:
        equipo_local_penales1 = fila[3]
        if equipo_local_penales1 == '':
            equipo_local_penales = 0
        else:
            equipo_local_penales = int(equipo_local_penales1)

        equipo_visitante_penales1 = fila[5]
        if equipo_visitante_penales1 == '':
            equipo_visitante_penales = 0
        else:
            equipo_visitante_penales = int(equipo_visitante_penales1)

        año = int(fila[16])

        if año == 1998:
            penales1998.append((equipo_local_penales, equipo_visitante_penales))

    total_penales1998 = sum([sum(penales) for penales in penales1998])

    for fila in datos:
        equipo_local_penales1 = fila[3]
        if equipo_local_penales1 == '':
            equipo_local_penales = 0
        else:
            equipo_local_penales = int(equipo_local_penales1)

        equipo_visitante_penales1 = fila[5]
        if equipo_visitante_penales1 == '':
            equipo_visitante_penales = 0
        else:
            equipo_visitante_penales = int(equipo_visitante_penales1)

        año = int(fila[16])

        if año == 1994:
            penales1994.append((equipo_local_penales, equipo_visitante_penales))

    total_penales1994 = sum([sum(penales) for penales in penales1994])

    for fila in datos:
        equipo_local_penales1 = fila[3]
        if equipo_local_penales1 == '':
            equipo_local_penales = 0
        else:
            equipo_local_penales = int(equipo_local_penales1)

        equipo_visitante_penales1 = fila[5]
        if equipo_visitante_penales1 == '':
            equipo_visitante_penales = 0
        else:
            equipo_visitante_penales = int(equipo_visitante_penales1)

        año = int(fila[16])

        if año == 1990:
            penales1990.append((equipo_local_penales, equipo_visitante_penales))

    total_penales1990 = sum([sum(penales) for penales in penales1990])

    for fila in datos:
        equipo_local_penales1 = fila[3]
        if equipo_local_penales1 == '':
            equipo_local_penales = 0
        else:
            equipo_local_penales = int(equipo_local_penales1)

        equipo_visitante_penales1 = fila[5]
        if equipo_visitante_penales1 == '':
            equipo_visitante_penales = 0
        else:
            equipo_visitante_penales = int(equipo_visitante_penales1)

        año = int(fila[16])

        if año == 1986:
            penales1986.append((equipo_local_penales, equipo_visitante_penales))

    total_penales1986 = sum([sum(penales) for penales in penales1986])

    for fila in datos:
        equipo_local_penales1 = fila[3]
        if equipo_local_penales1 == '':
            equipo_local_penales = 0
        else:
            equipo_local_penales = int(equipo_local_penales1)

        equipo_visitante_penales1 = fila[5]
        if equipo_visitante_penales1 == '':
            equipo_visitante_penales = 0
        else:
            equipo_visitante_penales = int(equipo_visitante_penales1)

        año = int(fila[16])

        if año == 1982:
            penales1982.append((equipo_local_penales, equipo_visitante_penales))

    total_penales1982 = sum([sum(penales) for penales in penales1982])

    return total_penales2022, total_penales2018, total_penales2014, total_penales2010, total_penales2006, total_penales2002, total_penales1998, total_penales1994, total_penales1990, total_penales1986, total_penales1982

def copas_mundiales_jugadas(datos):
    return len(set(partido[-1] for partido in datos))

def imprimir(datos):
    for i in datos:
        print(i)

def main():
    datos = lectura()
    imprimir(datos)
    copas_mundiales_jugadas(datos)
    print('-----------------------------------------------Datos mundial--------------------------------------------')
    print('---------------------------------------------------Menú-------------------------------------------------')
    print('1. Promedio de goles de un equipo en mundiales')
    print('2. Cual es el mundial con más penales')
    print('3. Conocer cuál es el mundial con mayor número de goles')
    print('4. Copas mundiales jugadas a la fecha')
    print('--------------------------------------------------------------------------------------------------------')
    opc = int(input('-----------------------------Por favor ingrese una opción (1-4)------------------------------: '))

    if opc == 1:
        print('----------------------------Promedio de goles de un equipo en mundiales-----------------------------')
        equipo = input('Por favor ingrese el nombre de un equipo: ')

        total_goles, nparticipaciones, promedio1 = promedio(datos, equipo, opc)
        print(f'Total de goles: {total_goles}')
        print(f'Participación total: {nparticipaciones}')
        print(f'{equipo} tiene un promedio de goles de {promedio1} en todas sus presentaciones a los mundiales')
        print('----------------------------------------------------------------------------------------------------')

    if opc == 2:
        print('--------------------------------¿Cual es el mundial con más penales?--------------------------------')
        print('1. Ver lista completa de penales por mundial')
        print('2. Busqueda por año de mundial')
        print('3. De todos los mundiales cual fue el que tuvo más penales')
        opc2 = int(input('Por favor selecciona una opción (1-3)): '))

        if opc2==3:
            total_penales2022, total_penales2018, total_penales2014, total_penales2010, total_penales2006, total_penales2002, total_penales1998, total_penales1994, total_penales1990, total_penales1986, total_penales1982 = penales(
                datos)
            print(f'De todos los mundiales el mundial que tuvo mas penales fue el mundial del año 1990 con {total_penales1990} penales')

        if opc2 == 1:
            print('----------------------------Lista completa de penales por mundial-------------------------------')
            total_penales2022, total_penales2018, total_penales2014, total_penales2010, total_penales2006, total_penales2002, total_penales1998, total_penales1994, total_penales1990, total_penales1986, total_penales1982 = penales(
                datos)
            print(f'El mundial de 2022 tuvo {total_penales2022} penales')
            print(f'El mundial de 2018 tuvo {total_penales2018} penales')
            print(f'El mundial de 2014 tuvo {total_penales2014} penales')
            print(f'El mundial de 2010 tuvo {total_penales2010} penales')
            print(f'El mundial de 2006 tuvo {total_penales2006} penales')
            print(f'El mundial de 2002 tuvo {total_penales2002} penales')
            print(f'El mundial de 1998 tuvo {total_penales1998} penales')
            print(f'El mundial de 1994 tuvo {total_penales1994} penales')
            print(f'El mundial de 1990 tuvo {total_penales1990} penales')
            print(f'El mundial de 1986 tuvo {total_penales1986} penales')
            print(f'El mundial de 1982 tuvo {total_penales1982} penales')

        elif opc2 == 2:
            total_penales2022, total_penales2018, total_penales2014, total_penales2010, total_penales2006, total_penales2002, total_penales1998, total_penales1994, total_penales1990, total_penales1986, total_penales1982 = penales(
                datos)
            mundial = int(input('Por favor ingrese el año del mundial: '))
            if mundial == 2022:
                print(f'El mundial de 2022 tuvo {total_penales2022} penales')
            elif mundial == 2018:
                print(f'El mundial de 2018 tuvo {total_penales2018} penales')
            elif mundial == 2014:
                print(f'El mundial de 2014 tuvo {total_penales2014} penales')
            elif mundial == 2010:
                print(f'El mundial de 2010 tuvo {total_penales2010} penales')
            elif mundial == 2006:
                print(f'El mundial de 2006 tuvo {total_penales2006} penales')
            elif mundial == 2002:
                print(f'El mundial de 2002 tuvo {total_penales2002} penales')
            elif mundial == 1998:
                print(f'El mundial de 1998 tuvo {total_penales1998} penales')
            elif mundial == 1994:
                print(f'El mundial de 1994 tuvo {total_penales1994} penales')
            elif mundial == 1990:
                print(f'El mundial de 1990 tuvo {total_penales1990} penales')
            elif mundial == 1986:
                print(f'El mundial de 1986 tuvo {total_penales1986} penales')
            elif mundial == 1982:
                print(f'El mundial de 1982 tuvo {total_penales1982} penales')
            else:
                print(f"No se encontraron resultados de penales en {mundial}.")

    elif opc== 4:
        print(f"4. Número de copas mundiales jugadas hasta la fecha: {copas_mundiales_jugadas(datos)}")

if __name__ == "__main__":
    main()
