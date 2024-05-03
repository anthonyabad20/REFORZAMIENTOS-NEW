"""Ejercicio 06"""
class Valor:
    def __init__(self):
        self.val= 0
        self.cubo = 0
        self.cuadrado = 0

    def ingrese_valor(self):
        self.val = int(input("Ingrese un valor: "))

    def cubo_r(self):
        self.cubo = self.val ** 3

    def cuadrado_r(self):
        self.cuadrado = self.cubo ** 2

val_01 = Valor()
val_01.ingrese_valor()
val_01.cubo_r()
val_01.cuadrado_r()

print("El valor ingresado es: {}".format(val_01.val))
print("El cubo del valor ingresado es: {}".format(val_01.cubo))
print("El cuadrado del cubo del valor ingresado es: {}".format(val_01.cuadrado))