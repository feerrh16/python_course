# Profundizando en el tipo Float
a = 3.0
# Formato a valores de tipo flotante:
# print(f'a: {a:.2f}')
# Constructor float puede recibir int y str
a = float(10)
a = float('10')
# print(f'a: {a:.2f}')
# Notación exponencial (valores positivos o negativos)
a = 3e5
a = 3e-5
# print(f'a: {a:2f}')
# Cualquier cálculo que involucre un float, se promueve a float
a = 4.0 + 5
print(f'a: {a:.2f}')
