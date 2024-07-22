#Gestión de empleados
class Empleado:
    def __init__(self, nombre, apellido, edad, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Salario: {self.salario}")


# Creación de un objeto de la clase Empleado
empleado1 = Empleado("Luis", "Cabrera", 40, 2500)

# Llamada al método para mostrar la información del empleado
empleado1.mostrar_informacion()