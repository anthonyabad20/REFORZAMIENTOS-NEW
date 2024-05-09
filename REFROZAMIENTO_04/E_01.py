
def fun_suma():
    try:
        suma = 80 + "Hola pyhtonista"
        print("El rsultado de la suma es: {}".format(suma))

    except TypeError as e:
        print("Se produjo un error de tipo:",e)
        print("Causa: No se puede sumar un entero con una cadena")
        print("Solución: Asegurate de agregar valores del mismo tipo a la suma ")


    except Exception as e:
        mensaje = "Oops! Algo salió mal {}.".format(e)
        mensaje += "Ocurrio un error .Por favor , revisa tu codigo"
        return mensaje

fun_suma()

