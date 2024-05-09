
def cargar_numero():
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            return numero
        except ValueError:
            print("Error: Ingrese un numero entero.Intente nuevamente")
def suma(a, b):
    return a+b
