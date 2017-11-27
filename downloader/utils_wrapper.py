import re
import sys

def get_imagen_principal(parseado, nombre):

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

# holi = "Origen: Corea del Sur."
# print(re.match("(\w+)\:\s.+", holi).group(1))