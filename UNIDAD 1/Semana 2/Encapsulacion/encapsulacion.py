#Gestión de cuentas bancarias
class CuentaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print("Retiro exitoso.")
        else:
            print("Saldo insuficiente.")

    def obtener_saldo(self):
        return self.saldo


# Creación de un objeto de la clase CuentaBancaria
cuenta = CuentaBancaria()

# Depositar 1000 en la cuenta
cuenta.depositar(2000)

# Retirar 500 de la cuenta
cuenta.retirar(500)

# Obtener el saldo actual de la cuenta
print("Saldo actual:", cuenta.obtener_saldo())