#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import operator
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


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
    with open(ruta, "r", encoding="utf8") as fp:
        texto = fp.read()
    oraciones = es_tokenizador_oraciones.tokenize(texto)
    # Obtener tokens de cada oración
    tokens = []
    for s in oraciones:
        # tokens.append([t for t in toktok.tokenize(s)])
        tokens += ([t for t in toktok.tokenize(s)])
    return tokens


def elementosUnicos(tokens):
    # Sacar elementos unicos
    # myset = set(tokens)
    # tokensUnicos = list(myset)
    tokensUnicos = set(tokens)
    return tokensUnicos


def distribucionFrecuencias(tokensUnicos, tokens):
    frecuencias = {}
    for token in tokensUnicos:
        # print(f"{token} {str(tokens.count(token))}")
        frecuencias[token] = tokens.count(token)
    # print(frecuencias)
    # Ordenar decrecientemente segun el numero de repeticiones
    frecOrdenadas = sorted(frecuencias.items(),
                           key=operator.itemgetter(1), reverse=True)
    print(frecOrdenadas)
    return frecOrdenadas


def reduccionDimensionalidad(listaUnicos, esListaPares):
    sinPalabrasFuncionales = []
    # Quitar las palabras funcionales de la lista
    if esListaPares:  # verificar si es lista de pares
        sinPalabrasFuncionales = [x for x in listaUnicos
                                  if x[0] not in stopwords.words("spanish")]
    else:
        sinPalabrasFuncionales = [x for x in listaUnicos
                                  if x not in stopwords.words("spanish")]
    # print(stopwords.words("spanish"))
    return sinPalabrasFuncionales


def distribucionFrecuenciasStemming(tokensReducidos):
    # Stemmer spanish
    stemmer = SnowballStemmer("spanish")
    tokensStem = []
    for t in tokensReducidos:
        tokensStem.append(stemmer.stem(t))  # Obtener la raiz
    tokensStemUnicos = elementosUnicos(tokensStem)
    frecuencias = {}
    for token in tokensStemUnicos:
        frecuencias[token] = tokensStem.count(token)
    # Ordenar decrecientemente segun el numero de repeticiones
    frecOrdenadas = sorted(frecuencias.items(),
                           key=operator.itemgetter(1), reverse=True)
    print(frecOrdenadas)
    return frecOrdenadas


def distribucionFrecuenciasLematizacionIngenua(tokensReducidos):
    lineas = []
    with open("recursos\lemmatization-es.txt", "r", encoding="utf8") as fp:
        lineas = fp.readlines()
    # for t in tokensReducidos:
    #     tokensStem.append(stemmer.stem(t))  # Obtener la raiz
    # tokensStemUnicos = elementosUnicos(tokensStem)
    # frecuencias = {}
    # for token in tokensStemUnicos:
    #     frecuencias[token] = tokensStem.count(token)
    # # Ordenar decrecientemente segun el numero de repeticiones
    # frecOrdenadas = sorted(frecuencias.items(),
    #                        key=operator.itemgetter(1), reverse=True)
    # print(frecOrdenadas)
    # return frecOrdenadas
    return None


def main():
    mensaje = ""
    # ruta = input(f"Ingrese la ruta: ")
    tokens = tokenizacion("recursos/practica3bo.txt")
    tokensUnicos = elementosUnicos(tokens)
    tokensConfrecuencias = distribucionFrecuencias(tokensUnicos, tokens)
    reducidos = reduccionDimensionalidad(tokensUnicos, False)
    tokensStemConfrecuencias = distribucionFrecuenciasStemming(reducidos)
    tokensLemaConfrecuencias = distribucionFrecuenciasLematizacionIngenua(
        reducidos)
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
