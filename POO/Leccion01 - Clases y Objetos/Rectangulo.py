class Rectangulo:
    """
    Clase que calcula el perímetro y el área de un rectángulo con valores introducidos por el usuario
    """

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return (self.base * 2) * (self.altura * 2)


base = float(input("Ingrese el valor de la base: \n"))
altura = float(input("Ingrese el valor de la altura: \n"))

R1 = Rectangulo(base, altura)
print(f'Perímetro = {R1.calcularPerimetro()} u')
print(f'Área = {R1.calcularArea()} u^2')
