
"""Ejercicio 08"""

class Nombre:
    def __init__(self):
        self.nombres = False
        self.edad = 0

    def ingreso_datos(self):
        self.nombres = input("Ingrese su nombre y apellido: ")
        self.edad = int(input("Ingrese su edad: "))

    def resultado(self):
        self.diccionario = {"nombre y apellido": self.nombres, "edad": self.edad}

nombre_01 = Nombre()
nombre_01.ingreso_datos()
nombre_01.resultado()
print(nombre_01.diccionario)