import speech_recognition as sr
from faker import Faker
import random


# Función para obtener un nombre mediante entrada de voz
def obtener_nombre_por_voz():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Dicta el nombre:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        nombre = recognizer.recognize_google(audio, language="es-ES")
        return nombre
    except sr.UnknownValueError:
        print("No se pudo entender la voz.")
        return None
    except sr.RequestError as e:
        print(f"Error al obtener la entrada de voz: {e}")
        return None


# Crear una instancia de Faker
fake = Faker()

# Lista de localidades
localidades = ["Ameca", "Ciudad de México", "Guadalajara", "Monterrey", "Querétaro"]

# Generar 10,000 tuplas de datos sintéticos
datos_sinteticos = []
for _ in range(2):
    id_autoincrementable = _ + 1
    nombre = obtener_nombre_por_voz()  # Obtener el nombre mediante entrada de voz
    apellido_paterno = fake.last_name()
    apellido_materno = fake.last_name()
    edad = random.randint(0, 100)
    peso = round(random.uniform(1, 200), 1)
    localidad = random.choice(localidades)

    tupla = (id_autoincrementable, nombre, apellido_paterno, apellido_materno, edad, peso, localidad)
    datos_sinteticos.append(tupla)

# Imprimir algunos datos de ejemplo
for i in range(2):
    print(datos_sinteticos[i])