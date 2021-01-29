class Calculadora():
    botones = None
    pantalla = None
    memoria = None
    color = None
    marca = None
    modelo = None
    bateria = None
    tipo = None
    funciones = None
    material = None

    def __init__(self):
        print("Clase Calculadora")

    def sumar (self):
        print("Metodo sumar")

    def restar (self):
        print("Metodo restar")

    def multiplicar (self):
        print("Metodo multiplicar")

    def dividir (self):
        print("Metodo dividir")

    def resultados (self):
        print("Metodo mostrar resultados")

calculadora = Calculadora()


calculadora.botones = "Si"
calculadora.pantalla = "Si"
calculadora.memoria = "No"
calculadora.color = "Negro"
calculadora.marca = "Sharp"
calculadora.modelo = "2020"
calculadora.bateria = "Si"
calculadora.tipo = "Cientifica"
calculadora.funciones = "Si"
calculadora.material = "Plastico"

print(calculadora.botones)
print(calculadora.pantalla)
print(calculadora.memoria)
print(calculadora.color)
print(calculadora.marca)
print(calculadora.modelo)
print(calculadora.bateria)
print(calculadora.tipo)
print(calculadora.funciones)
print(calculadora.material)


calculadora.sumar()
calculadora.restar()
calculadora.multiplicar()
calculadora.dividir()
calculadora.resultados()
