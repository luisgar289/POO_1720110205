class Examen():

    def __init__(self):
        pass

    def bucleWhile (self):

        repetir = "s"

        while repetir == "s":
            print("")
            materia = input("Materia: ")
            print("")
            cantidad = int(input("Número de alumnos: "))
            print("")
            alumno = input("Nombre del alumno: ")
            print("")
            clases = int(input("Número de clases: "))
            print("")
            retardos = int(input("Número de retardos: "))
            print("")
            if retardos == 3:
                falta = int(input("Número de faltas: " ))
                falta1 = falta + 1
                falta2 = clases - falta1 
            else:
                falta = int(input("Número de faltas: "))
                falta2 = clases -falta
            promedio = int(falta2 * 100 / clases)
            print("")
            print("Porcentaje de asistencias {}%" .format(promedio))
            print("")
            if promedio >= 80:
                print("{} tiene derecho a presentar examen" .format(alumno))
            else:
                print("{} no tiene derecho a presentar examen" .format(alumno))
            print("")
            repetir = str(input("Otra evaluación (s/n): "))

examen = Examen()

examen.bucleWhile()