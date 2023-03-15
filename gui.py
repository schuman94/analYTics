from tkinter import ttk
from utils import seleccionar_destino, seleccionar_lista_canales, seleccionar_api_key

def crear_widgets(ventana, entry_destino, entry_lista_canales, entry_api_key, iniciar_recuento):
    # Crear y posicionar los widgets
    label_destino = ttk.Label(ventana, text="Destino:")
    label_destino.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    entry_destino.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    boton_destino = ttk.Button(ventana, text="Seleccionar", command=lambda: seleccionar_destino(entry_destino))
    boton_destino.grid(row=0, column=2, padx=5, pady=5, sticky="w")

    label_lista_canales = ttk.Label(ventana, text="Lista de canales:")
    label_lista_canales.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    entry_lista_canales.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    boton_lista_canales = ttk.Button(ventana, text="Seleccionar", command=lambda: seleccionar_lista_canales(entry_lista_canales))
    boton_lista_canales.grid(row=1, column=2, padx=5, pady=5, sticky="w")

    label_api_key = ttk.Label(ventana, text="Archivo de la clave de API:")
    label_api_key.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    entry_api_key.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    boton_api_key = ttk.Button(ventana, text="Seleccionar", command=lambda: seleccionar_api_key(entry_api_key))
    boton_api_key.grid(row=2, column=2, padx=5, pady=5, sticky="w")

    boton_iniciar = ttk.Button(ventana, text="Iniciar recuento", command=iniciar_recuento)
    boton_iniciar.grid(row=3, column=0, columnspan=3, pady=10)

    # Iniciar el bucle principal de eventos
    ventana.mainloop()