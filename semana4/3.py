class Examen():
    materia = None
    alumno = None
    clases = None
    retardos = None
    falta = None
    falta1 = None

    def __init__ (self):
        pass

    def materia (self):
        self.materia = input("Materia: ")
    
    def alumno (self):
        self.alumno = input("Nombre del alumno: ")

    def clase (self):
        self.clases = input("Numero de clases: ")
    
    def retardo (self):
        self.retardos = int(input("Numero de retardos: "))
    
    def clase (self):
        if self.retardos == 3:
         self.falta = int(input("Numero de faltas: " ))
         falta1 = self.falta + 1
        else:
         self.falta = input("Numero de faltas: ")
         print(self.falta)

evaluacion = Examen()

evaluacion.retardo()
evaluacion.clase()
    
