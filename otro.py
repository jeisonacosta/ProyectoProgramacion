def calcular_imc(peso, altura):
  """Calcula el Índice de Masa Corporal (IMC)."""
  imc = peso / (altura ** 2)
  return imc

def clasificar_imc(imc):
  """Clasifica el IMC en categorías."""
  if imc < 18.5:
    return "Bajo peso"
  elif 18.5 <= imc < 25:
    return "Peso normal"
  elif 25 <= imc < 30:
    return "Sobrepeso"
  else:
    return "Obesidad"

def main():
  """Función principal del programa."""
  try:
    peso = float(input("Ingrese su peso en toneladas: "))
    altura = float(input("Ingrese su altura en centimetros: "))

    imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)

    print(f"Su IMC es: {imc:.2f}")
    print(f"Clasificación: {clasificacion}")

  except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
  main()