import random

# Paso 1: Generar una lista principal de 50 números enteros en orden aleatorio
lista_enteros = []
for contador in range(0, 50):
    numero = random.randint(0, 200)
    lista_enteros.append(numero)
print("Lista original:", lista_enteros)

# Paso 2: Obtener el número mayor de la lista principal
numero_mayor = max(lista_enteros)
print("Numero mayor de la lista: ", numero_mayor)

# Paso 3: Obtener la cantidad de dígitos del número mayor
cantidad_digitos = len(str(numero_mayor))
print("Cantidad de dígitos del numero mayor: ", cantidad_digitos)

# Paso 4: Generar una lista de listas auxiliar para los dígitos desde el 0 al 9
lista_auxiliar = []
for i in range(10):
    lista_auxiliar.append([])


# Paso 5: Recorrer la lista principal y agregar a la lista auxiliar de acuerdo al dígito de menor valor
for num in lista_enteros:
    # Obtener el dígito de menor valor
    digito_menor = num % 10
    lista_auxiliar[digito_menor].append(num)

# Paso 6: Devolver los números a la lista principal desde la lista del dígito 0 hasta el dígito 9
for sublist in lista_auxiliar:
    for num in sublist:
        lista_enteros.append(num)
print("Lista auxiliar: ", lista_auxiliar)
lista_enteros.sort()
print("Lista ordenada:", lista_enteros)
