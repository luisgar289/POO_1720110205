class Examen():

    materia = None
    alumno = None
    clases = None
    retardos = None
    falta = None
    falta1 = None
    promedio = None
    bucle = None

    def __init__ (self):
        pass

    def materias (self):
        self.materia = input("Materia: ")
            
    def alumnos (self):
        self.alumno = input("Nombre del alumno: ")

    def clase (self):
        self.clases = input("Numero de clases: ")
            
    def retardo (self):
        self.retardos = int(input("Numero de retardos: "))
            
    def falta (self):
        if self.retardos == 3:
            self.falta = int(input("Numero de faltas: " ))
            falta1 = self.falta + 1
        else:
            self.falta = input("Numero de faltas: ")
            print(self.falta)

    def promedio (self):
        self.promedio = int(((self.falta1 * 100) / self.clases))

    def resultado (self):
        if self.promedio >= 80:
            print("{} tiene derecho a presentar examen" .format(self.alumno))
        else:
            print("{} no tiene derecho a presentar examen" .format(self.alumno))
            
    def bucle (self):
        bucle = str(input("Otra evaluación (s/n): "))

evaluacion = Examen

evaluacion.materias()
evaluacion.alumnos()
evaluacion.clase()
evaluacion.retardo()
evaluacion.falta()
evaluacion.promedio()
evaluacion.resultado()
evalucion.bucle()