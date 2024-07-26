"""
Contar cuantas veces aparece un elemento en una lista.
"""

count = 0

l = [1,2,3,4,5,6,7,8,9,8,6,4,3,3,1,7,8,10,20,3,5]

n = int(input("Escribe un numero del 1 al 20: "))

for i in l:
    if n == i:
        count += 1

print(f"El numero de repeticiones es: {count}")