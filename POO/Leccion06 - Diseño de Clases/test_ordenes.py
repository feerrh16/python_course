from Producto import *
from Orden import *

if __name__ == '__main__':
    producto1 = Producto('Camisa', 250.00)
    producto2 = Producto('Pantalón', 300.00)
    producto3 = Producto('Falda', 340.00)
    producto4 = Producto('Zapatillas', 800.00)

    productos1 = [producto1, producto2]
    productos2 = [producto3, producto4]

    orden1 = Orden(productos1)
    print(orden1)
    # print(orden1.calcular_total())

    orden2 = Orden(productos2)
    print(orden2)
    # print(orden2.calcular_total())
    