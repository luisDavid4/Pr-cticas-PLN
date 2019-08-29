#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import nltk
from nltk.tokenize.toktok import ToktokTokenizer


def clear(): return os.system("cls")
# diccionario[linea_segmentada[1]=linea_segmentada[0]]


def tokenizacion(ruta):
    # Tokenizador TokTok (palabras)
    toktok = ToktokTokenizer()
    # Tokenizador de oraciones
    es_tokenizador_oraciones = nltk.data.load(
        'tokenizers/punkt/spanish.pickle')
    # Obtener oraciones de un texto
    texto = ""
    # with open(ruta, "w") as fp:
    "C:\Users\David\Documents\Repositorios\Practicas-PLN\3_Practica03\recursos\practica3.txt"
    with open("recursos"+os.path.sep+"practica3.txt", "w") as fp:
        texto = fp.read()
    oraciones = es_tokenizador_oraciones.tokenize(texto)
    # Obtener tokens de cada oración
    for s in oraciones:
        print([t for t in toktok.tokenize(s)])


def main():
    mensaje = ""
    ruta = input(f"Ingrese la ruta: ")
    tokenizacion(ruta)
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
        reiniciar = input(f"\n¿Desea reiniciar (s/n)? ")
