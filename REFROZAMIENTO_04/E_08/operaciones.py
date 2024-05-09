import math
def cargar_entero():
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            return numero
        except ValueError:
            print("Error: Ingrese un numero entero.Intente nuevamente")

def raiz(numero):
    raiz = math.sqrt(numero)
    print("El resultado de la raiz cuadrada es: ", raiz)

def potencias(numero):
    cuadrado = numero ** 2
    cubo = numero ** 3
    print("{} elevado al cuadrado es {}".format(numero, cuadrado))
    print("{} elevado al cubo es {}".format(numero, cubo))



