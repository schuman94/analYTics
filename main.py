import tkinter as tk
from tkinter import ttk
from gui import crear_widgets
from channel_processing import iniciar_recuento

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Recuento de canales")

# Crear los campos de entrada
entry_destino = ttk.Entry(ventana, width=50)
entry_lista_canales = ttk.Entry(ventana, width=50)
entry_api_key = ttk.Entry(ventana, width=50)

# Crear y posicionar los widgets en la ventana
crear_widgets(ventana, entry_destino, entry_lista_canales, entry_api_key, lambda: iniciar_recuento(entry_api_key, entry_destino, entry_lista_canales))

# Iniciar el bucle principal de eventos
ventana.mainloop()