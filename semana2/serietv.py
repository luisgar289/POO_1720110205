class SerieTV():

    actores = None
    titulo = None
    duracion= None
    capítulos= None
    trama= None
    escenarios= None
    director= None
    producción= None
    empresa= None
    categoría= None

    def __init__ (self):
        print("Clase Serie de TV")

    def entretener(self):
        print("Metodo entretener")

    def distraer (self):
        print("Metodo distraer")

    def impresionar (self):
        print("Metodo impresionar")
    def emocionar (self):
        print ("Metodo emocionar")

    def agradar (self):
        print("Metodo agradar")

euphoria = SerieTV()

euphoria.titulo = "Euphoria"
euphoria.actores = "Si"
euphoria.duracion= "Indefinido"
euphoria.capítulos= "9"
euphoria.trama= "Problema de adolescentes"
euphoria.escenarios= "Si"
euphoria.director= "Sam Levinson"
euphoria.producción= "Si"
euphoria.empresa= "HBO"
euphoria.categoría= "B15"

print(euphoria.titulo)
print(euphoria.actores)
print(euphoria.duracion)
print(euphoria.capítulos)
print(euphoria.trama)
print(euphoria.escenarios)
print(euphoria.director)
print(euphoria.producción)
print(euphoria.empresa)
print(euphoria.categoría)


euphoria.agradar()
euphoria.distraer()
euphoria.emocionar()
euphoria.entretener()
euphoria.impresionar()