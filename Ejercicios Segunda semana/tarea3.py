nombre_archivo = input("Ingrese el nombre del archivo: ")
try:
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            print(linea.upper(), end='')

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encuentra.")

except Exception as e:
    print(f"Ocurrió un error: {str(e)}")
