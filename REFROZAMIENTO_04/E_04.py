
string = "Hello Pythonista"
def bloque_01(string):
    try:
        resultado = len(string) / 0
        print("El resultado de la division es:", resultado)
    except ZeroDivisionError as e:
        print("Se produjo un error de división por cero:", e)
        print("Causa: No se puede dividir un valor por cero.")
        print("Solución: Corrobora de no intentar dividir entre cero en las operaciones.")

bloque_01(string)
