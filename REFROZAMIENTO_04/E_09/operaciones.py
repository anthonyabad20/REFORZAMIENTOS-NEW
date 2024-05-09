def numeros_enteros():
    while True:
        try:
            numero = int(input("Ingrese un numero entero entre 1 y 20: "))
            if numero >= 1 and numero <= 20:
                break
            else:
                print("El numero debe estar entre 1 y 20. Intente de nuevo")
        except ValueError:
            print("Error:Ingrese un valor entero.Intente de nuevo")
    with open("tabla.txt", "w") as archivo:
        for i in range(1,11):
            resultado = numero * i
            linea = f"{numero} x {i} = {resultado}\n"
            archivo.write(linea)
    print("Tabla creada exitosamente")
