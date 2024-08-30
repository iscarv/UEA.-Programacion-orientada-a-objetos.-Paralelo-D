import pickle


class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        # Inicializa los atributos del producto
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_producto_id(self):
        # Obtiene el ID del producto
        return self.producto_id

    def get_nombre(self):
        # Obtiene el nombre del producto
        return self.nombre

    def get_cantidad(self):
        # Obtiene la cantidad del producto
        return self.cantidad

    def get_precio(self):
        # Obtiene el precio del producto
        return self.precio

    def set_cantidad(self, cantidad):
        # Establece la cantidad del producto
        self.cantidad = cantidad

    def set_precio(self, precio):
        # Establece el precio del producto
        self.precio = precio

    def __str__(self):
        # Devuelve una representación en cadena del producto
        return f"ID: {self.producto_id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        # Inicializa un diccionario para almacenar los productos
        self.productos = {}

    def agregar_producto(self, producto):
        # Agrega un nuevo producto al inventario
        if producto.get_producto_id() in self.productos:
            print(f"El producto con ID {producto.get_producto_id()} ya existe.")
        else:
            self.productos[producto.get_producto_id()] = producto
            print(f"Producto {producto.get_nombre()} agregado.")

    def eliminar_producto(self, producto_id):
        # Elimina un producto del inventario por su ID
        if producto_id in self.productos:
            del self.productos[producto_id]
            print(f"Producto con ID {producto_id} eliminado.")
        else:
            print(f"No se encontró el producto con ID {producto_id}.")

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        # Actualiza la cantidad o el precio de un producto por su ID
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print(f"Producto con ID {producto_id} actualizado.")
        else:
            print(f"No se encontró el producto con ID {producto_id}.")

    def buscar_producto_por_nombre(self, nombre):
        # Busca productos por nombre (parcial o completo)
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print(f"No se encontró ningún producto con el nombre {nombre}.")

    def mostrar_todos_los_productos(self):
        # Muestra todos los productos en el inventario
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, archivo):
        # Guarda el inventario en un archivo usando pickle
        with open(archivo, 'wb') as f:
            pickle.dump(self.productos, f)
            print("Inventario guardado en archivo.")

    def cargar_inventario(self, archivo):
        # Carga el inventario desde un archivo usando pickle
        try:
            with open(archivo, 'rb') as f:
                self.productos = pickle.load(f)
                print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("No se encontró el archivo para cargar el inventario.")


def menu():
    inventario = Inventario()  # Crea una instancia de Inventario
    while True:
        # Muestra el menú de opciones
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Agrega un nuevo producto
            producto_id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(producto_id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            # Elimina un producto
            producto_id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(producto_id)

        elif opcion == '3':
            # Actualiza un producto
            producto_id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(producto_id, cantidad, precio)

        elif opcion == '4':
            # Busca un producto por nombre
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            # Muestra todos los productos
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            # Guarda el inventario en un archivo
            archivo = input("Ingrese nombre del archivo para guardar el inventario: ")
            inventario.guardar_inventario(archivo)

        elif opcion == '7':
            # Carga el inventario desde un archivo
            archivo = input("Ingrese nombre del archivo para cargar el inventario: ")
            inventario.cargar_inventario(archivo)

        elif opcion == '8':
            # Sale del programa
            print("Saliendo...")
            break

        else:
            # Maneja una opción no válida
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()  # Ejecuta el menú al iniciar el programa