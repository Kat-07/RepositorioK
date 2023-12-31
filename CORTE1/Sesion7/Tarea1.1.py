def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def es_numero_perfecto(numero):
    divisores = encontrar_divisores(numero)
    suma_divisores = sum(divisores) - numero
    if suma_divisores == numero:
        return True
    else:
        return False

def encontrar_numeros_perfectos(cantidad):
    numeros_perfectos = []
    i = 1
    while len(numeros_perfectos) < cantidad:
        if es_numero_perfecto(i):
            numeros_perfectos.append(i)
        i += 1
    return numeros_perfectos

numero = int(input("Ingrese un número: "))
divisores = encontrar_divisores(numero)
print(f"Los divisores de {numero} son: {divisores}")

cantidad_numeros_perfectos = int(input("Ingrese la cantidad de números perfectos a encontrar: "))

numeros_perfectos = encontrar_numeros_perfectos(cantidad_numeros_perfectos)
print(f"Los {cantidad_numeros_perfectos} primeros números perfectos son: {numeros_perfectos}")