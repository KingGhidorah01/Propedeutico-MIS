class Estudiante:
    def __init__(self, codigo, nombre, edad, genero, calificacion):
        self._codigo = codigo
        self._nombre = nombre
        self._edad = edad
        self._genero = genero
        self._calificacion = calificacion

    # Métodos getter para acceder a los atributos privados
    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    def get_genero(self):
        return self._genero

    def get_calificacion(self):
        return self._calificacion

    # Métodos setter para modificar los atributos privados
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_edad(self, nueva_edad):
        self._edad = nueva_edad

    def set_genero(self, nuevo_genero):
        self._genero = nuevo_genero

    def set_calificacion(self, nueva_calificacion):
        self._calificacion = nueva_calificacion


class MenuEstudiantes:
    def __init__(self):
        self.lista_estudiantes = []

    def agregar_estudiante(self):
        codigo = input("Ingrese el código del estudiante: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        genero = input("Ingrese el género del estudiante: ")
        calificacion = float(input("Ingrese la calificación del estudiante: "))

        estudiante = Estudiante(codigo, nombre, edad, genero, calificacion)
        self.lista_estudiantes.append(estudiante)
        print("Estudiante agregado con éxito.")

    def eliminar_estudiante(self):
        codigo = input("Ingrese el código del estudiante a eliminar: ")
        for estudiante in self.lista_estudiantes:
            if estudiante.get_codigo() == codigo:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminado con éxito.")
                return
        print("No se encontró un estudiante con ese código.")

    def modificar_estudiante(self):
        codigo = input("Ingrese el código del estudiante a modificar: ")
        for estudiante in self.lista_estudiantes:
            if estudiante.get_codigo() == codigo:
                print("Datos actuales del estudiante:")
                print(f"Código: {estudiante.get_codigo()}")
                print(f"Nombre: {estudiante.get_nombre()}")
                print(f"Edad: {estudiante.get_edad()}")
                print(f"Género: {estudiante.get_genero()}")
                print(f"Calificación: {estudiante.get_calificacion()}")

                nuevo_nombre = input("Nuevo nombre: ")
                nueva_edad = int(input("Nueva edad: "))
                nuevo_genero = input("Nuevo género: ")
                nueva_calificacion = float(input("Nueva calificación: "))

                estudiante.set_nombre(nuevo_nombre)
                estudiante.set_edad(nueva_edad)
                estudiante.set_genero(nuevo_genero)
                estudiante.set_calificacion(nueva_calificacion)

                print("Estudiante modificado con éxito.")
                return
        print("No se encontró un estudiante con ese código.")

    def mostrar_lista_estudiantes(self):
        print("Lista de Estudiantes:")
        for estudiante in self.lista_estudiantes:
            print(f"Código: {estudiante.get_codigo()}, Nombre: {estudiante.get_nombre()}, Edad: {estudiante.get_edad()}, Género: {estudiante.get_genero()}, Calificación: {estudiante.get_calificacion()}")

    def ordenar_lista_estudiantes(self):
        sub_menu_orden = input("¿Ordenar de menor a mayor (m) o de mayor a menor (M)? ")
        reverse_order = sub_menu_orden.lower() == 'm'

        self.lista_estudiantes.sort(key=lambda x: x.get_calificacion(), reverse=reverse_order)
        print("Lista de estudiantes ordenada con éxito.")


if __name__ == "__main__":
    menu = MenuEstudiantes()

    while True:
        print("\nMenú:")
        print("1. Agregar Estudiante")
        print("2. Eliminar Estudiante")
        print("3. Modificar Estudiante")
        print("4. Mostrar Lista de Estudiantes")
        print("5. Ordenar Lista de Estudiantes")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            menu.agregar_estudiante()
        elif opcion == '2':
            menu.eliminar_estudiante()
        elif opcion == '3':
            menu.modificar_estudiante()
        elif opcion == '4':
            menu.mostrar_lista_estudiantes()
        elif opcion == '5':
            menu.ordenar_lista_estudiantes()
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 6.")
