import re
import sys
import unicodedata

def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def contiene_nacionalidad(frase):

    frase = elimina_tildes(frase.lower())

    if "japon" in frase:
        return

    return "japon" in frase or "internacional" in frase or "china" in frase or "corea" in frase
