class Avion():

    motor = None
    color  = None
    ventanas  = None
    anno  = None
    marca  = None
    empresa  = None
    velocidad  = None
    asientos  = None
    trendeaterrizaje  = None
    llantas  = None

    def volar (self):
        print("Metodo volar")
    
    def transportar (self):
        print("Metodo transportar")

    def despegar (self):
        print("Metodo despegar")

    def aterrizar (self):
        print("Metodo aterrizar")

    def girar (self):
        print("Metodo girar")

avion = Avion()

avion.motor ="Si"
avion.color ="Blanco"
avion.ventanas="16"
avion.anno="2000"
avion.marca ="Boeing"
avion.empresa = "No"
avion.velocidad = "933 kmph"
avion.asientos= "Si"
avion.trendeaterrizaje ="Si"
avion.llantas="2"

print(avion.motor)
print(avion.color)
print(avion.ventanas)
print(avion.anno)
print(avion.marca)
print(avion.empresa)
print(avion.velocidad)
print(avion.asientos)
print(avion.trendeaterrizaje)
print(avion.llantas)

avion.volar()
avion.aterrizar()
avion.transportar()
avion.despegar()
avion.girar()
