import math

class DistanciaPuntos():

    x1= None
    y1 = None
    x2 = None
    y2 = None

    def __init__ (self):
        pass
    def operacion(self, x1, x2, y1, y2):
        resultado_1 = x2-x1
        elevacion_1 = resultado_1**2
        resultado_2 = y2-y1
        elevacion_2 = resultado_2**2
        resultado_3 = elevacion_1+elevacion_2
        final= math.sqrt(resultado_3)
        print("La distancia de un punto a otro es ",final)
 
punto = DistanciaPuntos()

punto.operacion(3.17,4.99,4.78,7.88)
punto.operacion(7.15,1.93,21.6,4.38)
punto.operacion(12.17,10.4,10.4,29.3)
punto.operacion(39.4,68.3,78.9,187.2)
punto.operacion(88.7,295.3,118.3,18.4)
