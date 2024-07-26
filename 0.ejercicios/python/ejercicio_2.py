"""
Escribir un programa que pida al usuario cuántos números quiere introducir. 
Luego que lea todos los números y realice una media aritmética.
"""
try:
    numbers = []
    x = int(input("Cuantos numeros quieres introducir? "))

    for i in range(x):
        num = int(input(f"Numero {i + 1}: "))
        numbers.append(num)

    suma = sum(numbers)

    print(f"La media de los numeros es: {round((suma / x),2)}")

except:
    print("Escribe un numero valido.")

