arreglo = [3, 41, 12, 9, 74, 15]
for iterval in arreglo:
    mayor = max(arreglo[:arreglo.index(iterval) + 1])
    print("Número del arrelgo:", iterval, ", Mayor:", mayor)
print('El número mayor:', max(arreglo))