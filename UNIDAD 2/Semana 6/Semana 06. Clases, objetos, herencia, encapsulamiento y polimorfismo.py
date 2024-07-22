# Definición de la clase base FiguraGeometrica
class FiguraGeometrica:
    def __init__(self, color):
        """
        Constructor de la clase FiguraGeometrica.

        Args:
        - color (str): El color de la figura.
        """
        self.__color = color  # Encapsulacion del color

    def obtener_color(self):
        """
        Método para obtener el color de la figura.

        Returns:
        - str: El color de la figura.
        """
        return self.__color


# Definición de la clase derivada Rectangulo, que hereda de FiguraGeometrica
class Rectangulo(FiguraGeometrica):  # <<--- HERENCIA
    def __init__(self, color, ancho, altura):
        """
        Constructor de la clase Rectangulo, que hereda de FiguraGeometrica.

        Args:
        - color (str): El color del rectángulo.
        - ancho (float): El ancho del rectángulo.
        - altura (float): La altura del rectángulo.
        """
        super().__init__(color)  # <<--- LLAMADA AL CONSTRUCTOR DE LA CLASE BASE (HERENCIA)
        self.__ancho = ancho  # Encapsulacion del ancho
        self.__altura = altura  # Encapsulacion de la altura

    def calcular_area(self):  # <<--- MÉTODO POLIMÓRFICO
        """
        Método para calcular el área del rectángulo.

        Returns:
        - float: El área del rectángulo.
        """
        return self.__ancho * self.__altura


# Definición de la clase derivada Circulo, que hereda de FiguraGeometrica
class Circulo(FiguraGeometrica):  # <<--- HERENCIA
    def __init__(self, color, radio):
        """
        Constructor de la clase Circulo, que hereda de FiguraGeometrica.

        Args:
        - color (str): El color del círculo.
        - radio (float): El radio del círculo.
        """
        super().__init__(color)  # <<--- LLAMADA AL CONSTRUCTOR DE LA CLASE BASE (HERENCIA)
        self.__radio = radio  # Encapsulacion del radio

    def calcular_area(self):  # <<--- MÉTODO POLIMÓRFICO
        """
        Método para calcular el área del círculo.

        Returns:
        - float: El área del círculo.
        """
        import math
        return math.pi * self.__radio ** 2


# Creación de instancias y demostración del programa
if __name__ == "__main__":
    # Creamos una instancia de Rectangulo y mostramos su color y área
    mi_rectangulo = Rectangulo("Rosado", 5, 10)
    print("Rectángulo:")
    print("Color:", mi_rectangulo.obtener_color())
    print("Área:", mi_rectangulo.calcular_area())  # <<--- POLIMORFISMO: LLAMADA AL MÉTODO ESPECÍFICO DE RECTANGULO

    # Creamos una instancia de Circulo y mostramos su color y área
    mi_circulo = Circulo("Morado", 8)
    print("\nCírculo:")
    print("Color:", mi_circulo.obtener_color())
    print("Área:", mi_circulo.calcular_area())  # <<--- POLIMORFISMO: LLAMADA AL MÉTODO ESPECÍFICO DE CIRCULO