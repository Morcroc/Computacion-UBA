#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 18:21:05 2023

@author: clinux01
"""
import numpy as np
import random
import csv
import matplotlib.pyplot as plt


def armar_matriz(filas, columnas):
    tablero = np.repeat(" ", filas*columnas)
    tablero = tablero.reshape(filas, columnas)
    return tablero

def definir_bordes(tablero):
    n_filas, n_columnas = tablero.shape
    for i in range(0, n_filas):
        tablero[(i, 0)] = "M"
        tablero[(i, n_columnas - 1)] = "M"
    for j in range(0, n_columnas):
        tablero[(n_filas - 1 , j)] = "M"
        tablero[(0, j)] = "M"
    return tablero

def crear_tablero(filas, columnas):
    tablero = armar_matriz(filas+2, columnas+2)
    tablero = definir_bordes(tablero)
    return tablero
    
def agregar_animales(tablero):
    filas = [1, 2, 2, 3, 1]
    columnas = [3, 1, 3, 1, 1]
    animal = ["A", "A", "A", "A", "L"]
    for i in range(0, len(animal)):
        tablero[(filas[i], columnas[i])] = animal[i]
    return tablero

def es_monte(tablero, coord):
    return tablero[coord] == "M"

def vecinos_de(tablero, coord):
    i, j = coord
    posibles_vecinos = [(i-1,j-1), (i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1, j), (i+1, j-1), (i, j-1)]
    vecinos = []
    for i in range(0, len(posibles_vecinos)):
        if(not es_monte(tablero, posibles_vecinos[i])):
            vecinos.append(posibles_vecinos[i])
    return vecinos

def buscar_adyacente(tablero, coord, objetivo):
    vecinos = vecinos_de(tablero, coord)
    adyacente = []
    i = 0
    while i < len(vecinos) and len(adyacente) == 0:
        if tablero[vecinos[i]] == objetivo:
            adyacente.append(vecinos[i])
        i += 1
    return adyacente
        
def mover(tablero, coord):
    if(not es_monte(tablero, coord)):        
        posicion = buscar_adyacente(tablero, coord, " ")
        if(len(posicion) != 0):
            tablero[posicion[0]] = tablero[coord]
            tablero[coord] = " "
    return tablero

def alimentar(tablero, coord):
    if(tablero[coord] == "L"):
        presa = buscar_adyacente(tablero, coord, "A")
        if(len(presa) != 0):
            tablero[presa[0]] = tablero[coord]
            tablero[coord] = " "
    return tablero

def reproducir(tablero, coord):
    #si hay un animal aca, busca un vecino que sea igual a el
    if(tablero[coord] == "A" or tablero[coord] == "L"):
        animal = tablero[coord]
        pareja = buscar_adyacente(tablero, coord, animal)
        if(len(pareja) != 0):
            posicion = buscar_adyacente(tablero, coord, " ")
            if(len(posicion) != 0):
                tablero[posicion[0]] = animal
    return tablero

def fase_mover(tablero):
    filas, columnas = tablero.shape
    for i in range(1, filas-1):
        for j in range(1, columnas-1):
            tablero = mover(tablero, (i, j))
    return tablero

def fase_alimentar(tablero):
    filas, columnas = tablero.shape
    for i in range(1, filas-1):
        for j in range(1, columnas-1):
            tablero = alimentar(tablero, (i, j))
    return tablero

def fase_reproducir(tablero):
    filas, columnas = tablero.shape
    for i in range(1, filas-1):
        for j in range(1, columnas-1):
            tablero = reproducir(tablero, (i, j))
    return tablero

def evolucionar(tablero):
    tablero = fase_alimentar(tablero)
    tablero = fase_reproducir(tablero)
    tablero = fase_mover(tablero)
    return tablero

def evolucionar_en_el_tiempo(tablero, k):
    for i in range(0, k):
        tablero = evolucionar(tablero)
    return tablero

def mezclar_celdas(tablero):
    celdas = []
    for i in range(1, tablero.shape[0]-1):
        for j in range(1, tablero.shape[1]-1):
            celdas.append((i, j))
    random.shuffle(celdas)
    return celdas

def generar_tablero_azar(filas, columnas, n_antilopes, n_leones):
    tablero = crear_tablero(filas, columnas)
    celdas = mezclar_celdas(tablero)
    while len(celdas) != 0 and n_antilopes > 0:
        tablero[celdas.pop(0)] = "A"
        n_antilopes -= 1
    while len(celdas) != 0 and n_leones > 0:
        tablero[celdas.pop(0)] = "L"
        n_leones -= 1
    return tablero

def cuantos_de_cada(tablero):
    cantidad = [0, 0]
    for i in range(1, tablero.shape[0]-1):
        for j in range(1, tablero.shape[1]-1):
            if tablero[(i, j)] == "A":
                cantidad[0] += 1
            if tablero[(i, j)] == "L":
                cantidad[1] += 1
    return cantidad
    
def registrar_evolucion(tablero, k):
    resultados = []
    for i in range(0, k):
        resultados.append(cuantos_de_cada(tablero))
        tablero = evolucionar(tablero)
    resultados.append(cuantos_de_cada(tablero))
    return resultados

def guardar_evolucion(tablero, k):
    evolucion_especies = registrar_evolucion(tablero, k)
    with open("predpres.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["antilopes", "leones"])
        csv_writer.writerows(evolucion_especies)
    return

def generar_grafico():
    valores = np.loadtxt('predpres.csv',delimiter=',',skiprows=1)
    plt.ylabel('Cantidad de Individuos')
    plt.xlabel('Ciclo')
    plt.plot(valores[:,0], label = 'antilopes')
    plt.plot(valores[:,1], label = 'leones')
    plt.legend()
    return