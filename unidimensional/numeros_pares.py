import random

def generar_arreglo():
    return [random.randint(100, 999) for _ in range(100)]

def obtener_pares(arreglo):
    return [num for num in arreglo if num % 2 == 0]


if __name__ == "__main__":
    arreglo = generar_arreglo()
    pares = obtener_pares(arreglo)
    print("Arreglo original:", arreglo)
    print("Números pares:", pares)
