class Segundos():

    dias = 0
    segundosDia = 0
    final = 0

    def __init__ (self):
        pass

    def entrada (self):
        self.dias = input("Dias: ")
    
    def dia (self):
        self.segundosDia = 3600 * 24

    def operacion(self):
        self.final = calculo.entrada() * calculo.dia()
        print("Segundos: " , )
    
calculo = Segundos()
calculo.entrada()
calculo.dia()
