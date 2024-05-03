"""Ejercicio 11"""
class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.bonificacion_01 = 0

    def mayor(self):
        if self.edad >= 18:
            print("La persona es mayor de edad")
        else:
            print("La persona es menor de edad")

    def bonifica(self):
        self.bonificacion_01 = self.sueldo * 1.2
        print("El sueldo con bonificación es {}".format(self.bonificacion_01))

pers_1 = Persona("Rocio", 21, 3000)
pers_1.mayor()
pers_1.bonifica()

pers_2 = Persona("Nathaly", 22, 1025)
pers_2.mayor()
pers_2.bonifica()