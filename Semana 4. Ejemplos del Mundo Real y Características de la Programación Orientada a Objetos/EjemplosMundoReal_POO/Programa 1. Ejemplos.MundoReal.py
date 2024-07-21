class Libro:
    def __init__(self, titulo, autor, genero, precio):
        self.titulo = titulo        # Atributo: Título del libro
        self.autor = autor          # Atributo: Autor del libro
        self.genero = genero        # Atributo: Género del libro
        self.precio = precio        # Atributo: Precio del libro

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.genero}) - ${self.precio}"
# Comienza la clase TiendaLibros (Abstracción: Representación de una tienda de libros)
class TiendaLibros:
    def __init__(self, nombre):
        self.nombre = nombre        # Atributo: Nombre de la tienda
        self.catalogo = []          # Atributo: Lista de libros en el catálogo

    def agregar_libro(self, libro):
        self.catalogo.append(libro)  # Método: Agrega un libro al catálogo

    def mostrar_catalogo(self):
        print(f"Catalogo de libros en {self.nombre}:")
        for libro in self.catalogo:
         print(libro)  # Método: Muestra todos los libros en el catálogo

    def buscar_por_genero(self, genero):
            libros_genero = []
            for libro in self.catalogo:
                if libro.genero == genero:
                    libros_genero.append(libro)
            return libros_genero  # Método: Retorna una lista de libros por género
# Comienza la clase Persona (Abstracción: Representación de una persona que compra libros)
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre        # Atributo: Nombre de la persona

    def comprar_libro(self, libro, tienda):
        tienda.agregar_libro(libro)    # Método: Utiliza el método de la tienda para agregar un libro
        print(f"{self.nombre} ha comprado el libro: {libro}")   # Acción: Compra un libro
libro1 = Libro("Lluvia de Miel", "Adolfo Ortiz Rodríguez", "Poemas", 30)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 35)

tienda = TiendaLibros("Librería Erenis")
tienda.agregar_libro(libro1)
tienda.agregar_libro(libro2)

tienda.mostrar_catalogo()

persona1 = Persona("Alice")
persona1.comprar_libro(libro1, tienda)