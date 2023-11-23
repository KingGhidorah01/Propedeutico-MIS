total = 0
count = 0

while True:
    input_value = input("Ingresa un número: ")

    if input_value == "hecho":
        break  # Salir del bucle si se ingresa "hecho"

    try:
        number = float(input_value)
        total += number
        count += 1
    except ValueError:
        print("Entrada inválida")

if count > 0:
    average = total / count
    print(total, count, average)
else:
    print("No se ingresaron números válidos.")
