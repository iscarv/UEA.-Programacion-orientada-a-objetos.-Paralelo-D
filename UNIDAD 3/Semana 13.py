import tkinter as tk
from tkinter import ttk

# Funciones para manejar los eventos
def agregar_dato():
    dato = entrada.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada.delete(0, tk.END)

def limpiar_datos():
    lista_datos.delete(0, tk.END)
    entrada.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Datos")
ventana.configure(bg='pink')  # Cambiar el color de fondo de la ventana

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:", bg='pink')
etiqueta.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=30, bg='white')
entrada.pack(pady=5)

# Botones
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato, bg='lavender')
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos, bg='lavender')
boton_limpiar.pack(pady=5)

# Lista para mostrar los datos
lista_datos = tk.Listbox(ventana, width=50, height=10, bg='white', selectbackground='lightpink')
lista_datos.pack(pady=10)

# Iniciar el bucle principal
ventana.mainloop()