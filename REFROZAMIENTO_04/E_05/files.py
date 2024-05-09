def validar_nombres(nom_usuario):
    if len(nom_usuario) < 7:
        print("{} debe contener al menos 7 caracteres".format(nom_usuario))
        return False
    elif len(nom_usuario) < 12:
        print("{} no puede contener mas  12 caracteres".format(nom_usuario))
        return False
    elif nom_usuario.isalnum():
        print("{} puede contener solo letras y números".format(nom_usuario))
        return False
    else:
        return True