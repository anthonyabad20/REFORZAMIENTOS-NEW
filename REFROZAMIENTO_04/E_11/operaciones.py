
def califica(nombre, nota_01, nota_02):
    promedio = (nota_01 + nota_02) / 2

    with open('calificaciones.txt', 'a') as f:

        f.write(f'{nombre},{nota_01},{nota_02},{promedio}')

def leer(nombre):
    with open('calificaciones.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            nombre_linea, _, _, promedio_linea = line.split(',')
            if nombre_linea == nombre:
                aprobado = float(promedio_linea) > 10
                return aprobado
    return False

nombre = input("Ingrese el nombre del alumno: ")

nota_01 = float(input("Ingrese la nota del alumno: "))
nota_02 = float(input("Ingrese la nota del alumno: "))

califica(nombre, nota_01, nota_02)
aprobado = leer(nombre)

if aprobado:
    print("El alumno {} esta aprobado".format(nombre))
else:
    print("El alumno {} esta desaprobado".format(nombre))


