#Martín Josué Andrade Salazar
# Función para escalar una imagen
def escalar_imagen(imagen, factor):
    filas = len(imagen)
    columnas = len(imagen[0])
    imagen_escalada = []

    for fila in imagen:
        for _ in range(factor):
            nueva_fila = ''.join([caracter * factor for caracter in fila])
            imagen_escalada.append(nueva_fila)

    return imagen_escalada

# Leer la cantidad de veces que se escalará la imagen
n = 3

# Leer la imagen original línea por línea
imagen_original = []
for _ in range(n):
    linea = input("Ingresa las letras (en minusculas): ").lower()

    imagen_original.append(linea)

# Escalar la imagen
imagen_escalada = escalar_imagen(imagen_original, n)

# Imprimir la imagen escalada
for fila in imagen_escalada:
    print(fila)
