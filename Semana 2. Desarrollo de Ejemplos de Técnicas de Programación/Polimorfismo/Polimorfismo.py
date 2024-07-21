#Programa de dibujo
class Figura:
    def dibujar(self):
        pass


class Circulo(Figura):
    def dibujar(self):
        print("Dibujando un círculo.")


class Rectangulo(Figura):
    def dibujar(self):
        print("Dibujando un rectángulo.")


class Triangulo(Figura):
    def dibujar(self):
        print("Dibujando un triángulo.")


# Función para dibujar cualquier figura
def dibujar_figura(figura):
    figura.dibujar()


# Creación de objetos de las clases Circulo, Rectangulo y Triangulo
circulo = Circulo()
rectangulo = Rectangulo()
triangulo = Triangulo()

# Llamadas a la función dibujar_figura con diferentes objetos
dibujar_figura(circulo)
dibujar_figura(rectangulo)
dibujar_figura(triangulo)