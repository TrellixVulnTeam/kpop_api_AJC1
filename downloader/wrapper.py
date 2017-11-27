import re
from downloader.utils_wrapper import *

class WikiFicha(object):

    def __init__(self, nombre):

        #Basic Information (correspondiente con la mini ficha antes de la carrera)
        self. nombre = nombre
        self.imagen_principal = ""
        self.nombres_alternativos = {} #keys serian los diferentes sitios, como Japón, China, etc.
        self.origen = ""
        self.num_integrantes= {} #Activos e inactivos serian las keys
        self.debut = "" #datetime
        self.fandom = ""
        self.agencia = ""
        self.subunidades = []
        self.solistas = []

    def setInfo(self, parseado):

        self._setBasicInfo(parseado)

    def _setBasicInfo(self, parseado):

        #imagen_principal bloque

        imagen_obtenida = get_imagen_principal(parseado, self.nombre)
        self.imagen_principal = imagen_obtenida if imagen_obtenida != self.imagen_principal else self.imagen_principal







