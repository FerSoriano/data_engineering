"""
Escribir un programa que lea un número impar por teclado.
Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.
"""

while True:
    try:
        n = int(input("Escribe un numero: "))

        if n % 2 != 0:
            print("El numero es IMPAR!✅")
            break
        else:
            print("El numero NO es IMPAR!❌")
        
    except:
        print("Escribe un numero valido! ⚠️")
    


