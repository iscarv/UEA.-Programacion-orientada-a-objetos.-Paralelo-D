class Libro:
    def __init__(self, isbn, titulo, autor, categoria):
        # Inicializamos el título y el autor como una tupla, lo que hace que sean inmutables.
        self.isbn = isbn
        self.datos = (titulo, autor)  # Tupla con el título y el autor
        self.categoria = categoria

    @property
    def titulo(self):
        # Devuelve el título del libro, que es el primer elemento de la tupla.
        return self.datos[0]

    @property
    def autor(self):
        # Devuelve el autor del libro, que es el segundo elemento de la tupla.
        return self.datos[1]

    def __str__(self):
        # Proporciona una representación en cadena del libro para facilitar su visualización.
        return f"ISBN: {self.isbn}, Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        # Inicializa un usuario con su nombre, ID único y una lista de libros prestados.
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        # Añade un libro a la lista de libros prestados del usuario.
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        # Elimina un libro de la lista de libros prestados del usuario, si está presente.
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        # Devuelve una lista de cadenas que representan los libros prestados por el usuario.
        return [str(libro) for libro in self.libros_prestados]


class Biblioteca:
    def __init__(self):
        # Inicializa la biblioteca con un diccionario de libros y un conjunto para los IDs de usuarios.
        self.libros = {}  # Diccionario de libros con ISBN como clave
        self.usuarios = {}  # Diccionario de usuarios con ID como clave
        self.ids_usuarios = set()  # Conjunto para gestionar los IDs de usuarios únicos

    def añadir_libro(self, libro):
        # Añade un libro a la biblioteca si su ISBN no existe ya en el diccionario.
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe.")

    def quitar_libro(self, isbn):
        # Elimina un libro de la biblioteca usando su ISBN.
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} ha sido eliminado.")
        else:
            print(f"No se encontró libro con ISBN {isbn}.")

    def registrar_usuario(self, nombre, id_usuario):
        # Registra un nuevo usuario si su ID no está ya en el conjunto de IDs de usuarios.
        if id_usuario not in self.ids_usuarios:
            nuevo_usuario = Usuario(nombre, id_usuario)
            self.usuarios[id_usuario] = nuevo_usuario
            self.ids_usuarios.add(id_usuario)  # Añade el ID al conjunto de IDs únicos
            print(f"Usuario '{nombre}' registrado con ID {id_usuario}.")
        else:
            print(f"El ID de usuario {id_usuario} ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        # Elimina un usuario del sistema usando su ID.
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.discard(id_usuario)  # Elimina el ID del conjunto de IDs únicos
            print(f"Usuario con ID {id_usuario} ha sido dado de baja.")
        else:
            print(f"No se encontró usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        # Presta un libro a un usuario si el libro y el usuario existen.
        libro = self.libros.get(isbn)
        usuario = self.usuarios.get(id_usuario)
        if libro and usuario:
            if libro not in usuario.libros_prestados:
                usuario.prestar_libro(libro)
                print(f"Libro '{libro.titulo}' prestado a usuario con ID {id_usuario}.")
            else:
                print(f"El libro '{libro.titulo}' ya está prestado a este usuario.")
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, id_usuario):
        # Devuelve un libro de un usuario si el libro está prestado por él.
        libro = self.libros.get(isbn)
        usuario = self.usuarios.get(id_usuario)
        if libro and usuario:
            if libro in usuario.libros_prestados:
                usuario.devolver_libro(libro)
                print(f"Libro '{libro.titulo}' devuelto por usuario con ID {id_usuario}.")
            else:
                print(f"El libro '{libro.titulo}' no está prestado a este usuario.")
        else:
            print("Libro o usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        # Busca libros en la biblioteca según el criterio (título, autor, categoría) y el valor proporcionado.
        resultados = []
        for libro in self.libros.values():
            if getattr(libro, criterio, None) == valor:
                resultados.append(str(libro))
        return resultados

    def listar_libros_prestados(self, id_usuario):
        # Lista todos los libros prestados a un usuario específico.
        usuario = self.usuarios.get(id_usuario)
        if usuario:
            return usuario.listar_libros_prestados()
        else:
            return "Usuario no encontrado."


# Función del menú que presenta las opciones al usuario
def menu():
    # Muestra el menú de opciones disponibles para el usuario.
    print("\nSistema de Biblioteca Digital")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados")
    print("9. Salir")


# Función principal que ejecuta el ciclo del sistema
def main():
    # Inicializa una instancia de la biblioteca.
    biblioteca = Biblioteca()

    while True:
        # Muestra el menú en cada iteración.
        menu()
        opcion = input("Seleccione una opción (1-9): ")

        if opcion == "1":
            # Añadir libro
            isbn = input("Ingrese ISBN: ")
            titulo = input("Ingrese título: ")
            autor = input("Ingrese autor: ")
            categoria = input("Ingrese categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)

        elif opcion == "2":
            # Quitar libro
            isbn = input("Ingrese ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            # Registrar usuario
            nombre = input("Ingrese nombre del usuario: ")
            id_usuario = input("Ingrese ID de usuario: ")
            biblioteca.registrar_usuario(nombre, id_usuario)

        elif opcion == "4":
            # Dar de baja usuario
            id_usuario = input("Ingrese ID de usuario a dar de baja: ")
            biblioteca.dar_de_baja_usuario(id_usuario)

        elif opcion == "5":
            # Prestar libro
            isbn = input("Ingrese ISBN del libro a prestar: ")
            id_usuario = input("Ingrese ID de usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == "6":
            # Devolver libro
            isbn = input("Ingrese ISBN del libro a devolver: ")
            id_usuario = input("Ingrese ID de usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == "7":
            # Buscar libro
            criterio = input("Ingrese criterio de búsqueda (titulo, autor, categoria): ")
            valor = input("Ingrese valor a buscar: ")
            resultados = biblioteca.buscar_libro(criterio, valor)
            if resultados:
                print("\nLibros encontrados:")
                for resultado in resultados:
                    print(resultado)
            else:
                print("No se encontraron libros con ese criterio.")

        elif opcion == "8":
            # Listar libros prestados
            id_usuario = input("Ingrese ID de usuario: ")
            libros_prestados = biblioteca.listar_libros_prestados(id_usuario)
            if isinstance(libros_prestados, list):
                print("\nLibros prestados:")
                for libro in libros_prestados:
                    print(libro)
            else:
                print(libros_prestados)

        elif opcion == "9":
            # Salir del sistema
            print("Saliendo del sistema...")
            break

        else:
            # Opción no válida
            print("Opción no válida, por favor intente de nuevo.")


# Ejecuta la función principal si este archivo es ejecutado directamente
if __name__ == "__main__":
    main()
