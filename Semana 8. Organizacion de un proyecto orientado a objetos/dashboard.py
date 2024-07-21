#Adaptación de Proyecto de Programación Orientada a Objetos
import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)
# Se organizan los trabajos de acuerdo a su nombre y extención para poder ingresar a las carpetas
    opciones = {
        '1': 'Semana 2. Desarrollo de Ejemplos de Tecnicas de Programacion/Abstraccion/abstraccion.py',
        '2': 'Semana 2. Desarrollo de Ejemplos de Tecnicas de Programacion/Encapsulacion/encapsulacion.py',
        '3': 'Semana 2. Desarrollo de Ejemplos de Tecnicas de Programacion/Herencia/herencia.py',
        '4': 'Semana 2. Desarrollo de Ejemplos de Tecnicas de Programacion/Polimorfismo/polimorfismo.py',
        '5': 'Semana 3/Promedio semanal del clima. POO.py',
        '6': 'Semana 3/Promedio semanal del clima. Programacion Tradicional.py',
        '7': 'Semana 4. Ejemplos del Mundo Real y Características de la Programación Orientada a Objetos/EjemplosMundoReal_POO/Programa 1. Ejemplos.MundoReal.py',
        '8': 'Semana 4. Ejemplos del Mundo Real y Características de la Programacion Orientada a Objetos/EjemplosMundoReal_POO/Programa 2. Ejemplos.MundoReal.py',
        '9': 'Semana 5. (Tipos de datos, Identificadores)/Tipos de datos, Identificadores.py',
        '10': 'Semana 6. Clases, objetos, herencia, encapsulamiento y polimorfismo/(Semana 06). Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '11': 'Semana 7. Constructores y Destructores/Constructores y Destructores.py',
        '12': 'Semana 8. Organizacion de un proyecto orientado a objetos/dashboard.py'
        # Se agregaron las rutas de los scripts
    }

    while True:
        print("\nMenu Principal- Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
