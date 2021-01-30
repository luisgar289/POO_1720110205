class App_e_learning():

    colores= None
    botones= None
    funciones= None
    version= None
    requerimientos= None
    ventanas= None
    tipografia= None
    archivos= None
    peso= None
    conectividad= None

    def __init__(self):
        print("Clase App e-learning")

    def notificacion (self):
        print("Metodo de notificacion")

    def mostrar (self):
        print("Metodo mostrar")

    def comunicar (self):
        print("Metodo comunicar")

    def registrar (self):
        print ("Metodo registrar")

    def administrar (self):
        print("Metodo administar")

classroom = App_e_learning()

classroom.colores= "Blanco,verde,rojo y azul"
classroom.botones= "Si"
classroom.funciones= "Si"
classroom.version= "13.4"
classroom.requerimientos= "Android 6.0+"
classroom.ventanas= "Multiples"
classroom.tipografia= "Elegant"
classroom.archivos= "Todos"
classroom.peso= "20 MB"
classroom.conectividad= "Wifi o datos moviles"

print(classroom.colores)
print(classroom.botones)
print(classroom.funciones)
print(classroom.version)
print(classroom.requerimientos)
print(classroom.ventanas)
print(classroom.tipografia)
print(classroom.archivos)
print(classroom.peso)
print(classroom.conectividad)

classroom.notificacion()
classroom.mostrar()
classroom.comunicar()
classroom.registrar()
classroom.administrar()