def simulador_ventanillas(cantidad_ventanillas, cantidad_clientes, tiempo_atencion):
    ventanillas = [0] * cantidad_ventanillas
    tiempo_actual = 0

    while cantidad_clientes > 0 or any(ventanilla != 0 for ventanilla in ventanillas):
        for i in range(len(ventanillas)):
            if ventanillas[i] == 0 and cantidad_clientes > 0:
                cliente_actual = cantidad_clientes
                cantidad_clientes -= 1
                ventanillas[i] = tiempo_atencion
                print(f"Cliente {cliente_actual} atendido en Ventanilla {i + 1} desde el minuto {tiempo_actual}")

        tiempo_actual += 1

        for i in range(len(ventanillas)):
            if ventanillas[i] > 0:
                ventanillas[i] -= 1
                if ventanillas[i] == 0:
                    print(f"Cliente {cantidad_clientes + i + 1} terminó de ser atendido en Ventanilla {i + 1} en el minuto {tiempo_actual}")

# Solicitar información al usuario
cantidad_ventanillas = int(input("Ingrese la cantidad de ventanillas disponibles: "))
cantidad_clientes = int(input("Ingrese la cantidad de clientes en fila: "))
tiempo_atencion = int(input("Ingrese la cantidad de minutos que tarda en atender cada ventanilla a un solo cliente: "))

# Llamar a la función simuladora
simulador_ventanillas(cantidad_ventanillas, cantidad_clientes, tiempo_atencion)
