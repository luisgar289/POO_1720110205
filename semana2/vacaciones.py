class Vacaciones ():

    lugar = None
    transporte = None
    actividades = None
    tiempo = None
    paisajes = None
    comida = None
    ropa = None
    bebidas = None
    personas = None
    hotel = None

    def __init__ (self):
        print ("Clase Vacaciones")

    def disfrutar (self):
        print ("Metodo disfrutar")
    
    def conocer (self):
        print("Metodo conocer")

    def descansar (self):
        print ("Metodo descansar")

    def despejar (self):
        print ("Metodo despejar")

    def viajar (self):
        print("Metodo viajar")

acapulco = Vacaciones()

acapulco.lugar = "Acapulco"
acapulco.transporte = "Avion"
acapulco.actividades = "Visitar playa"
acapulco.tiempo = "Indefinido"
acapulco.paisajes ="Mar y atardeceres"
acapulco.comida = "Mariscos"
acapulco.ropa ="Traje de baño"
acapulco.bebidas = "Agua de coco"
acapulco.personas = "5"
acapulco.hotel = "Si"

print(acapulco.lugar)
print(acapulco.transporte)
print(acapulco.actividades)
print(acapulco.tiempo)
print(acapulco.paisajes)
print(acapulco.comida)
print(acapulco.ropa)
print(acapulco.bebidas)
print(acapulco.personas)
print(acapulco.hotel)

acapulco.disfrutar()
acapulco.conocer()
acapulco.descansar()
acapulco.despejar()
acapulco.viajar()