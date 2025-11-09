import random

def generar_notas():
    return [round(random.uniform(0, 5), 2) for _ in range(30)]

def promedio(notas):
    prom = round(sum(notas) / len(notas), 2)
    print(f"Promedio del grupo: {prom}")


if __name__ == "__main__":
    notas = generar_notas()
    print("Notas:", notas)
    promedio(notas)
