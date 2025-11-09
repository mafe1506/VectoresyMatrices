import random

def generar_notas():
    return [round(random.uniform(0, 5), 2) for _ in range(30)]

def nota_max_min(notas):
    nota_max = max(notas)
    nota_min = min(notas)
    print(f"Nota más alta: {nota_max}")
    print(f"Nota más baja: {nota_min}")


if __name__ == "__main__":
    notas = generar_notas()
    print("Notas:", notas)
    nota_max_min(notas)
