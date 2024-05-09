import files
nom_usuario = input('Nombre de usuario: ')
if files.validar_nombres(nom_usuario):
    print("Nombre de usuario correcto")
else:
    print("Nombre de usuario incorrecto.Intente nuevamente")

