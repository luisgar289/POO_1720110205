class Temperatura():

    def __init__(self):
        pass

    contador = 0

    def proceso (self):

        pregunta = int(input("¿Cuantos calculos realizaras? "))

        contador = 0

        for proceso in range(pregunta):
            contador += 1
            suma = 0

            celcius = int(input("Temperatura {} en celcius: ".format(contador)))
            farenheit = celcius * 1.8 + 32
            print(farenheit)
            suma += farenheit
            
            if contador == pregunta:
                promedio = suma / contador # arreglar esta parte
                print(promedio)


calculo = Temperatura()
calculo.proceso()
     
    