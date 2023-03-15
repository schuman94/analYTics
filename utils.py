import tkinter as tk
from tkinter import filedialog
import os
from datetime import datetime

# Extrae el nombre de la lista de canales sin la extension
def obtener_nombre_sin_extension(ruta):
    nombre = os.path.basename(ruta)
    nombre_sin_extension, _ = os.path.splitext(nombre)
    return nombre_sin_extension

# Función para seleccionar el archivo de destino
def seleccionar_destino(entry_destino):
    directorio_destino = filedialog.askdirectory(title="Seleccionar directorio de destino")
    entry_destino.delete(0, tk.END)
    entry_destino.insert(0, directorio_destino)

# Función para generar la ruta del destino
def generar_ruta_destino(directorio, lista_canales):
    fecha_hora = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    nombre_lista_canales = obtener_nombre_sin_extension(lista_canales)
    nombre_archivo = f"recuento_{nombre_lista_canales}_{fecha_hora}.txt"
    return os.path.join(directorio, nombre_archivo)

# Función para seleccionar el archivo de lista de canales
def seleccionar_lista_canales(entry_lista_canales):
    ruta_lista_canales = filedialog.askopenfilename(title="Seleccionar lista de canales")
    entry_lista_canales.delete(0, tk.END)
    entry_lista_canales.insert(0, ruta_lista_canales)

# Función para seleccionar el archivo de la clave de API
def seleccionar_api_key(entry_api_key):
    ruta_api_key = filedialog.askopenfilename(title="Seleccionar archivo de la clave de API")
    entry_api_key.delete(0, tk.END)
    entry_api_key.insert(0, ruta_api_key)