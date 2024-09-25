import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Configurar color de fondo
        self.root.configure(bg='pink')

        # Lista para almacenar las tareas
        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        # Botón para añadir tarea
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Botón para marcar tarea como completada
        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Vínculo de la tecla Enter para añadir tarea
        self.task_entry.bind("<Return>", lambda event: self.add_task())


    def add_task(self):
        """Añade una tarea a la lista si el campo de entrada no está vacío."""
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def complete_task(self):
        """Marca la tarea seleccionada como completada cambiando su color."""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            self.tasks[selected_task_index[0]] = f"{task} (Completada)"
            self.update_task_listbox()
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para marcarla como completada.")

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminarla.")

    def update_task_listbox(self):
        """Actualiza el Listbox para reflejar las tareas actuales."""
        self.task_listbox.delete(0, tk.END)  # Limpiar el Listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Añadir cada tarea al Listbox

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()