class Cajero():

    material= None
    energia= None
    pantalla= None
    modelo= None
    funciones= None
    luces= None
    marca= None
    tamanno= None
    velocidad= None
    software= None


    def __init__(self):
        print("Clase Cajero Automatico")

    def retirar (self):
        print("Metodo retirar")

    def consultar (self):
        print("Metodo retirar")

    def mostrar (self):
        print("Metodo mostrar")

    def contar (self):
        print("Metodo contar")

    def leer (self):
        print("Metodo leer")

cajero = Cajero()

cajero.material="Metal"
cajero.energia="Electrica"
cajero.pantalla="Si"
cajero.modelo="2018"
cajero.funciones="Si"
cajero.luces="Si"
cajero.marca="BBVA"
cajero.tamanno="Grande"
cajero.velocidad="Alta"
cajero.software="BBVA"

print(cajero.material)
print(cajero.energia)
print(cajero.pantalla)
print(cajero.modelo)
print(cajero.funciones)
print(cajero.luces)
print(cajero.marca)
print(cajero.tamanno)
print(cajero.velocidad)
print(cajero.software)


cajero.retirar()
cajero.consultar()
cajero.mostrar()
cajero.contar()
cajero.leer()