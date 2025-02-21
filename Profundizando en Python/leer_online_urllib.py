# Leer contenido online
import urllib
from urllib.request import urlopen

peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
with urlopen(peticion) as mensaje:
    contenido = mensaje.read().decode('utf-8')
    print(contenido)

with open('C:\\CURSOS\\Python\\Profundizando en Python\\nuevo_archivo_urllib.txt','w', encoding='utf-8') as archivo:
    archivo.write(contenido)
