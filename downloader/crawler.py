from bs4 import BeautifulSoup
import re
from downloader.wrapper import WikiFicha

class Crawler(object):

    def __init__(self, queue=[], interval=5):

        self.queue = queue
        self.interval = interval * 60
        self.base = "http://es.drama.wikia.com/wiki/"

    def _downloadurl(self, url):

        import urllib.request

        page = urllib.request.urlopen(url)
        html = page.read()

        return html

    def _urlrules(self, url):

        comienzawiki = bool(re.search('\/wiki\/.+', url))

        return comienzawiki

    def start(self):

        for url in self.queue:

            downloaded_content = self._downloadurl(url)
            #soup = BeautifulSoup(downloaded_content, parseOnlyThese=SoupStrainer('a'))
            soup = BeautifulSoup(downloaded_content, 'html.parser')

            titulo = soup.find('h1', class_="page-header__title").text

            wiki_object = WikiFicha(titulo)
            # wiki_object.setInfo(soup)

            holi = soup.find_all('h2')
            for h in holi:
                if titulo.lower() == h.text.lower():
                    macrotextoficha = h.find_next_sibling()
                    for li in macrotextoficha.find_all('li'):
                        if li.find('ul'):
                            print("con ul")
                            print([li.text])

                           # titulo_seccion = re.match("(w+)\:[\s.+|\s\n.+|\s.+.]", li.text)
                            titulo_seccion_match = re.match("(\w+|.+)\:[\s[\n.+|.+]|\n[\n.+|.+]]]", li.text)
                            try:
                                titulo_seccion = titulo_seccion_match.group(1)

                                #Casuistica para ver de cual de las secciones se trata
                                if titulo_seccion.lower() == "nombre":
                                    #TODO PONER LA FUNCION DE EXTRAE_NOMBRES_ALTERNATIVOS ABAJO, AUNQUE HABRA QUE MOVERLA A UTIL PARA QUE TE DEJE DE PRUEBA
                                    nombres_alternativos = [for frase in li.text.split("\n") if contiene_nacionalidad(frase)]
                                print(titulo_seccion)
                                # titulo_seccion = titulo_seccion.group(0)
                            except AttributeError:
                                print("El nombre de la sección de la ficha de información básica no está bien parseado."
                                     "La cadena es: {0}".format(li.text))
                        else:
                            print("sin ul")
                            print([li.text])
                        # print('ul de lis')
                        # print(li.find_all('ul'))



crawler = Crawler(queue=["http://es.drama.wikia.com/wiki/Gugudan"])
crawler.start()





