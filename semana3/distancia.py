import math

class DistanciaPuntos():

    X1= None
    Y1 = None
    X2 = None
    Y2 = None

    def __init__ (self):
        pass
    def operacion_1(self, X1, X2, Y1, Y2):
        resultado_1 = X2-X1
        elevacion1 = resultado_1**2
        resultado_2 = Y2-Y1
        elevacion2 = resultado_2**2
        resultado3 = elevacion1+elevacion2
        final= math.sqrt(resultado3)
        print(final)
 
punto = DistanciaPuntos()
punto.X1=3.17
punto.Y1=4.78
punto.X2= 4.99
punto.Y2 = 7.88

punto.operacion_1(3.17,4.99,4.78,7.88)


