class Temperatura():

    def __init__(self):
        pass

    contador = 0

    def proceso (self):

        pregunta = int(input("¿Cuantos calculos realizaras? "))

        contador = 0

        for proceso in range(pregunta):
            contador += 1
            final = 0

            celcius = int(input("Temperatura {} en celcius: ".format(contador)))
            farenheit = celcius * 1.8 + 32
            final += farenheit
            
            if contador == pregunta:
                promedio = final / pregunta
                print(promedio)


calculo = Temperatura()
calculo.proceso()
     
    