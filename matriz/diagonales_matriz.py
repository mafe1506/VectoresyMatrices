import random

def crear_matriz(n):
    return [[random.randint(1, 99) for _ in range(n)] for _ in range(n)]

def diagonal_principal(matriz):
    return [matriz[i][i] for i in range(len(matriz))]

def diagonal_secundaria(matriz):
    n = len(matriz)
    return [matriz[i][n - 1 - i] for i in range(n)]


if __name__ == "__main__":
    N = int(input("Ingrese el tamaño de la matriz (N): "))
    matriz = crear_matriz(N)

    print("\nMatriz generada:")
    for fila in matriz:
        print(fila)

    print("\nDiagonal principal:", diagonal_principal(matriz))
    print("Diagonal secundaria:", diagonal_secundaria(matriz))
