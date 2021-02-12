class Segundos():

    dias = 0
    diaFinal = 0
    dia = int hora * 24

    def __init__ (self):
        pass

    def hora (self):
        hora = 60 * 60
        print("Una hora tiene ", hora)
    
    def dia (self):
        dia = int(input ("¿Cuantos segundos tiene una hora?",))
        diaFinal = dia * 24
        print("Un dia tiene: ", diaFinal)
    
    def calculo (self):
        print(diaFinal)

calculo = Segundos()
calculo.hora()
calculo.dia()
calculo.calculo()