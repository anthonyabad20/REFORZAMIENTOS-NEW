import random

def generar_aleatorios():
    lista = []
    for _ in range(30):
        lista.append(random.randint(0,100))
    print("La lista de numeros aleatorios: {}".format(lista))
    return lista

def orden_lista(lista):
    lista.sort()
    print("La lisra ordenada es: {}".format(lista))


