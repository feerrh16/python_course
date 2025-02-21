# Leer contenido online
import requests

url = 'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
}

try:
    respuesta = requests.get(url, headers=headers)
    respuesta.raise_for_status()  # Lanza una excepción si la solicitud no tiene éxito (código de estado diferente de 200)
    
    contenido = respuesta.text  # Obtener el contenido de la respuesta en texto
    
    print(contenido)
    
    with open('C:\\CURSOS\\Python\\Profundizando en Python\\nuevo_archivo_requests.txt', 'w', encoding='UTF-8') as archivo:
        archivo.write(contenido)

except requests.exceptions.RequestException as e:
    print(f"No se pudo acceder al archivo: {e}")
