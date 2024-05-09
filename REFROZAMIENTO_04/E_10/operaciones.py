def persona():
    nombre = input('Nombre del persona: ')
    apellido = input('Apellido del persona: ')
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad > 0:
                break
            else:
                print("La edad debe ser mayor a 0.Intente nuevamente.")
        except ValueError:
            print("Error: La edad debe ser un numero entero.Intente nuevamente.")
    personas_info = f"{nombre}, {apellido}, {edad}\n"
    with open("agenda.txt", "a") as archivo:
        archivo.write(personas_info)
    print("La información de la persona se ha agregado a la 'agenda.txt' exitosamente")
