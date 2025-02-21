# Módulo de Prueba

from Persona import Persona

print(f'Módulo en ejecución: {__name__}'.center(30, '-'))
persona1 = Persona('Juan', 'Javier', 21)
persona1.mostrar_info()
persona1.__del__()
