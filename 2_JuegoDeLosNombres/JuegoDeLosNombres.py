#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random


def clear(): return os.system("cls")


class Agente:
    def __init__(self, m):  # m=el número total de objetos en el contexto
        self.nombresObjetos = [[] for i in range(m)]

    def nombrar(self):
        nombre = ""
        longitud = random.randrange(1, 9)  # valores entre [x,y)
        consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                       'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        vocales = ['a', 'e', 'i', 'o', 'u']
        for i in range(longitud):
            nombre += f"{random.choice(consonantes)}{random.choice(vocales)}"
        return nombre

    def enunciar(self, k, oyente):  # k=número de objeto, a=agente oyente
        exito = False
        nombreCorto = ""
        for nombre in self.nombresObjetos[k]:
            if nombreCorto == "" or len(nombre) < len(nombreCorto):
                nombreCorto = nombre
        if nombreCorto == "":
            nombreCorto = self.nombrar()
            self.nombresObjetos[k].append(nombreCorto)
        # Comunicar el nombre corto al oyente:
        if nombreCorto in oyente.nombresObjetos[k]:
            exito = True
            self.nombresObjetos[k] = [nombreCorto]
            oyente.nombresObjetos[k] = [nombreCorto]
        else:
            oyente.nombresObjetos[k].append(nombreCorto)
        return exito


class Objeto:
    nombre = ""


def imprimirMetricas(agentes, t):
    soloUnNombrePorObj = True
    numObjetos = len(agentes[0].nombresObjetos)
    numNombresConocidos = 0
    numNombresCadaObjeto = ""
    longMediaNombres = 0  # en número de letras
    todosNombres = []
    listaNombresCadaObjeto = [[] for i in range(numObjetos)]
    # Obtención de todos los nombres
    for agente in agentes:
        for i in range(numObjetos):
            for nombreObjeto in agente.nombresObjetos[i]:
                listaNombresCadaObjeto[i].append(nombreObjeto)
                todosNombres.append(nombreObjeto)
    # Preparación de mensajes:
    for i in range(numObjetos):
        listaNombresCadaObjeto[i] = list(dict.fromkeys(
            listaNombresCadaObjeto[i]))  # quitar duplicados
        cantidadNombres = len(listaNombresCadaObjeto[i])
        numNombresCadaObjeto += f"Obj{i+1}={cantidadNombres} "
        if cantidadNombres != 1:
            soloUnNombrePorObj = False
    todosNombres = list(dict.fromkeys(todosNombres))  # quitar duplicados
    numNombresConocidos = len(todosNombres)
    sumaLetras = 0
    for nombre in todosNombres:
        sumaLetras += len(nombre)
    longMediaNombres = sumaLetras/numNombresConocidos
    print(f"\nNúmero total de nombres conocidos: {numNombresConocidos}")
    print(f"Número total de nombres para cada objeto: {numNombresCadaObjeto}")
    print(
        f"Longitud promedio de todos los nombres: {'%.1f'%(longMediaNombres)} letras")
    print(f"Número de iteración: {t}")
    return soloUnNombrePorObj


def esEstable(agentes):
    estable = True
    numObjetos = len(agentes[0].nombresObjetos)
    for i in range(numObjetos):
        for agente in agentes:
            # verificar que cada agente tenga solo 1 nombre para cada objeto
            if len(agente.nombresObjetos[i]) != 1\
                    or len(agentes[0].nombresObjetos[i]) != 1:
                estable = False
            elif agente.nombresObjetos[i][0] != agentes[0].nombresObjetos[i][0]:
                estable = False
    return estable


def main():
    mensaje = ""
    n = int(input(f"Ingrese el número de agentes (n): "))
    m = int(input(f"Ingrese el número de objetos (m): "))
    max_t = int(input(f"Ingrese el número de iteraciones máximas (max_t): "))
    t = 0  # número de iteración
    listaAgentes = []
    listaObjetos = []
    for i in range(n):
        listaAgentes.append(Agente(m))
    for i in range(m):
        listaObjetos.append(Objeto())
    vocabularioEstable = False
    while t < max_t and not vocabularioEstable:
        t += 1
        hablante = random.choice(listaAgentes)
        oyente = random.choice(listaAgentes)
        while hablante == oyente:
            oyente = random.choice(listaAgentes)
        objAleatorio = random.randrange(0, m)  # valores entre [x,y)
        hablante.enunciar(objAleatorio, oyente)
        if imprimirMetricas(listaAgentes, t):
            vocabularioEstable = esEstable(listaAgentes)
    if vocabularioEstable:
        mensaje = "\n\tNombre final de cada objeto:\n"
        for i in range(m):
            listaObjetos[i].nombre = listaAgentes[0].nombresObjetos[i][0]
            mensaje += f"Obj{i+1} = {listaObjetos[i].nombre}\n"
    else:
        mensaje = f"\n\tEn la iteración máxima no se obtuvo el vocabulario estable.\n"
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
