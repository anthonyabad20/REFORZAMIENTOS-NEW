"""Ejercicio 10"""

class Alumno:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def mostar(self):
        print("El alumno {}, tiene {} años y {} de nota final".format(self.nombre, self.edad, self.nota))

    def aprobo(self):
        if self.nota >= 11:
            print("El alumno aprobo con {} de nota final".format(self.nota))
        else:
            print("El alumno desaprobo con {} de nota final".format(self.nota))

persona_01 = Alumno("Pedro", 25, 15)
persona_01.mostar()
persona_01.aprobo()

persona_02 = Alumno("Eduardo", 21, 13)
persona_02.mostar()
persona_02.aprobo()

persona_3 = Alumno("Alonso", 18, 18)
persona_3.mostar()
persona_3.aprobo()