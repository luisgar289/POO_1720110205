class Examen():
  
    materia = None
    alumno = None
    clases = 0
    retardos = 0
    falta = 0
    falta1 = 0
    promedio = 0
    bucle = None

    def __init__(self):
        pass

    def materia (self):
        self.materia = input("Materia: ")
           
    def alumno(self):
        self.alumno = input("Nombre del alumno: ")

    def clase(self):
        self.clases = int(input("Numero de clases: "))
            
    def retardo(self):
        self.retardos = int(input("Numero de retardos: "))
            
    def falta (self):
        if self.retardos == 3:
            self.falta = int(input("Numero de faltas: " ))
            falta1 = self.falta + 1
        else:
            self.falta = int(input("Numero de faltas: "))

    def promedio (self):
        self.promedio = self.falta1 * 100 / self.clases

    def resultado (self):
        if 80 >= self.promedio:
            print("{} tiene derecho a presentar examen" .format(self.alumno))
        else:
            print("{} no tiene derecho a presentar examen" .format(self.alumno))
            
        bucle = str(input("Otra evaluación (s/n): "))

evaluacion = Examen()

evaluacion.materia()
evaluacion.alumno()
evaluacion.clase()
evaluacion.retardo()
evaluacion.falta()
evaluacion.promedio()
evaluacion.resultado()