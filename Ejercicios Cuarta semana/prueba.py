import random
from matplotlib import pyplot as plt
import speech_recognition as sr
from collections import Counter

# Configuración del reconocimiento de voz
recognizer = sr.Recognizer()

def obtener_input_por_voz(mensaje):
    print(mensaje)
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Habla ahora...")
        audio = recognizer.listen(source)

    try:
        input_voz = recognizer.recognize_google(audio)
        return input_voz
    except sr.UnknownValueError:
        print("No se pudo entender. Intenta nuevamente.")
        return obtener_input_por_voz(mensaje)
    except sr.RequestError as e:
        print(f"Error en la solicitud de reconocimiento de voz: {e}")
        return obtener_input_por_voz(mensaje)

# Obtener 20 nombres por voz
nombres = []
for _ in range(1):
    nombre = obtener_input_por_voz("Por favor, dicta un nombre:")
    nombres.append(nombre)

# Obtener 20 apellidos paternos por voz
apellidos_paternos = []
for _ in range(1):
    apellido_paterno = obtener_input_por_voz("Por favor, dicta un apellido paterno:")
    apellidos_paternos.append(apellido_paterno)

# Obtener 20 apellidos maternos por voz
apellidos_maternos = []
for _ in range(1):
    apellido_materno = obtener_input_por_voz("Por favor, dicta un apellido materno:")
    apellidos_maternos.append(apellido_materno)

localidades = ["Ameca", "Tala", "Guadalajara", "Zapoapan", "Ahualulco"]

# Generar 10000 datos sintéticos
datos_sinteticos = []
for i in range(1, 10001):
    nombre = random.choice(nombres)
    apellido_paterno = random.choice(apellidos_paternos)
    apellido_materno = random.choice(apellidos_maternos)
    edad = random.randint(0, 100)
    peso = round(random.uniform(1, 200), 2)
    localidad = random.choice(localidades)

    tupla = (i, nombre, apellido_paterno, apellido_materno, edad, peso, localidad)
    datos_sinteticos.append(tupla)

# Contar hermanos y homónimos
hermanos_counter = Counter((dato[2], dato[3]) for dato in datos_sinteticos)
hermanos = sum(count - 1 for count in hermanos_counter.values() if count > 1)

homonimos_counter = Counter((dato[1], dato[2], dato[3]) for dato in datos_sinteticos)
homonimos = sum(count - 1 for count in homonimos_counter.values() if count > 1)

# Imprimir resultados
print(f"Total de hermanos: {hermanos}")
print(f"Total de homónimos: {homonimos}")

# Histograma de edades por localidad
for localidad in set(dato[6] for dato in datos_sinteticos):
    edades_localidad = [dato[4] for dato in datos_sinteticos if dato[6] == localidad]
    plt.hist(edades_localidad, bins=20, edgecolor='black')
    plt.title(f'Histograma de Edades en {localidad}')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    plt.show()

# Histograma de pesos por localidad
for localidad in set(dato[6] for dato in datos_sinteticos):
    pesos_localidad = [dato[5] for dato in datos_sinteticos if dato[6] == localidad]
    plt.hist(pesos_localidad, bins=20, edgecolor='black')
    plt.title(f'Histograma de Pesos en {localidad}')
    plt.xlabel('Peso')
    plt.ylabel('Frecuencia')
    plt.show()

# Contar el total de personas por localidad
total_por_localidad = Counter(dato[6] for dato in datos_sinteticos)

# Pregunta 1: Localidad con mayor porcentaje de menores (<18)
porcentaje_menores_por_localidad = {}
for localidad in localidades:
    total_personas_localidad = total_por_localidad[localidad]
    if total_personas_localidad > 0:
        porcentaje_menores = (sum(1 for dato in datos_sinteticos if dato[4] < 18 and dato[6] == localidad) / total_personas_localidad) * 100
        porcentaje_menores_por_localidad[localidad] = porcentaje_menores

localidad_mayor_porcentaje_menores = max(porcentaje_menores_por_localidad,
                                          key=porcentaje_menores_por_localidad.get)
print(f"La localidad con mayor porcentaje de menores (<18) es: {localidad_mayor_porcentaje_menores}")

# Pregunta 2: Localidad con mayor porcentaje de adultos (18-60)
porcentaje_adultos_por_localidad = {}
for localidad in localidades:
    total_personas_localidad = total_por_localidad[localidad]
    if total_personas_localidad > 0:
        porcentaje_adultos = (sum(1 for dato in datos_sinteticos if 18 <= dato[4] <= 60 and dato[6] == localidad) / total_personas_localidad) * 100
        porcentaje_adultos_por_localidad[localidad] = porcentaje_adultos

localidad_mayor_porcentaje_adultos = max(porcentaje_adultos_por_localidad,
                                          key=porcentaje_adultos_por_localidad.get)
print(f"La localidad con mayor porcentaje de adultos (18-60) es: {localidad_mayor_porcentaje_adultos}")

# Pregunta 3: Localidad con mayor porcentaje de adultos mayores (>60)
porcentaje_adultos_mayores_por_localidad = {}
for localidad in localidades:
    total_personas_localidad = total_por_localidad[localidad]
    if total_personas_localidad > 0:
        porcentaje_adultos_mayores = (sum(1 for dato in datos_sinteticos if dato[4] > 60 and dato[6] == localidad) / total_personas_localidad) * 100
        porcentaje_adultos_mayores_por_localidad[localidad] = porcentaje_adultos_mayores

localidad_mayor_porcentaje_adultos_mayores = max(porcentaje_adultos_mayores_por_localidad,
                                                  key=porcentaje_adultos_mayores_por_localidad.get)
print(f"La localidad con mayor porcentaje de adultos mayores (>60) es: {localidad_mayor_porcentaje_adultos_mayores}")

# Pregunta 4: En qué localidad son más pesados los adultos (18-60)
peso_promedio_adultos_por_localidad = {}
for localidad in localidades:
    peso_total_adultos = sum(dato[5] for dato in datos_sinteticos if 18 <= dato[4] <= 60 and dato[6] == localidad)
    total_adultos = sum(1 for dato in datos_sinteticos if 18 <= dato[4] <= 60 and dato[6] == localidad)
    if total_adultos > 0:
        peso_promedio_adultos = peso_total_adultos / total_adultos
        peso_promedio_adultos_por_localidad[localidad] = peso_promedio_adultos

localidad_mas_pesados_adultos = max(peso_promedio_adultos_por_localidad,
                                    key=peso_promedio_adultos_por_localidad.get)
print(f"La localidad donde los adultos (18-60) son más pesados es: {localidad_mas_pesados_adultos}")

# Pregunta 5: Localidad más longeva
edad_promedio_por_localidad = {}
for localidad in localidades:
    edad_total_localidad = sum(dato[4] for dato in datos_sinteticos if dato[6] == localidad)
    total_personas_localidad = total_por_localidad[localidad]
    if total_personas_localidad > 0:
        edad_promedio_localidad = edad_total_localidad / total_personas_localidad
        edad_promedio_por_localidad[localidad] = edad_promedio_localidad

localidad_mas_longeva = max(edad_promedio_por_localidad, key=edad_promedio_por_localidad.get)
print(f"La localidad más longeva es: {localidad_mas_longeva}")
