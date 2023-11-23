#Martín Josué Andrade Salazar
# Función para calcular el volumen de una gelatina
def calcular_volumen(largo, ancho, alto):
    return largo * ancho * alto


# Número de casos a analizar
num_casos = int(input("Numero de casos a analizar: "))

for caso in range(num_casos):
    # Número de niños en este caso
    num_ninos = int(input("Numero de niños: "))
    nombres = []  # Lista de nombres de los niños
    volumenes = []  # Lista de volúmenes de gelatina

    # Recopilación de datos de los niños
    for i in range(num_ninos):
        datos = input("Ingrese el nombre largo ancho alto (separado por espacios): ").split()
        nombres.append(datos[0])
        volumen = calcular_volumen(int(datos[1]), int(datos[2]), int(datos[3]))
        volumenes.append(volumen)

    # Calcular el volumen total de gelatina
    volumen_total = sum(volumenes)

    # Calcular el volumen esperado para cada niño si nadie hubiera robado gelatina
    volumen_esperado = volumen_total / num_ninos

    # Encontrar al niño que tiene más gelatina de la esperada y al que tiene menos
    nino_perdedor = None
    nino_ganador = None

    for i in range(num_ninos):
        if volumenes[i] > volumen_esperado:
            nino_ganador = nombres[i]
        elif volumenes[i] < volumen_esperado:
            nino_perdedor = nombres[i]

    if nino_perdedor is not None and nino_ganador is not None:
        print(f"Le han quitado gelatina a {nino_perdedor} y pasado a {nino_ganador}.")
    else:
        print("No hubo broma")
