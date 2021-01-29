class Futbolista():

    uniforme = None
    altura = None
    equipo = None
    edad = None
    velocidad = None
    resistencia = None
    cara = None
    cabello = None
    nacionalidad = None
    rendimiento = None

    def __init__(self):
        print("Clase Futbolista")

    def patear (self):
        print("Metodo patear")

    def correr (self):
        print("Metodo correr")

    def celebrar (self):
        print("Metodo print")

    def caminar (self):
        print("Metodo caminar")

    def ganar (self):
        print("Metodo meter gol")

cr7 = Futbolista()

cr7.uniforme = "Si"
cr7.altura = "1,87"
cr7.equipo = "Juventus"
cr7.edad = "35"
cr7.velocidad = "33,12 km"
cr7.resistencia = "Si"
cr7.cara = "Si"
cr7.cabello = "Si"
cr7.nacionalidad = "Portuguesa"
cr7.rendimiento = "Si"

print(cr7.uniforme)
print(cr7.altura)
print(cr7.edad)
print(cr7.equipo)
print(cr7.velocidad)
print(cr7.resistencia)
print(cr7.cara)
print(cr7.cabello)
print(cr7.nacionalidad)
print(cr7.rendimiento)


cr7.caminar()
cr7.celebrar()
cr7.correr()
cr7.ganar()
cr7.patear()