#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 18:04:24 2023

@author: clinux01
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import imageio
import os

capacidad_max = 10
capacidad_min = 3

def armar_matriz(n):
    tablero = np.repeat(0, n*n)
    tablero = tablero.reshape(n, n)
    return tablero

def definir_bordes(tablero):
    n_filas, n_columnas = tablero.shape
    for i in range(0, n_filas):
        tablero[(i, 0)] = -1
        tablero[(i, n_columnas - 1)] = -1
    for j in range(0, n_columnas):
        tablero[(n_filas - 1 , j)] = -1
        tablero[(0, j)] = -1
    return tablero

def crear_tablero(n):
    tablero = armar_matriz(n + 2)
    tablero = definir_bordes(tablero)
    return tablero

def es_borde(tablero, coord):
    return tablero[(coord)] == -1

def tirar_copo(tablero):
    filas, columnas = tablero.shape
    random_coord = (random.randint(1, filas-2), random.randint(1, columnas-2))
    tablero[(random_coord)] += 1
    return tablero

def vecinos_de(tablero, coord):
    vecinos = []
    j, k = coord
    for i in range(-1, 2, 2):
        if(not es_borde(tablero, (j+i, k))):
            vecinos.append((j+i, k))
        if(not es_borde(tablero, (j, k+i))):
            vecinos.append((j, k+i))
    return vecinos

def desbordar_posicion(tablero, paralelo, coord):
    if(tablero[coord] >= paralelo[coord]):
        #desborde = random.randint(1, tablero[coord])
        #tablero[coord] -= desborde
        vecinos = vecinos_de(tablero, coord)
        for i in range(0, len(vecinos)):
            tablero[vecinos[i]] += 1
            
        tablero[coord] -= min(4, paralelo[coord])
    return tablero

def desbordar_valle(tablero, paralelo):
    filas, columnas = tablero.shape
    for i in range(1, filas -1):
        for j in range(1, columnas - 1):
            desbordar_posicion(tablero, paralelo, (i, j))
    return tablero

def hay_que_desbordar(tablero, paralelo):
    filas, columnas = tablero.shape
    for i in range(1, filas -1):
        for j in range(1, columnas-1):
            if(tablero[(i, j)] >= paralelo[(i, j)]):
                return True
    return False

def estabilizar(tablero, paralelo):
    while(hay_que_desbordar(tablero, paralelo)):
        tablero = desbordar_valle(tablero, paralelo)
    return tablero

def paso(tablero, paralelo):
    tablero =tirar_copo(tablero)
    tablero = estabilizar(tablero, paralelo)
    return tablero

def crear_tablero_aleatorio(n, cant_copos, paralelo):
    tablero = crear_tablero(n)
    for i in range(0, cant_copos):
        tablero = paso(tablero, paralelo)
    return tablero

def crear_paralelo(n, minimo, maximo):
    paralelo = crear_tablero(n)
    filas, columnas = paralelo.shape
    for i in range(1, filas-1):
        for j in range(1, columnas-1):
            paralelo[i, j] = random.randint(minimo, maximo)
    return paralelo

def simular(n_valle, simulaciones, cant_copos, minimo, maximo):
    paralelo = crear_paralelo(n_valle, minimo, maximo)
    tablero = crear_tablero_aleatorio(n_valle, cant_copos, paralelo)
    print(paralelo)
    print(tablero)
    for i in range(0, simulaciones):
        tablero = paso(tablero, paralelo)
    return tablero

def guardar_foto(t, paso):
    dir_name = "output"
    if not os.path.exists(dir_name): # me fijo si no existe el directorio
        os.mkdir(dir_name) #si no existe lo creo
        
    ax = plt.gca()
    file_name = os.path.join(dir_name, "out{:05}.png".format(paso))
    plt.imshow(t, vmin=-1, vmax=7)
    ax.set_title("Copos tirados: {}".format(paso+1)) #titulo
    plt.savefig(file_name)
    
def hacer_video(cant_fotos):
    dir_name = "output"
    lista_fotos=[]
    for i in range (cant_fotos):
        file_name = os.path.join(dir_name, "out{:05}.png".format(i))
        lista_fotos.append(imageio.imread(file_name))
        
    video_name = os.path.join(dir_name, "avalancha.mp4")
    # genero el video con 10 Copos por segundo. Explorar otros valores:
    imageio.mimsave(video_name, lista_fotos, fps=10)
    print('Estamos trabajando en el directorio', os.getcwd())
    print('y se guardo el video:', video_name)
    
def probar(n, pasos, cant_copos, minimo, maximo):
    p = crear_paralelo(n, minimo, maximo)
    t = crear_tablero_aleatorio(n, cant_copos, p)
    for i in range(pasos):
        paso(t, p)
        guardar_foto(t, i)
    hacer_video(pasos)
    return t