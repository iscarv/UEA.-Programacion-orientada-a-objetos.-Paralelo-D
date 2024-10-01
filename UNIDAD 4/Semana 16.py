import tkinter as tk
from tkinter import messagebox

# Clase principal que define la aplicación de gestión de tareas
class TaskManagerApp:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Gestión de Tareas")  # Título de la ventana
        self.root.geometry("400x400")  # Tamaño de la ventana
        self.root.config(bg="#E6E6FA")  # Fondo de color morado claro (Lavender)

        # Lista para almacenar las tareas con su estado (completada o no)
        self.tasks = []

        # Campo de entrada para agregar nuevas tareas
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', lambda event: self.add_task())  # Atajo para añadir tarea con la tecla "Enter"

        # Botón para añadir una nueva tarea (botones con fondo blanco)
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task, bg="white", fg="black")
        self.add_button.pack(pady=5)

        # Botón para marcar una tarea como completada (botones con fondo blanco)
        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task, bg="white", fg="black")
        self.complete_button.pack(pady=5)

        # Botón para eliminar una tarea seleccionada (botones con fondo blanco)
        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task, bg="white", fg="black")
        self.delete_button.pack(pady=5)

        # Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.pack(pady=10)

        # Definición de atajos de teclado
        self.root.bind('<Escape>', lambda event: self.root.quit())  # Atajo para cerrar la aplicación con "Escape"
        self.root.bind('<c>', lambda event: self.complete_task())  # Atajo para completar tarea con la tecla "C"
        self.root.bind('<d>', lambda event: self.delete_task())  # Atajo para eliminar tarea con la tecla "D"
        self.root.bind('<Delete>', lambda event: self.delete_task())  # Alternativa para eliminar tarea con "Delete"

    # Función para añadir una tarea a la lista
    def add_task(self):
        task = self.entry.get()
        if task:  # Verificar si el campo no está vacío
            # Agregar la tarea a la lista de tareas con el estado "no completada"
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()  # Actualizar la lista visual de tareas
            self.entry.delete(0, tk.END)  # Limpiar el campo de entrada después de agregar la tarea

    # Función para marcar una tarea como completada
    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()  # Obtener el índice de la tarea seleccionada
        if selected_task_index:  # Verificar si se ha seleccionado una tarea
            index = selected_task_index[0]  # Obtener el índice de la tarea
            # Marcar la tarea como completada
            self.tasks[index]["completed"] = True
            self.update_task_listbox()  # Actualizar la lista visual de tareas

    # Función para eliminar una tarea de la lista
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()  # Obtener el índice de la tarea seleccionada
        if selected_task_index:  # Verificar si se ha seleccionado una tarea
            index = selected_task_index[0]  # Obtener el índice de la tarea
            del self.tasks[index]  # Eliminar la tarea de la lista de tareas
            self.update_task_listbox()  # Actualizar la lista visual de tareas

    # Función para actualizar el contenido del Listbox
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Limpiar la lista actual
        for task in self.tasks:
            # Formatear el texto de la tarea, indicando si está completada
            display_text = task["task"] + (" [Completada]" if task["completed"] else "")
            self.task_listbox.insert(tk.END, display_text)  # Añadir la tarea al Listbox

# Crear la ventana principal de Tkinter y lanzar la aplicación
root = tk.Tk()
app = TaskManagerApp(root)
root.mainloop()