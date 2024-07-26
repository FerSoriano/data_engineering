"""
Dadas dos listas (las que se quiera crear), generar una tercera 
con los elementos que estén presentes en AMBAS listas. 
Retornar esta nueva lista pero sin elementos duplicados.
"""

lista_1 = [1,2,3,8,99]
lista_2 = [5,1,4,3,99,1]

lista_1.extend(lista_2)
lista_3 = list(set(lista_1))
lista_3.sort()

print(lista_3)