class ConexionBaseDeDatos:
    def __init__(self, nombre_bd):
        """
        Constructor de la clase. Inicializa la conexión a la base de datos.

        :param nombre_bd: Nombre de la base de datos a la que se conectará.
        """
        self.nombre_bd = nombre_bd
        self.conexion = None
        self.conectar_a_bd()

    def conectar_a_bd(self):
        """
        Método que simula la conexión a la base de datos.
        """
        self.conexion = f"Conexión a {self.nombre_bd} establecida."
        print(self.conexion)

    def cerrar_conexion(self):
        """
        Método que simula el cierre de la conexión a la base de datos.
        """
        if self.conexion:
            print(f"Cerrando la conexión a {self.nombre_bd}...")
            self.conexion = None

    def __del__(self):
        """
        Destructor de la clase. Cierra la conexión a la base de datos.
        """
        self.cerrar_conexion()
        print(f"Conexión a {self.nombre_bd} cerrada correctamente.")


# Demostración de uso de la clase ConexionBaseDeDatos
if __name__ == "__main__":
    # Creación de una instancia de ConexionBaseDeDatos
    conexion_bd = ConexionBaseDeDatos("mi_base_de_datos")
    # El constructor (__init__) se llama automáticamente aquí y establece la conexión.

    # Realizar operaciones con la base de datos
    # ...

    # Al finalizar el programa o cuando el objeto conexion_bd sale del alcance,
    # el destructor (__del__) se llama automáticamente para cerrar la conexión.