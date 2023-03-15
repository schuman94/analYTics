import re
from googleapiclient.discovery import build

# Extraer el ID del canal de la URL del canal
def get_channel_id(url):
    # Extraer el ID del canal de la URL del canal
    channel_id = None

    # Ejemplo de URL de canal: https://www.youtube.com/channel/UC1234567890abcdefABCDEF
    match = re.search(r'youtube\.com/channel/([^/]+)', url)
    if match:
        channel_id = match.group(1)
    else:
        # Ejemplo de URL de usuario: https://www.youtube.com/user/ExampleUserName
        match = re.search(r'youtube\.com/user/([^/]+)', url)
        if match:
            channel_id = match.group(1)
        else:
            # Ejemplo de URL con arroba: https://www.youtube.com/@ExampleUserName
            match = re.search(r'youtube\.com/@([^/]+)', url)
            if match:
                channel_id = match.group(1)
    
    return channel_id

#Extrae el numero de suscriptores del canal
def get_subscriber_count(api_key, channel_id):
    # Crear un objeto de servicio de YouTube utilizando la clave de API
    youtube = build('youtube', 'v3', developerKey=api_key)

    if not channel_id.startswith('UC'):
        # Si channel_id es un nombre de usuario, busque el ID de canal real
        search_response = youtube.search().list(
            part='snippet',
            type='channel',
            q=channel_id,
            maxResults=1,
            fields='items(id(channelId))'
        ).execute()
        if search_response['items']:
            channel_id = search_response['items'][0]['id']['channelId']
        else:
            return None

    # Obtener la información del canal utilizando la API de datos de YouTube
    channel_info = youtube.channels().list(
        part='statistics',
        id=channel_id
    ).execute()

    # Extraer y devolver el recuento de suscriptores
    return int(channel_info['items'][0]['statistics']['subscriberCount'])