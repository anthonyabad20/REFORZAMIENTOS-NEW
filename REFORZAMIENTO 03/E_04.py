

"""Ejercicio 04"""

orac = input("Ingrese una oración con más de 2 palabras: ")

def cont_palab(orac):
    list_palab = orac.split()
    total = len(list_palab)

    if total >= 3:
        return print("La cantidad de palabras es: {}".format(total))

    else:
        return print("Ha ingresado una oración con menos de 3 palabras")


cont_palab(orac)
