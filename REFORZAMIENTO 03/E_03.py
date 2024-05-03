
"""Ejercicio 03"""

valor = int(input("Ingrese un numero: "))
lista_01 = []   #e lista indicara los digitos del numero

for num in str(valor):
    lista_01.append(int(num))

def suma_digitos(valor):
    return sum(lista_01)

print("La suma de los dígitos del número es: {}".format(suma_digitos(valor)))