class Segundos():
    # Un minuto tiene 60 segundos
    # Una hora tiene 3600 segundos
    # Un dia tiene 86400

    dia = 0

    def __init__ (self):
        pass

    def calculo (self):
        dia = int(input("Dias: "))
        final = 86400 * dia
        print("En ", dia , " hay ", final , " segundos")

calculo = Segundos()

calculo.calculo()