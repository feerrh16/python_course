class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        self._id_producto = Producto.generar_id()

        if self.validar_nombre(nombre):
            self._nombre = nombre
        else:
            print('Ingrese un producto válido')

        if self.validar_precio(precio):
            self._precio = precio
        else:
            print('Ingrese un precio válido')

    # Métodos get
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
    
    # Métodos set
    @nombre.setter
    def nombre(self, nombre):
        if self.validar_nombre(nombre):
            self._nombre = nombre
        else:
            print('Ingrese un producto válido')

    @precio.setter
    def precio(self, precio):
        if self.validar_precio(precio):
            self._precio = precio
        else:
            print('Ingrese un precio válido')

    # Validaciones
    def validar_precio(self, valor):
        return True if 1 < valor < 999 else False
    
    def validar_nombre(self, nombre):
        return True if nombre != '' else False
    
    @classmethod
    def generar_id(cls):
        cls.contador_productos += 1
        return cls.contador_productos
    
    def __str__(self):
        return  f'ID: {self._id_producto}\n' \
                f'Nombre: {self._nombre}\n' \
                f'Precio: ${self._precio}\n'
                
if __name__ == '__main__':
    producto1 = Producto('Camisa', 250.00)
    print(producto1)

    producto2 = Producto('Pantalón', 300.00)
    print(producto2)
