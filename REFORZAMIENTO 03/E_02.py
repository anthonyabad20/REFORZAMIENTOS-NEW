"""Ejercicio 02"""

numero_01 = int(input("Ingrese el primer numero: "))
numero_02 = int(input("Ingrese un el segundo numero: "))

lista_01 = []
lista_02 = []

def lista(numero_01, numero_02):
    if numero_01 > numero_02:
        valor = numero_02 + 1

        while valor < numero_01:
            lista_01.append(valor ** 2)
            valor = valor + 1
        print("Los cuadrados de los valores entre {} y {} son: {}".format(numero_01, numero_02, lista_01))

    elif numero_02 > numero_01:
        valor = numero_01 + 1

        while valor < numero_02:

            lista_02.append(valor, 2)
            valor = valor + 1
            print("Los cuadrados de los valores entre {} y {} son: {}".format(numero_01, numero_02, lista_02))

    else:
        print("Los números son iguales")
lista(numero_01, numero_02)