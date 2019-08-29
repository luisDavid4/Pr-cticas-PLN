#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random


def clear(): return os.system("cls")


def distHamming(palabra1, palabra2):
    distancia = 0
    longitud = len(palabra1)
    if longitud != len(palabra2):
        distancia = -1
    else:
        for i in range(longitud):
            if palabra1[i] != palabra2[i]:
                distancia += 1
    return distancia


def main():
    mensaje = ""
    p1 = input(f"Ingrese una palabra: ")
    p2 = input(f"Ingrese otra palabra: ")
    distancia = distHamming(p1, p2)
    mensaje = f"La distancia de Hamming entre las palabras es: {distancia}."
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
