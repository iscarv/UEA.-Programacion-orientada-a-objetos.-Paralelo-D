import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import calendar


class EventManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Eventos")
        self.root.configure(bg="#FFCCCB")  # Rosa bajito

        # Frame para la lista de eventos
        self.frame_event_list = ttk.Frame(root)
        self.frame_event_list.pack(pady=10)

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.frame_event_list, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para entrada de datos
        self.frame_input = ttk.Frame(root)
        self.frame_input.pack(pady=10)

        # Etiqueta y botón para seleccionar fecha
        ttk.Label(self.frame_input, text="Fecha:").grid(row=0, column=0)
        self.date_button = ttk.Button(self.frame_input, text="Seleccionar Fecha", command=self.open_calendar)
        self.date_button.grid(row=0, column=1)

        self.selected_date = None  # Para guardar la fecha seleccionada

        # Etiqueta y campo de entrada para hora
        ttk.Label(self.frame_input, text="Hora (HH:MM):").grid(row=1, column=0)
        self.time_entry = ttk.Entry(self.frame_input)
        self.time_entry.grid(row=1, column=1)

        # Etiqueta y campo de entrada para descripción
        ttk.Label(self.frame_input, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = ttk.Entry(self.frame_input)
        self.desc_entry.grid(row=2, column=1)

        # Botones de acción
        self.btn_add = ttk.Button(root, text="Agregar Evento", command=self.add_event)
        self.btn_add.pack(pady=5)

        self.btn_delete = ttk.Button(root, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.btn_delete.pack(pady=5)

        self.btn_exit = ttk.Button(root, text="Salir", command=root.quit)
        self.btn_exit.pack(pady=5)

    def open_calendar(self):
        """Abre un mini calendario para seleccionar la fecha."""
        self.calendar_window = tk.Toplevel(self.root)
        self.calendar_window.title("Mini Calendario")
        self.calendar_window.configure(bg="#FFCCCB")

        # Obtener la fecha actual
        self.today = datetime.now()
        self.current_month = self.today.month
        self.current_year = self.today.year

        # Mostrar el calendario
        self.show_calendar()

    def show_calendar(self):
        """Muestra el calendario del mes actual en la ventana."""
        # Limpiar la ventana del calendario
        for widget in self.calendar_window.winfo_children():
            widget.destroy()

        # Título del mes
        month_name = calendar.month_name[self.current_month]
        ttk.Label(self.calendar_window, text=f"{month_name} {self.current_year}", font=("Arial", 14)).grid(row=0,
                                                                                                           column=1,
                                                                                                           columnspan=5)

        # Flechas de navegación
        ttk.Button(self.calendar_window, text="<", command=self.prev_month).grid(row=0, column=0)
        ttk.Button(self.calendar_window, text=">", command=self.next_month).grid(row=0, column=6)

        # Días de la semana
        days = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        for i, day in enumerate(days):
            ttk.Label(self.calendar_window, text=day).grid(row=1, column=i)

        # Obtener los días del mes
        month_days = calendar.monthcalendar(self.current_year, self.current_month)

        # Crear botones para cada día
        for week_index, week in enumerate(month_days):
            for day in week:
                if day != 0:  # Solo los días válidos
                    btn = ttk.Button(self.calendar_window, text=str(day), command=lambda d=day: self.select_date(d))
                    btn.grid(row=week_index + 2, column=week.index(day), padx=5, pady=5)

    def prev_month(self):
        """Navega al mes anterior."""
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.show_calendar()

    def next_month(self):
        """Navega al siguiente mes."""
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.show_calendar()

    def select_date(self, day):
        """Selecciona una fecha y actualiza el campo de entrada."""
        self.selected_date = datetime(self.current_year, self.current_month, day)
        formatted_date = self.selected_date.strftime("%d/%m/%Y")
        self.date_button.config(text=f"Fecha: {formatted_date}")

        # Cierra la ventana del calendario
        self.calendar_window.destroy()

    def add_event(self):
        """Agrega un evento a la lista."""
        if self.selected_date:
            date = self.selected_date.strftime("%d/%m/%Y")
            time = self.time_entry.get()
            description = self.desc_entry.get()
            if time and description:
                self.tree.insert("", "end", values=(date, time, description))
                self.clear_entries()
            else:
                messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una fecha.")

    def delete_event(self):
        """Elimina el evento seleccionado de la lista."""
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este evento?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un evento para eliminar.")

    def clear_entries(self):
        """Limpia los campos de entrada."""
        self.time_entry.delete(0, 'end')
        self.desc_entry.delete(0, 'end')
        self.selected_date = None
        self.date_button.config(text="Seleccionar Fecha")


if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagerApp(root)
    root.mainloop()