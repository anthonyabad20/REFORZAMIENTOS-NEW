def decorador(func):
    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función")
        producto = func(*args, **kwargs)
        print("La función ha sido ejecutada correctamente")
        return producto
    return wrapper

@decorador
def multiplicar(*args):
    producto = 1
    for arg in args:
        producto = producto * arg
    return producto

producto = multiplicar(10, 34, 9, 10)
print("El resultado de la multiplicación es: ", producto)


