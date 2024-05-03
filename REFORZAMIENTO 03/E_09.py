"""Ejercicio 09"""

import math

class Circulo:
    def __init__(self):
        self.radio = 0
        self.area = 0
        self.peri = 0

    def radio_solicitar(self):
        while True:
            try:
                self.radio = float(input("Ingrese el radio del circulo: "))
                break
            except ValueError:
                print("Error.El valor ingresado no es un número")

    def area_circulo(self):
        self.area = math.pi * (self.radio ** 2)

    def perimet_circulo(self):
        self.peri = 2 * math.pi * self.radio

circulo_1 = Circulo()
circulo_1.radio_solicitar()
circulo_1.area_circulo()
circulo_1.perimet_circulo()

print("El radio del circulo 1 es: {}".format(circulo_1.radio))
print("El perimetro del circulo 1 es: {}".format(circulo_1.peri))
print("El area del circulo 1 es: {}".format(circulo_1.area))


circulo_2 = Circulo()
circulo_2.radio_solicitar()
circulo_2.area_circulo()
circulo_2.perimet_circulo()

print("El radio del circulo 2 es: {}".format(circulo_2.radio))
print("El perimetro del circulo 2 es: {}".format(circulo_2.peri))
print("El area del circulo 2 es: {}".format(circulo_2.area))