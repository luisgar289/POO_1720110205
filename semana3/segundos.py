class Segundos():
    # Un minuto tiene 60 segundos
    # Una hora tiene 3600 segundos
    # Un dia tiene 86400

    dia = int(0)
    numeroCalculos = int(input("¿Cuantos calculos realizaras? "))

    def __init__ (self):
        pass

    def calculo (self):
    
        hora = int(60 * 60)
        print("En una hora hay ", hora , " segundos.")
        segundosDia = hora * 24
        print ("En un dia hay ", segundosDia , " segundos." )

    for calculo in range(numeroCalculos):

        dia = int(input("Dime cuantos dias quieres convertir a segundos. "))
        final = int(86400 * dia)
        if dia == 1:
            print("En ", dia ," dia hay ", final , " segundos")
        else:
            print("En ", dia ," dias hay ", final , " segundos")

calculo = Segundos()

calculo.calculo