class Plato:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre        # Atributo: Nombre del plato
        self.descripcion = descripcion  # Atributo: Descripción del plato
        self.precio = precio        # Atributo: Precio del plato

    def __str__(self):
        return f"{self.nombre}: {self.descripcion} - ${self.precio}"

# Comienza la clase Restaurante (Abstraccion: Representación de un restaurante)
class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre        # Atributo: Nombre del restaurante
        self.menu = {}              # Atributo: Diccionario para el menú de platos

    def agregar_plato(self, plato):
        self.menu[plato.nombre] = plato  # Método: Agrega un plato al menú

    def mostrar_menu(self):
        print(f"Menú de {self.nombre}:")
        for plato in self.menu.values():
            print(plato)            # Método: Muestra todos los platos en el menú

    def buscar_plato(self, nombre_plato):
        return self.menu.get(nombre_plato, None)   # Método: Busca un plato por nombre en el menú

# Comienza la clase Pedido (Abstraccion: Representación de un pedido realizado por un cliente)
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente      # Atributo: Cliente que realiza el pedido
        self.platos = []            # Atributo: Lista de platos en el pedido

    def agregar_plato(self, plato, restaurante):
        if plato in restaurante.menu.values():
            self.platos.append(plato)   # Método: Agrega un plato al pedido si está en el menú
            print(f"{self.cliente.nombre} ha añadido '{plato.nombre}' al pedido")
        else:
            print(f"El plato '{plato.nombre}' no está en el menú del restaurante")

    def mostrar_pedido(self):
        if self.platos:
            print(f"Pedido de {self.cliente.nombre}:")
            for plato in self.platos:
                print(plato)        # Método: Muestra todos los platos en el pedido del cliente
        else:
            print(f"No hay platos en el pedido de {self.cliente.nombre}")

# Comienza la clase Cliente (Abstraccion: Representación de un cliente del restaurante)
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre        # Atributo: Nombre del cliente


plato1 = Plato("Hamburguesa", "Carne de res con lechuga, tomate y queso", 10)
plato2 = Plato("Pizza Margarita", "Mozzarella, salsa de tomate y albahaca fresca", 12)
plato3 = Plato("Ensalada César", "Lechuga romana, pollo a la parrilla y aderezo César", 8)

restaurante = Restaurante("Las delicias de Mamá")
restaurante.agregar_plato(plato1)
restaurante.agregar_plato(plato2)
restaurante.agregar_plato(plato3)

restaurante.mostrar_menu()

cliente1 = Cliente("Alice")
pedido_cliente1 = Pedido(cliente1)

pedido_cliente1.agregar_plato(plato1, restaurante)
pedido_cliente1.agregar_plato(plato3, restaurante)

pedido_cliente1.mostrar_pedido()