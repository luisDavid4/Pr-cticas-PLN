#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import operator
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
    with open("recursos/practica3.txt", "r", encoding="utf8") as fp:
        # with open(ruta, "r", encoding="utf8") as fp:
        texto = fp.read()
    oraciones = es_tokenizador_oraciones.tokenize(texto)
    # Obtener tokens de cada oración
    tokens = []
    for s in oraciones:
        # tokens.append([t for t in toktok.tokenize(s)])
        tokens += ([t for t in toktok.tokenize(s)])
    return tokens


def distribucionFrecuencias(tokens):
    frecuencias = {}
    # Sacar elementos unicos
    # myset = set(tokens)
    # tokensUnicos = list(myset)
    tokensUnicos = set(tokens)
    print(tokens)
    print(len(tokens))
    print(tokensUnicos)
    print(len(tokensUnicos))
    for token in tokensUnicos:
        print(f"{token} {str(tokens.count(token))}")
        frecuencias[token] = tokens.count(token)
    print(frecuencias)
    ordenado = sorted(frecuencias.items(), key=operator.itemgetter(1))
    ordenado.reverse()
    print(ordenado)


def main():
    mensaje = ""
    # ruta = input(f"Ingrese la ruta: ")
    tokens = tokenizacion("ruta")
    distribucionFrecuencias(tokens)

    # print(tokensUnicos)
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
