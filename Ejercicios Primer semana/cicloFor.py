def es_primo(n):
  """
  Función que determina si un número es primo.

  Args:
    n: El número a evaluar.

  Returns:
    True si n es primo, False en caso contrario.
  """

  if n < 2:
    return False

  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False

  return True


def main():
  """
  Función principal del programa.
  """

  # Solicitamos al usuario que ingrese dos números separados por un espacio.
  numeros = input("Ingrese dos números separados por un espacio: ").split()

  # Convertimos los números ingresados a números enteros.
  n1 = int(numeros[0])
  n2 = int(numeros[1])

  # Inicializamos una lista para almacenar los números primos rellenos.
  primos = []

  # Recorremos los números entre n1 y n2.
  for i in range(n1, n2 + 1):
    # Si el número tiene 2 dígitos, lo evaluamos.
    if len(str(i)) == 2:
      # Si uno de los dígitos no es primo, no lo agregamos a la lista.
      if not es_primo(i // 10) or not es_primo(i % 10):
        continue
      primos.append(i)

  # Imprimimos la lista de números primos rellenos.
  print("Entre {} y {}, los números primos rellenos son:".format(n1, n2))
  for primo in primos:
    if primo is not None:
      print(primo, end=" ")
    else:
      print("-", end=" ")


if __name__ == "__main__":
  main()
