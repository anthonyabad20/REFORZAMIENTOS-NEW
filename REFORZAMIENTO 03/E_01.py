
"""Ejercicio 01"""
num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))

list_1 = []
list_2 = []

for valor in str(num_1):
    list_1.append(int(valor))

for valor in str(num_2):
    list_2.append(int(valor))

resultado_1 = sum(list_1)
resultado_2 = sum(list_2)

def sum_digit(num_1, num_2):
   if resultado_2 > resultado_1:
       print("La suma de dígitos de {} es mayor".format(num_2))
   else:
       print("La suma de dígitos de {} es mayor".format(num_1))

   if resultado_2 > 10:
       print("La suma de dígitos de {} es mayor de 10".format(num_2))
   if resultado_1 > 10:
       print("La suma de dígitos de {} es mayor de 10".format(num_1))
   else:
       print("Ninguna suma de dígitos de los número es mayor de 10")

sum_digit(num_1, num_2)