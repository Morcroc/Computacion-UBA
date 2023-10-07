# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:23:58 2023

@author: velas
"""

import random


def cuantas_figus(figus_total):
    album = [0] * figus_total
    contador = 0
    while sum(album) < figus_total:
        figu = random.randint(0, figus_total -1)
        contador += 1
        album[figu] = 1
    return contador

def promedio_cuantas_figus(figus_total, n_rep):
    resultados = []
    for i in range(0, n_rep):
        resultados.append(cuantas_figus(figus_total))
        
    return sum(resultados)/n_rep

def cantidad_figus_esperada(figus_total):
    cantidad = 0
    for i in range(0, figus_total):
        cantidad += figus_total/(figus_total - i)
    return cantidad

def dame_chance(resultados, cantidad_maxima):
    contador = 0
    for i in range(0, len(resultados)):
        if(resultados[i] <= cantidad_maxima):
            contador += 1
    return contador/len(resultados)

def simular_chance(figus_total, cantidad_max, n_rep):
    contador = 0
    for i in range(0, n_rep):
        figus = cuantas_figus(figus_total)
        if(figus <= cantidad_max):
            contador += 1
    
    return contador/n_rep