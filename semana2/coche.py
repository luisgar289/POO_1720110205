class Coche():

    motor = None
    color = None
    modelo = None
    anno = None
    kilometraje = None
    velocidad = None
    llantas = None
    quemacocos = None
    marca = None
    ventana = None

    def __init__(self):
        print("Clase Coche")

    def transportar (self):
        print("Metodo transportar")

    def girar (self):
        print("Metodo girar")

    def acelerar (self):
        print("Metodo acelerar")

    def encender (self):
        print("Metodo encender")

    def apagar (self):
        print("Metodo apagar")

ferrari = Coche()

ferrari.marca = "Ferrari"
ferrari.motor = "Ferrari 052 3.0 V10"
ferrari.color = "Rojo"
ferrari.modelo = "f2003 GA"
ferrari.anno = "2003" 
ferrari.kilometraje = "2500"
ferrari.velocidad = "2.445 kmh"
ferrari.llantas = "2"
ferrari.quemacocos = "No"
ferrari.ventana = "No"

print(ferrari.marca)
print(ferrari.motor)
print(ferrari.color)
print(ferrari.modelo)
print(ferrari.anno)
print(ferrari.kilometraje)
print(ferrari.velocidad)
print(ferrari.llantas)
print(ferrari.quemacocos)
print(ferrari.ventana)

ferrari.acelerar()
ferrari.apagar()
ferrari.encender()
ferrari.girar()
ferrari.transportar()