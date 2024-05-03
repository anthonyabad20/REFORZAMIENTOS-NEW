""""Ejercicio 13"""
class Persona:
    def __init__(self):
        self.nombres = input("Ingrese nombres: ")
        self.edad = int(input("Ingrese edad "))

class Empleado(Persona):
    def __init__(self, sueldo):
        self.sueldo = sueldo

    def impuesto(self):
        if self.sueldo > 4000:
            self.impuesto = self.sueldo * 0.1
            print("El impuesto a pagar es: ", self.impuesto)
        else:
            print("No pagara impuestos")

empleado_1 = Empleado(6000)

print("El saldo del empleado es: {}".format(empleado_1.sueldo))
empleado_1.impuesto()

empleado_1 = Empleado(2000)

print("El saldo del empleado es: {}".format(empleado_1.sueldo))
empleado_1.impuesto()