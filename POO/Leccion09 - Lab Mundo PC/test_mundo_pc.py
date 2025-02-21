from Orden import *
from Computadora import *

raton1 = Raton('USB', 'Logitech')
teclado1 = Teclado('USB', 'Razer')
monitor1 = Monitor('Samsung', 60)
computadora1 = Computadora('PC Ofimática', raton1, teclado1, monitor1)

raton2 = Raton('Bluetooth', 'HyperX')
teclado2 = Teclado('Bluetooth', 'Custom')
monitor2 = Monitor('Sony', 35)
computadora2 = Computadora('Gamer', raton2, teclado2, monitor2)

raton3 = Raton('USB', 'Red Dragon')
teclado3 = Teclado('USB', 'Razer')
monitor3 = Monitor('Asus', 27)
computadora3 = Computadora('Custom', raton3, teclado3, monitor3)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)

orden1.agregar_computadora(computadora3)
print(orden1)

computadoras2 = [computadora1, computadora3]
orden2 = Orden(computadoras2)
print(orden2)
