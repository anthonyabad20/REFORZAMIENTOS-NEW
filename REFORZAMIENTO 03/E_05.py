"""Ejercicio 05"""

valores = int(input("Ingrese la cantidad de valores a añadir a la lista: "))

lista_01 = []

def remover_valor(lista_01, remover):
    i = 0
    while valores > i:
        valor = int(input("Ingrese un número a añadir a la lista_01 : "))
        lista_01.append(valor)
        i = i + 1


    remover = int(input("Ingrese el número a eliminar de la lista_01 : "))
    print("La lista original es: {}".format(lista_01))

    if remover in lista_01:
        lista_01.remove(remover)
        print("Los valores de la lista actualizada es: {}".format(lista_01))
    else:
        print("El valor no se encuentra en la lista")
        print("Los valores de la lista actualizada es: {}".format(lista_01))

    print("El número a eliminar es : {}".format(remover))

remover_valor(lista_01, valores)