"""
Escribir un programa que sume todos los números enteros impares desde el O hasta el 100
"""

n = 0
for i in range(101):
    if i % 2 != 0:
        n += i
print(f'Resultado: {n}')