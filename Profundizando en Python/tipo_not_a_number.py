from decimal import Decimal
import math

"""
NaN = Not a Number
NaN no es sensible a mayúsculas o minúsculas
NaN es un tipo de dato numérico indefinido
"""

a = float('nan')
print(f'a: {a}')
print(f'¿Es NaN (Not a Number)?: {math.isnan(a)}')

a = Decimal('nan')
print(f'a: {a}')
print(f'¿Es NaN (Not a Number)?: {math.isnan(a)}')
