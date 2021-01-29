class Banco ():

    '''
    Atributos
    '''

    color = None
    decoracion = None
    empleados = None
    uniforme = None
    piso = None
    dispositivos = None
    marca = None
    seguridad = None
    puertas = None
    ventanas = None

    def __init__ (self):
        print("Clase Banco")

    '''
    Metodos
    '''

    def depositar (self):
        print("Metodo Depositar")
    
    def consultar (self):
        print("Metodo Consultar")
    
    def retirar (self):
        print("Metodo Retirar")

    def tramitar (self):
        print ("Metodo retirar")
    
    def aclarar (self):
        print("Metodo Aclarar")

#Creacion del objeto

bbva = Banco()

bbva.color = "Gama de azules"
bbva.decoracion = "Plantas y colores azules"
bbva.empleados = "5"
bbva.uniforme = "Camisa y pantalon azul rey "
bbva.piso = "Si"
bbva.dispositivos = "Cajeros y computadoras"
bbva.marca = "BBVA"
bbva.seguridad = "Si"
bbva.puertas = "Si"
bbva.ventanas = "Si"

#Imprimir  atributos  

print(bbva.marca)
print(bbva.color)
print(bbva.decoracion)
print(bbva.empleados)
print(bbva.uniforme)
print(bbva.piso)
print(bbva.dispositivos)
print(bbva.seguridad)
print(bbva.puertas)
print(bbva.ventanas)

#Invocar metodos

bbva.depositar()
bbva.consultar()
bbva.retirar()
bbva.tramitar()
bbva.aclarar()