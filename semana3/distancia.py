import math

class DistanciaPuntos():

    X1= None
    Y1 = None
    X2 = None
    Y2 = None

    def __init__ (self):
        pass
    def operacion(self, X1, X2, Y1, Y2):
        resultado_1 = X2-X1
        elevacion1 = resultado_1**2
        resultado_2 = Y2-Y1
        elevacion2 = resultado_2**2
        resultado3 = elevacion1+elevacion2
        final= math.sqrt(resultado3)
        print("La distancia de un punto a otro es ",final)
 
punto = DistanciaPuntos()

punto.operacion(3.17,4.99,4.78,7.88)
punto.operacion(7.15,1.93,21.6,4.38)
punto.operacion(12.17,10.4,10.4,29.3)
punto.operacion(39.4,68.3,78.9,187.2)
punto.operacion(88.7,295.3,118.3,18.4)
