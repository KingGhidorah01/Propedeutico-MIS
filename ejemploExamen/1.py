def combinacion_optima(tela):
    # Definir los tamaños de corte
    tamanos_corte = [5, 4, 3]

    mejor_combinacion = None
    mejor_desperdicio = float('inf')  # Inicializar con un valor infinito para encontrar la mejor combinación

    # Iterar sobre todas las combinaciones posibles de cortes
    for corte1 in range(tela // tamanos_corte[0] + 1):
        for corte2 in range(tela // tamanos_corte[1] + 1):
            for corte3 in range(tela // tamanos_corte[2] + 1):
                longitud_total = corte1 * tamanos_corte[0] + corte2 * tamanos_corte[1] + corte3 * tamanos_corte[2]
                desperdicio = tela - longitud_total

                # Verificar si esta combinación es mejor que la actual mejor_combinacion
                if desperdicio < mejor_desperdicio:
                    mejor_combinacion = (corte1, corte2, corte3)
                    mejor_desperdicio = desperdicio

    # Imprimir la mejor combinación
    print(f'{mejor_combinacion[0]} cortes de {tamanos_corte[0]}m, {mejor_combinacion[1]} cortes de {tamanos_corte[1]}m, {mejor_combinacion[2]} cortes de {tamanos_corte[2]}m tiene un desperdicio de {mejor_desperdicio}m')

# Solicitar la longitud de la tela al usuario
tela = int(input("Ingrese la longitud de la tela en metros: "))
combinacion_optima(tela)
