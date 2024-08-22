# Tarea: Manipulación de archivos y manejo de excepciones

class Producto:
    # Constructor
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Inicializa los atributos del producto con los valores dados
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos Getters para obtener los valores de los atributos
    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos Setters para modificar los valores de los atributos
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Método para convertir el objeto Producto a una cadena de texto
    def __str__(self):
        return f'ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}'


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        # Inicializa la lista de productos y el nombre del archivo donde se guardará el inventario
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()  # Carga los productos desde el archivo al iniciar

    def cargar_inventario(self):
        # Carga los productos del archivo de texto al inventario
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    # Divide la línea en partes y crea un objeto Producto
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                    self.productos.append(producto)  # Añade el producto a la lista de productos
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            # Si el archivo no existe, lo crea y muestra un mensaje
            print(f"Archivo {self.archivo} no encontrado, se creará un nuevo archivo.")
            open(self.archivo, 'w').close()
        except PermissionError:
            # Si no se tienen permisos para leer el archivo, muestra un mensaje de error
            print(f"Permiso denegado para leer el archivo {self.archivo}.")
        except Exception as e:
            # Captura cualquier otro tipo de excepción y muestra un mensaje de error
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        # Guarda el estado actual del inventario en el archivo de texto
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    # Escribe cada producto en una línea del archivo
                    file.write(f'{producto.get_id_producto()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n')
            print("Inventario guardado exitosamente.")
        except PermissionError:
            # Si no se tienen permisos para escribir en el archivo, muestra un mensaje de error
            print(f"Permiso denegado para escribir en el archivo {self.archivo}.")
        except Exception as e:
            # Captura cualquier otro tipo de excepción y muestra un mensaje de error
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        # Añade un producto al inventario si el ID no existe
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                # Si el ID del producto ya existe, muestra un mensaje de error y no añade el producto
                print("Error: Ya existe un producto con este ID.")
                return
        self.productos.append(producto)  # Añade el producto a la lista
        self.guardar_inventario()  # Guarda el inventario en el archivo

    def eliminar_producto(self, id_producto):
        # Elimina un producto del inventario por su ID
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                self.productos.remove(p)  # Remueve el producto de la lista
                self.guardar_inventario()  # Guarda el inventario en el archivo
                return
        # Si no se encuentra el producto, muestra un mensaje de error
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        # Actualiza la cantidad y/o el precio de un producto por su ID
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)  # Actualiza la cantidad
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)  # Actualiza el precio
                self.guardar_inventario()  # Guarda el inventario en el archivo
                return
        # Si no se encuentra el producto, muestra un mensaje de error
        print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        # Busca productos en el inventario por nombre
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            print("Productos encontrados:")
            for p in productos_encontrados:
                print(p)  # Muestra cada producto encontrado
        else:
            print("No se encontraron productos con ese nombre.")  # Muestra un mensaje si no hay coincidencias

    def mostrar_todos_los_productos(self):
        # Muestra todos los productos del inventario
        if not self.productos:
            print("El inventario está vacío.")  # Mensaje si no hay productos
        else:
            for p in self.productos:
                print(p)  # Muestra cada producto


# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()  # Crea un objeto Inventario y carga los productos desde el archivo
    while True:
        # Muestra el menú principal al usuario
        print("\n--- Menú ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Opción para añadir un producto
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            # Opción para eliminar un producto
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            # Opción para actualizar un producto
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (dejar en blanco para no actualizar): ")
            nuevo_precio = input("Nuevo precio (dejar en blanco para no actualizar): ")

            # Si no se introduce un valor, el atributo no se actualiza
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            # Opción para buscar un producto por nombre
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            # Opción para mostrar todos los productos del inventario
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            # Opción para salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, por favor selecciona otra.")  # Mensaje de error para opciones inválidas


# Ejecutar el menú
if __name__ == "__main__":
    menu()  # Inicia el programa ejecutando el menú

