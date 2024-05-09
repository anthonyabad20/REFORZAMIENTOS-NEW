"""
Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
persona= { 'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
persona['profesion']
"""
persona= { 'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
def bloque(persona, clave):
    try:
        valor = persona[clave]
        print("El valor de la claver es: ", valor)

    except KeyError as e:
        print("Se produjo un error de clave:", e)
        print("Causa: La clave ingresada no existe en el diccionario.")
        print("Solución: Asegúrate de acceder a una clave válida dentro del diccionario.")
bloque(persona,'profesion')
