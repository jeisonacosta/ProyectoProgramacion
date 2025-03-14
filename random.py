import random

def generar_numero_aleatorio(inicio, fin):
    """Genera un número entero aleatorio dentro de un rango dado."""
    return random.randint(inicio, fin)

def main():
    inicio = 1
    fin = 100
    numero_aleatorio = generar_numero_aleatorio(inicio, fin)
    print(f"Número aleatorio generado entre {inicio} y {fin}: {numero_aleatorio}")

if __name__ == "__main__":
    main()