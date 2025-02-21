from Empleado import *
from Gerente import *

# Aplicación del Polimorfismo
def imprimir_detalles(objeto):
    print(type(objeto))
    print(f'{objeto.mostrar_detalles()}\n')
    if isinstance(objeto, Gerente):
        print(objeto._departamento)


empleado1 = Empleado('Juan', 9000)
imprimir_detalles(empleado1)

gerente1 = Gerente('Karla', 24000, 'Finanzas')
imprimir_detalles(gerente1)
