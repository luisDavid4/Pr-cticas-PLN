#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random


def clear(): return os.system("cls")


class Ahorcado:
    def __init__(self, p, E):
        self.p = p.lower()  # palabra a adivinar
        self.E = E  # errores máximos permitidos
        self.e = 0  # contador errores cometidos
        self.l = []  # letras encontradas

    def jugar(self, c):
        cMinus = c.lower()
        cAcento = ''
        cU = ''
        if cMinus == 'a' or cMinus == 'á':
            cMinus = 'a'
            cAcento = 'á'
        elif cMinus == 'e' or cMinus == 'é':
            cMinus = 'e'
            cAcento = 'é'
        elif cMinus == 'i' or cMinus == 'í':
            cMinus = 'i'
            cAcento = 'í'
        elif cMinus == 'o' or cMinus == 'ó':
            cMinus = 'o'
            cAcento = 'ó'
        elif cMinus == 'u' or cMinus == 'ú' or cMinus == 'ü':
            cMinus = 'u'
            cAcento = 'ú'
            cU = 'ü'
        atino = False
        if cMinus != '' and cMinus in self.p:
            self.l.append(cMinus)
            atino = True
        if cAcento != '' and cAcento in self.p:
            self.l.append(cAcento)
            atino = True
        if cU != '' and cU in self.p:
            self.l.append(cU)
            atino = True
        if not atino:
            self.e += 1

    def estado(self):
        edo = 0  # 0=jugando, 1=perder, 2 =ganar
        mensaje = ""
        if self.e >= self.E:
            mensaje = f"{self.p} (perdiste)"
            edo = 1
        else:
            for c in self.p:
                mensaje += f"{c} " if (c in self.l) else f"_ "
            if not "_" in mensaje:
                mensaje += f"(ganaste)"
                edo = 2
            else:
                mensaje += f"({str(self.E-self.e)} errores posibles)"
        print(f"{mensaje}\n")
        return edo


def main():
    mensaje = ""
    try:
        palabra = ""
        with open('listaPalabras.txt', 'r', encoding="utf-8") as f:
            listaPalabras = f.readlines()
            palabra = random.choice(listaPalabras)
        maxErrores = random.randrange(3, 8)  # valores entre 3 y 7
        ahorcado = Ahorcado(palabra[:-1], maxErrores)
        edo = ahorcado.estado()
        while edo == 0:
            letra = input(f"Introduzca una letra: ")
            ahorcado.jugar(letra.lower())
            edo = ahorcado.estado()
        mensaje = f"Sesión de juego finalizada."
    except Exception as e:
        mensaje = f"Error detectado: {e}"
    return mensaje


if __name__ == "__main__":
    reiniciar = 's'
    while reiniciar != 'n':
        clear()
        print(f"{main()}")
        reiniciar = input(f"\n¿Desea reiniciar (s/n)? ")
