import csv
from utils import generar_ruta_destino
from youtube_api import get_channel_id, get_subscriber_count

# Función para iniciar el recuento
def iniciar_recuento(entry_api_key, entry_directorio, entry_lista_canales):
    archivo_api_key = entry_api_key.get()
    with open(archivo_api_key, 'r') as f:
        api_key = f.read().strip()

    directorio = entry_directorio.get()
    lista_canales = entry_lista_canales.get()

    # Leer las URL de los canales de YouTube desde el archivo de entrada
    with open(lista_canales, 'r') as f:
        urls = f.read().splitlines()

    # Obtener el recuento de suscriptores para cada canal
    resultados = []
    for url in urls:
        channel_id = get_channel_id(url)
        if channel_id:
            subscriber_count = get_subscriber_count(api_key, channel_id)
            resultados.append((url, subscriber_count))
        else:
            print(f"No se pudo obtener el ID del canal para la URL: {url}")

    # Generar la ruta de destino con el nombre personalizado
    destino = generar_ruta_destino(directorio, lista_canales)

    # Escribir los resultados en un archivo de texto en la ruta de destino
    with open(destino, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        for resultado in resultados:
            writer.writerow(resultado)