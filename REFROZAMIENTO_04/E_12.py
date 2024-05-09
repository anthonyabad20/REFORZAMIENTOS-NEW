def buenos_dias(funcion_a_decorar):
    def wrapper(*args, **kwargs):
        print("Buenos días!")
        resultado = funcion_a_decorar(*args, **kwargs)
        print("Hasta luego!")
        return resultado
    return wrapper

@buenos_dias
def saludar(nombre):
    return f"Soy {nombre}"

nombre = input("Ingrese su nombre: ")
print(saludar(nombre))
