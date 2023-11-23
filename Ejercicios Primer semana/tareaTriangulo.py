while True:
    altura = int(input("Ingrese la altura del triángulo (0 para salir): "))
    if altura == 0:
        break
    for i in range(1, altura + 1):
        espacios = altura - i
        asteriscos = 2 * i - 1
        linea = " " * espacios + "*" * asteriscos
        print(linea)
