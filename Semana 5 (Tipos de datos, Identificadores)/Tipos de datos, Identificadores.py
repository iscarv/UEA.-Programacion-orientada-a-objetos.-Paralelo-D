# Programa para gestionar un registro de estudiantes.
# Funcionalidad: Permite agregar, eliminar y mostrar estudiantes en un registro.

# Lista para almacenar el registro de estudiantes
estudiantes = []


def agregar_estudiante(id_estudiante, nombre, edad, nota, esta_inscrito):
    """
    Función para agregar un estudiante al registro.

    Args:
    id_estudiante (int): ID del estudiante.
    nombre (str): Nombre del estudiante.
    edad (int): Edad del estudiante.
    nota (float): Nota del estudiante.
    esta_inscrito (bool): Estado de inscripción del estudiante.

    Returns:
    None
    """
    estudiante = {
        "id_estudiante": id_estudiante,
        "nombre": nombre,
        "edad": edad,
        "nota": nota,
        "esta_inscrito": esta_inscrito
    }
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} agregado con éxito.")


def eliminar_estudiante(id_estudiante):
    """
    Función para eliminar un estudiante del registro por su ID.

    Args:
    id_estudiante (int): ID del estudiante.

    Returns:
    None
    """
    global estudiantes
    estudiantes = [estudiante for estudiante in estudiantes if estudiante["id_estudiante"] != id_estudiante]
    print(f"Estudiante con ID {id_estudiante} eliminado con éxito.")


def mostrar_estudiantes():
    """
    Función para mostrar todos los estudiantes en el registro.

    Returns:
    None
    """
    for estudiante in estudiantes:
        print(
            f"ID: {estudiante['id_estudiante']}, Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Nota: {estudiante['nota']}, Inscrito: {estudiante['esta_inscrito']}")


# Ejemplos de uso del programa
agregar_estudiante(1, "Luna Castillo", 20, 8.5, True)
agregar_estudiante(2, "Andreina Ferrer", 24, 9.0, True)
agregar_estudiante(3, "Alfredo Miranda", 18, 7.8, False)

print("\nRegistro de estudiantes:")
mostrar_estudiantes()

eliminar_estudiante(2)

print("\nRegistro de estudiantes después de eliminar:")
mostrar_estudiantes()
