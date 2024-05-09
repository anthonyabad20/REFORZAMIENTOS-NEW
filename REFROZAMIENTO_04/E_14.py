def decorador_argumentos(func):
    def wrapper(*args, **kwargs):
        print("La cantidad de argumentos que tiene la función es:", len(args) + len(kwargs))
        resultado = func(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente")
        return resultado
    return wrapper
@decorador_argumentos
def sumar(*args, **kwargs):
    total = 0
    for arg in args:
        total += arg
    for key, value in kwargs.items():
        total += value
    return total

# Ejemplo de uso
resultado = sumar(8, 9, 7,9, valor1=3, valor2=2)
print("El resultado de la suma es : {}".format(resultado))


