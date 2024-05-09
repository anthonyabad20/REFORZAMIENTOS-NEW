"""
Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]

"""
lista = [2, 6, 10, 4, 5, 23, 1]
def bloque(lista, indice):
    try:
        valor = lista[indice]
        print("El valor en el indice es ", valor)

    except IndexError as e:
        print("Se produjo un error de índice:", e)
        print("Causa: El índice está fuera del rango de la lista.")
        print("Solución: Asegúrate de acceder a un índice válido dentro de la lista.")

bloque(lista,10)


