import re
from downloader.utils_wrapper import *

class WikiFicha(object):

    def __init__(self, nombre):

        #Basic Information (correspondiente con la mini ficha antes de la carrera)
        self. nombre = nombre
        self.nombre_normalized = self.string_normalization(nombre)
        self.imagen_principal = ""
        self.nombres_alternativos = {} #keys serian los diferentes sitios, como Japón, China, etc.
        self.nombres_alternativos_normalized = {}
        self.origen = ""
        self.origen_normalized = ""
        self.num_integrantes= {} #Activos e inactivos serian las keys
        self.num_integrantes_normalized = {}
        self.debut = "" #datetime
        self.debut_normalized = {}
        self.fandom = ""
        self.fandom_normalized = ""
        self.agencia = ""
        self.agencia_normalized = ""
        self.subunidades = []
        self.subunidades_normalized = []
        self.solistas = []
        self.solistas_normalized = []

    @staticmethod
    def string_normalization(cadena):
        return elimina_tildes(cadena).lower()

    def setInfo(self, parseado):

        self._setBasicInfo(parseado)

    def _setBasicInfo(self, parseado):

        #imagen_principal bloque

        imagen_obtenida = self.get_imagen_principal(parseado, self.nombre)
        self.imagen_principal = imagen_obtenida if imagen_obtenida != self.imagen_principal else self.imagen_principal

    #Métodos de clase específicos para extraer los datos básicos
    @classmethod
    def get_imagen_principal(cls, parseado, nombre):

        imagen = parseado.find('a', class_="image")
        for img in imagen:
            if nombre.lower() in str(img).lower():
                img_class = img.find('img')
                if img_class is not None:
                    img_src = img_class['src']
                    url_withoutscale_match = re.match("(.+\/)scale-to-width-down\/\d+(\?cb=.+)", img_src)
                    try:
                        url_withoutscale = url_withoutscale_match.group(1) + url_withoutscale_match.group(2)
                    except AttributeError:
                        print("Ha fallado el parseado de la dirección de la imagen. La url es {0}".format(img_src))
                        sys.exit()

                    clean_url = url_withoutscale.replace("amp;", "")

        return clean_url

    @classmethod
    def extrae_nombres_alternativos(cls, lista_frases):
        pass
        #TODO HAY QUE IMPLEMENTAR EL DICCIONARIO DEL TIPO QUE DETECTE SI ES JAPON, CHINA, COREA O INTERNACIONAL, OKIS?
        #TODO TAMBIEN QUE HACER EL PARSEADO. SEPARAR MEDIANTE "EN" EN LOS QUE TIENEN NACIONALIDAD ASIATICA Y QUEDARSE CON LO QUE VA ANTES DEL PARENTESIS. EN EL INTERNACIONAL EL FORMATO ES MAS FACIL