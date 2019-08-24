#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random


def clear(): return os.system("cls")


class Agente:
    def __init__(self, m):
        self.m = m  # el número total de objetos en el contexto

    def nombrar(self):
        nombre = ""
        longitud = random.randrange(1, 9)  # valores entre [x,y)
        consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                       'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        vocales = ['a', 'e', 'i', 'o', 'u']
        for i in range(longitud):
            nombre += f"{random.choice(consonantes)}{random.choice(vocales)}"
        return nombre


class Objeto:
    def __init__(self):
        nombresCandidatos = []


def main():
    tiempo = 0
    hablante = Agente(1)
    return hablante.nombrar()


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
