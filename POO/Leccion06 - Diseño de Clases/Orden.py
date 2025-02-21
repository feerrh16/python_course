from Producto import *

class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        self._id_orden = Orden.generar_orden()

        if self.validar_productos(productos):
            self._productos = list(productos)
        else:
            print('Ingrese sus productos')

    def agregar_producto(self, producto):
        self._productos.append(producto)

    @classmethod
    def generar_orden(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    @property
    def productos(self):
        return self._productos
    
    @productos.setter
    def productos(self, productos):
        if self.validar_productos(productos):
            self._productos = productos
        else:
            print('Ingrese sus productos')

    def validar_productos(self, productos):
        return True if productos != '' else False

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__()
        return  f'Orden: {self._id_orden}\n' \
                f'Productos:\n{productos_str}\n' \
                f'Total de su compra: ${self.calcular_total()}\n'
    
if __name__ == '__main__':
    producto1 = Producto('Camisa', 250.00)
    producto2 = Producto('Pantalón', 300.00)
    productos1 = [producto1, producto2]
    orden1 = Orden(productos1)
    print(orden1)
    orden2 = Orden(productos1)
    print(orden2)
    