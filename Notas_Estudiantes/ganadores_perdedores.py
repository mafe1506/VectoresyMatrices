import random

def generar_notas():
    return [round(random.uniform(0, 5), 2) for _ in range(30)]

def contar_ganadores_perdedores(notas):
    ganaron = sum(1 for nota in notas if nota > 3.0)
    perdieron = len(notas) - ganaron
    print(f"Ganaron: {ganaron} estudiantes")
    print(f"Perdieron: {perdieron} estudiantes")


if __name__ == "__main__":
    notas = generar_notas()
    print("Notas:", notas)
    contar_ganadores_perdedores(notas)
