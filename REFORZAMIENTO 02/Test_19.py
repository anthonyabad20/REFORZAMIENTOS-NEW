"""Ejercicio 19"""
lista_08 = []
numero = 0

while numero < 10:
    lista_08.append(int(input("Ingresa un número entero: ")))
    numero = numero + 1

suma = sum(lista_08)
print("La suma de los valores ingresados es:", suma)

media = suma / len(lista_08)
print("La media de los valores ingresados es:", media)