
"""Ejercicio 07"""
class Cadena:
    def __init__(self):
        self.termino = "Hola Pythonistas, seguimos adelante"
        self.revertida = 0
    def revertir(self):
        self.list = self.termino.split()
        self.list.reverse()
        self.revertida = " ".join(self.list)

grupo_01 = Cadena()
grupo_01.revertir()
print("La cadena de palabras revertida es: {}".format(grupo_01.revertida))

grupo_02 = Cadena()
grupo_02.revertir()
print("La cadena de palabras invertida es: {}".format(grupo_02.revertida))