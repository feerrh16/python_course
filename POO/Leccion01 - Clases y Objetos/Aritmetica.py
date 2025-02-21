class Aritmetica:
    """Clase para realizar las operaciones aritméticas básicas"""

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


op1 = Aritmetica(12, 3)
print(f'Resultado: {op1.sumar()}')

op2 = Aritmetica(234, 2)
print(f'Resultado: {op2.restar()}')

op3 = Aritmetica(34, 34)
print(f'Resultado: {op3.multiplicar()}')

op4 = Aritmetica(34, 12)
print(f'Resultado: {op4.dividir()}')
