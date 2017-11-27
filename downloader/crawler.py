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

                            print()

                           # titulo_seccion = re.match("(w+)\:[\s.+|\s\n.+|\s.+.]", li.text)

                           # print([li.text])
                           # titulo_seccion = re.match("(\w+|.+)\:[\s[\n.+|.+]|\n[\n.+|.+]]]", li.text)
                           # try:
                           #     print(titulo_seccion.groups())
                           # except AttributeError:
                           #     print("El nombre de la sección de la ficha de información básica no está bien parseado."
                           #           "La cadena es: {0}".format(li.text))
                        print(li.text)
                        # print('ul de lis')
                        # print(li.find_all('ul'))



crawler = Crawler(queue=["http://es.drama.wikia.com/wiki/Gugudan"])
crawler.start()





