# Define una función para cargar los datos del archivo CSV
def cargar_datos():
    # Abre el archivo 'wcm.csv' en modo lectura y codificado en utf-8
    with open('wcm.csv', 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()  # Lee todas las líneas del archivo
        # Divide cada línea en una lista y elimina espacios en blanco alrededor
        datos = [linea.strip().split(',') for linea in lineas]
    return datos[1:]  # Retorna los datos omitiendo la primera línea de encabezados

# Define funciones para cada punto solicitado

# 1. Conocer el número de copas mundo que un país ha ganado
def copas_ganadas(pais):
    return sum(1 for partido in datos if partido[0] == pais and int(partido[2]) > int(partido[4]))

# 2. Conocer el numero de subcampeonatos que un país ha ganado
def subcampeonatos(pais):
    return sum(1 for partido in datos if partido[1] == pais and int(partido[2]) < int(partido[4]))

# 3. Conocer el numero de participaciones de un equipo al mundial 
def participaciones(pais):
    return sum(1 for partido in datos if pais in partido[:2])

# 4. Conocer el numero de copas mundiales jugadas hasta la fecha 
def copas_mundiales_jugadas():
    return len(set(partido[-1] for partido in datos))

# 5. Conocer el número de asistentes a las copas mundiales
def asistentes_totales():
    return sum(int(partido[10]) for partido in datos)

# 6. Conocer el número de finales disputadas por penales
def finales_penales():
    return sum(1 for partido in datos if int(partido[3]) > 0 or int(partido[5]) > 0)

# 7. Conocer el número de goles a favor de los equipos en los mundiales 
def goles_a_favor(pais):
    return sum(int(partido[2]) if partido[0] == pais else int(partido[4]) for partido in datos)

# 8. Conocer el número de goles en contra de los equipos en los mundiales 
def goles_en_contra(pais):
    return sum(int(partido[4]) if partido[0] == pais else int(partido[2]) for partido in datos)

# 9. Conocer la diferencia de goles en todas sus presentaciones 
def diferencia_de_goles(pais):
    return goles_a_favor(pais) - goles_en_contra(pais)

# 10. Conocer el promedio de goles de un equipo en mundiales
def promedio_goles(pais):
    return goles_a_favor(pais) / participaciones(pais) if participaciones(pais) > 0 else 0

# 11. Conocer cuantas veces se han enfrentado 2 equipos en los mundiales
def enfrentamientos(equipo1, equipo2):
    return sum(1 for partido in datos if (equipo1 in partido[:2] and equipo2 in partido[:2]))

# 12. Conocer cual es el mundial con más penales
def mundial_con_mas_penales():
    mundiales = set(partido[-1] for partido in datos)
    penales_por_mundial = {m: sum(1 for partido in datos if partido[-1] == m and (int(partido[3]) > 0 or int(partido[5]) > 0)) for m in mundiales}
    return max(penales_por_mundial, key=penales_por_mundial.get)

# 13. Conocer cual es el mundial con mayor número de goles 
def mundial_con_mas_goles():
    mundiales = set(partido[-1] for partido in datos)
    goles_por_mundial = {m: sum(int(partido[2]) + int(partido[4]) for partido in datos if partido[-1] == m) for m in mundiales}
    return max(goles_por_mundial, key=goles_por_mundial.get)

# 14. Conocer cuales fueron las mayores goleadas de los mundiales
def mayores_goleadas():
    max_goleada = max(int(partido[2]) if int(partido[2]) > int(partido[4]) else int(partido[4]) for partido in datos)
    return [(partido[0], partido[1], partido[-1]) for partido in datos if int(partido[2]) == max_goleada or int(partido[4]) == max_goleada]

# Cargar los datos
datos = cargar_datos()

# Función principal
def main():
    print("Bienvenido al analizador de copas mundiales.")
    print("¿Qué información deseas obtener?")
    print("1. Número de copas mundiales ganadas por un país.")
    print("2. Número de subcampeonatos de un país.")
    print("3. Número de participaciones de un equipo al mundial.")
    print("4. Número de copas mundiales jugadas hasta la fecha.")
    print("5. Número de asistentes a las copas mundiales.")
    print("6. Número de finales disputadas por penales.")
    print("7. Número de goles a favor de los equipos en los mundiales.")
    print("8. Número de goles en contra de los equipos en los mundiales.")
    print("9. Diferencia de goles en todas sus presentaciones.")
    print("10. Promedio de goles de un equipo en mundiales.")
    print("11. Cuantas veces se han enfrentado 2 equipos en los mundiales.")
    print("12. En qué mundial hubo más penales.")
    print("13. En qué mundial hubo más goles.")
    print("14. Mayores goleadas en los mundiales.")
    
    opcion = int(input("Ingrese el número correspondiente a la información que desea obtener: "))

    if opcion in range(1, 12):
        print("¿Deseas ver información de un país en específico? (Sí/No)")
        opcion_pais = input().lower()
        if opcion_pais == 'si':
            print("Lista de todos los países en la lista:")
            paises = set(partido[0] for partido in datos) | set(partido[1] for partido in datos)
            print(sorted(paises))
            pais = input("Ingrese el nombre del país en minúsculas para saber la información: ").capitalize()
        else:
            pais = None
    elif opcion == 12:
        pais = None
    elif opcion == 13:
        pais = None
    else:  # En el caso de la opción 14, no es necesario especificar un país
        pais = None

    if opcion == 1:
        print(f"1. Número de copas mundiales ganadas por {pais}: {copas_ganadas(pais)}")
    elif opcion == 2:
        print(f"2. Número de subcampeonatos de {pais}: {subcampeonatos(pais)}")
    elif opcion == 3:
        print(f"3. Número de participaciones de {pais} al mundial: {participaciones(pais)}")
    elif opcion == 4:
        print(f"4. Número de copas mundiales jugadas hasta la fecha: {copas_mundiales_jugadas()}")
    elif opcion == 5:
        print(f"5. Número de asistentes a las copas mundiales: {asistentes_totales()}")
    elif opcion == 6:
        print(f"6. Número de finales disputadas por penales: {finales_penales()}")
    elif opcion == 7:
        print(f"7. Número de goles a favor de los equipos en los mundiales: {goles_a_favor(pais)}")
    elif opcion == 8:
        print(f"8. Número de goles en contra de los equipos en los mundiales: {goles_en_contra(pais)}")
    elif opcion == 9:
        print(f"9. Diferencia de goles en todas sus presentaciones: {diferencia_de_goles(pais)}")
    elif opcion == 10:
        print(f"10. Promedio de goles de {pais} en mundiales: {promedio_goles(pais)}")
    elif opcion == 11:
        equipo1 = input("Ingrese el nombre del primer equipo: ").capitalize()
        equipo2 = input("Ingrese el nombre del segundo equipo: ").capitalize()
        print(f"11. Se han enfrentado {enfrentamientos(equipo1, equipo2)} veces en los mundiales.")
    elif opcion == 12:
        print(f"12. El mundial con más penales fue el año {mundial_con_mas_penales()}.")
    elif opcion == 13:
        print(f"13. El mundial con mayor número de goles fue el año {mundial_con_mas_goles()}.")
    if opcion == 14:
        print(f"14. Las mayores goleadas en los mundiales son:")
        for goleada in mayores_goleadas():
            partido = [int(goleada[0]), int(goleada[1]), int(goleada[2])]
            print(f"{goleada[0]} vs {goleada[1]} en el año {goleada[2]}, con una goleada de {max(partido[0], partido[1])} - {min(partido[0], partido[1])}.")
    print("¿Deseas ver información de otro tipo? (Sí/No)")
    opcion_otro = input().lower()
    if opcion_otro == 'si':
        main()
    else:
        print("Hasta luego.")

# Ejecutar el programa
if __name__ == "__main__":
    main()