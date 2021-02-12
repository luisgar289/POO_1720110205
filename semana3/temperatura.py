class Temperatura():

    def __init__(self):
        pass

    contador = 0

    def proceso (self):

        pregunta = int(input("Numero de Temperaturas: "))

        contador = 0
        suma = 0

        for proceso in range(pregunta):

            contador += 1
            celcius = int(input("Temperatura {} en celcius: ".format(contador)))
            farenheit = float(celcius * 1.8 + 32)
            suma += farenheit

        promedio = suma / pregunta
        print("Promedio en Farenheit: {}°F" .format(round (promedio,2)))

calculo = Temperatura()
calculo.proceso()
     
    