nombre = input("Ingrese el nombre del alumno: ")

nota_01 = float(input("Ingrese la nota del alumno: "))
nota_02 = input(("Ingrese la nota del alumno: "))
calificaciones(nombre, nota_01, nota_02)
aprobado = leer(nombre)

if aprobado:
    print("El alumno {} esta aprobado".format(nombre))
else:
    print("El alumno {} esta desaprobado".format(nombre))

