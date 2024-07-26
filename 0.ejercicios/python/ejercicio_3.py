"""
Utilizando la función range() y la conversión a listas, generar las siguientes listas dinámicamente:

    Todos los números del 0 al 10 [0, 1, 2, ..., 10]  ✅
    Todos los números del -10 al 0 [-10, -9, -8, ..., O] ✅
    Todos los números pares del 0 al 20 [0, 2, 4, ..., 20] ✅
    Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1] ✅
    Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50] ✅
"""


print("Lista 1:")
lista = []
for i in range(0,11):
    lista.append(i)
print(lista, end='\n\n')

print("Lista 2:")
lista = []
for i in range(-10,1):
    lista.append(i)
print(lista, end='\n\n')

print("Lista 3:")
lista = []
for i in range(0,21,2):
    lista.append(i)
print(lista, end='\n\n')

print("Lista 4:")
lista = []
# for i in range(-20,1):
    # if i % 2 != 0:
for i in range(-19,0,2):
        lista.append(i)
print(lista, end='\n\n')

print("Lista 5:")
lista = []
for i in range(0,51):
    if i % 5 == 0:
        lista.append(i)
print(lista, end='\n\n')



def main_third(): 
    _inner_transform_list = lambda range_data : list(range_data)
    list_ranges =[
        _inner_transform_list(rango)
        for rango in 
        [range(11),range(-10,1),range(0,21,2),range(-19,0,2),range(0,51,5)]
    ] 

    for  _ in list_ranges:
        print(_)