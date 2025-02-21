from dominio.Pelicula import *
from servicio.CatalogoPeliculas import *

opcion = None

while opcion != 4:
    try:
        print('Opciones:')
        print('1. Agregar pelicula')
        print('2. Listar peliculas')
        print('3. Eliminar catálogo de peliculas')
        print('4. Salir')
        opcion = int(input('Ingresa una opción: '))

        if opcion == 1:
            nombre_pelicula = input('Ingresa el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_pelicula(pelicula)
        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()
        elif opcion == 3:
            CatalogoPeliculas.eliminar_peliculas()
        
    except Exception as e:
        print(f'Ocurrió un error: {e}')
        opcion = None
else:
    print('Fin del programa')
