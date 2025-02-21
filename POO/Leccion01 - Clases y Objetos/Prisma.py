class Prisma:
    """
    Clase para calcular el volumen de un prisma dados valores por el usuario
    """

    def __init__(self, largo, ancho, profundo):
        self.largo = largo
        self.ancho = ancho
        self.profundo = profundo

    def calcularVolumen(self):
        return self.largo * self.ancho * self.profundo


largo = int(input("Ingrese el valor del largo que tiene el prisma: \n"))
ancho = int(input("Ingrese el valor del ancho que tiene el prisma: \n"))
profundo = int(input("Ingrese el valor de la profundidad del prisma: \n"))

prism1 = Prisma(largo, ancho, profundo)
print(f'Volumen = {prism1.calcularVolumen()} u^3\n')
