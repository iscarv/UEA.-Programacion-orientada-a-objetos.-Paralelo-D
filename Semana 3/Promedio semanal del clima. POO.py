# Programación Orientada a objetos (POO)
# Determinar el promedio semanal del clima
# Clase base que representa el clima y contiene métodos comunes
class Clima:
    def __init__(self):
        self._temperaturas = []  # Atributo privado para almacenar las temperaturas (Encapsulamiento)

    def ingresar_temperaturas(self, dias):
        # Método para ingresar temperaturas diarias
        for i in range(dias):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self._temperaturas.append(temp)

    def calcular_promedio(self):
        # Método para calcular el promedio de las temperaturas almacenadas
        if not self._temperaturas:
            return 0.0
        total = sum(self._temperaturas)
        promedio = total / len(self._temperaturas)
        return promedio

    def get_temperaturas(self):
        # Método para obtener las temperaturas almacenadas
        return self._temperaturas

# Clase derivada para el clima semanal (Herencia)
class ClimaSemanal(Clima):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base (Herencia)

    def ingresar_temperaturas(self):
        # Método específico para ingresar temperaturas semanales (Polimorfismo)
        print("Ingresando temperaturas para la semana.")
        super().ingresar_temperaturas(7)  # Usa el método de la clase base con 7 días

    def calcular_promedio(self):
        # Método específico para calcular el promedio semanal (Polimorfismo)
        print("Calculando promedio semanal.")
        return super().calcular_promedio()  # Usa el método de la clase base

# Función principal para ejecutar el programa
def main():
    print("Programa para calcular el promedio semanal del clima.")
    clima_semanal = ClimaSemanal()  # Crea una instancia de ClimaSemanal
    clima_semanal.ingresar_temperaturas()  # Ingresa las temperaturas para la semana
    promedio_semanal = clima_semanal.calcular_promedio()  # Calcula el promedio semanal
    print(f"El promedio semanal de la temperatura es: {promedio_semanal:.2f}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()