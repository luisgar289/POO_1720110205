class Estudiante():

    cabello = None
    uniforme = None
    grado= None
    edad = None
    escuela = None
    zapatos = None
    materias = None
    sexo = None
    actitud = None
    valores = None

    def __init__ (self):
        print("Clase Estudiante")

    def estudiar (self):
        print ("Metodo estudiar")

    def participar (self):
        print ("Metodo participar")

    def aprender (self):
        print("Metodo aprender")

    def memorizar (self):
        print("Metodo memorizar")

    def exponer (self):
        print ("Metodo exponer")

luis = Estudiante()

luis.cabello = "Cafe"
luis.uniforme="No"
luis.grado = "2do cuatrimestre"
luis.edad = "18 años"
luis.escuela = "UTEC Tulancingo"
luis.zapatos = "Si"
luis.materias ="8"
luis.sexo = "Masculino"
luis.actitud ="Positiva"
luis.valores ="Si"

print(luis.uniforme)
print(luis.grado)
print(luis.edad)
print(luis.escuela)
print(luis.zapatos)
print(luis.materias)
print(luis.sexo)
print(luis.actitud)
print(luis.valores)

luis.estudiar()
luis.participar()
luis.aprender()
luis.memorizar()
luis.exponer()
