#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import operator
import nltk
from nltk.tokenize.toktok import ToktokTokenizer


def clear(): return os.system("cls")
# diccionario[linea_segmentada[1]=linea_segmentada[0]]


def busqueda(tokens, lineas):
    resumenes = []
    for linea in lineas:
        contiene = True
        for token in tokens:
            if not token in linea:
                contiene = False
        if contiene:
            resumenes.append(linea)
    return resumenes


def main():
    mensaje = ""
    palabras = input(f"Lista de palabras separadas por espacios: ")
    tokens = palabras.split()
    lineas = []
    with open("wikipedia_es_abstracts.txt", "r", encoding="utf8") as file:
        lineas = file.readlines()
    resumenes = busqueda(tokens, lineas)
    print(resumenes[0])
    return mensaje


if __name__ == "__main__":
    reiniciar = 's'
    while reiniciar != 'n':
        clear()
        # '''Comentar/Descomentar
        mensaje = main()
        '''
        try:
            mensaje = f"{main()}"
        except Exception as e:
            mensaje = f"\nError detectado: {e}"
        # '''
        print(f"{mensaje}")
        # '''Comentar/Descomentar
        reiniciar = 'n'
        '''
        reiniciar = input(f"\n¿Desea reiniciar (s/n)? ")
        # '''
