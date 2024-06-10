#Gestión de vehículos
class Vehiculo:
    def __init__(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def arrancar(self):
        print("El vehículo ha arrancado.")


class Coche(Vehiculo):
    def __init__(self, velocidad_maxima, marca):
        super().__init__(velocidad_maxima)
        self.marca = marca

    def conducir(self):
        print(f"Conduciendo el coche de marca {self.marca}.")


class Bicicleta(Vehiculo):
    def __init__(self, velocidad_maxima, tipo):
        super().__init__(velocidad_maxima)
        self.tipo = tipo

    def pedalear(self):
        print(f"Pedalear en la bicicleta de tipo {self.tipo}.")


# Creación de objetos de las clases Coche y Bicicleta
coche = Coche(300, "Toyota")
bicicleta = Bicicleta(40, "Montaña")

# Llamadas a métodos específicos de cada clase
coche.arrancar()
coche.conducir()

bicicleta.arrancar()
bicicleta.pedalear()