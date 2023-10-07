#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 18:50:31 2023

@author: clinux01
"""

import matplotlib.pyplot as plt
import numpy as np
import random

def mover_bola(x, y, vx, vy, dt):
    nuevo_x = x + (vx * dt)
    nuevo_y = y + (vy * dt)
    return nuevo_x, nuevo_y

def simular_bola(x, y, vx, vy, dt, L, n_pasos):
    posiciones_x = [x]
    posiciones_y = [y]
    for i in range(0, n_pasos):
        x, y = mover_bola(x, y, vx, vy, dt)
        x, vx, y, vy = rebotar(x, y, vx, vy, L, L)
        posiciones_x.append(x)
        posiciones_y.append(y)
        
        
    return posiciones_x, posiciones_y

def graficar_bola(posiciones_x, posiciones_y, estilo='o'):
    fig, ax = plt.subplots() #Creamos una figura y un eje de matplotlib
    ax.plot( posiciones_x, posiciones_y, estilo) #Grafica la pelotita
    
    ax.set_aspect("equal") #Hace que la escala de los ejes sea la misma
    
    #Graficamos los bordes de la mesa: vlines y hlines dibujan rectas verticales
    # y horizontales respectivamente:
    ax.vlines(-5, ymin=-5, ymax=5, color="black") #Izquierda
    ax.vlines(5, ymin=-5, ymax=5, color="black") #Derecha
    ax.hlines(-5, xmin=-5, xmax=5, color="black") #Abajo
    ax.hlines(5, xmin=-5, xmax=5, color="black") #Arriba
    
    #Seteamos ticks (las lineas en los numeros de la posicion)
    #Largos cada dos metros:
    ax.set_xticks(np.arange(-6, 7, 2))
    ax.set_yticks(np.arange(-6, 7, 2))
    #Cortos (por eso el minor=True) cada 0.5 metros:
    ax.set_xticks(np.arange(-7, 7, 0.5), minor=True)
    ax.set_yticks(np.arange(-7, 7, 0.5), minor=True)
    
    ax.grid(which="both") #Dibujamos la grilla
    ax.set_xlim([-7, 7]) #Seteamos limites del grafico en x
    ax.set_ylim([-7, 7]) #idem en y
    plt.show()
    return

def espejar(z, vz, L):
    if(vz < 0):
        L = -L
    nueva_z = z - 2 * (z - L)
    nueva_vz = -vz
    return nueva_z, nueva_vz

def rebotar(x, y, vx, vy, x_max, y_max):
    nueva_x = x
    nueva_vx = vx
    nueva_y = y
    nueva_vy = vy
    if(x >= x_max or x <= -x_max):
        nueva_x, nueva_vx = espejar(x, vx, x_max)
    if(y >= y_max or y <= -y_max):
        nueva_y, nueva_vy = espejar(y, vy, y_max)
    return nueva_x, nueva_vx, nueva_y, nueva_vy

def pelicula_bola(posiciones_x, posiciones_y, nombre):
    archivo = open(nombre + ".txt", "w")
    print(1, file = archivo)
    print("", file = archivo)
    for i in range(0, len(posiciones_x)):
        print(1, posiciones_x[i], posiciones_y[i], file = archivo)
    return

def posiciones_y_velocidades_iniciales(L, v_max, n_bolas):
    muchas_x, muchas_y, muchas_vx, muchas_vy = [], [], [], []
    for i in range(0, n_bolas):
        muchas_x.append((random.random() * 2 -1) * L)
        muchas_y.append((random.random() * 2 -1) * L)
        muchas_vx.append((random.random() * 2 -1) * v_max)
        muchas_vy.append((random.random() * 2 -1) * v_max)
    return muchas_x, muchas_y, muchas_vx, muchas_vy

def simular_muchas_bolas(cond_iniciales, dt, L, n_pasos):
    posiciones_x_muchas, posiciones_y_muchas = [], []
    for i in range(0, len(cond_iniciales)):
        x, y = simular_bola(cond_iniciales[0][i], cond_iniciales[1][i], cond_iniciales[2][i], cond_iniciales[3][i], dt, L, n_pasos)
        posiciones_x_muchas.append(x)
        posiciones_y_muchas.append(y)
    return posiciones_x_muchas, posiciones_y_muchas

def archivo_muchas_bolas(posiciones_x_muchas, posiciones_y_muchas, nombre):
    archivo = open(nombre + ".txt", "w")
    print(len(posiciones_x_muchas), file = archivo)
    print("", file = archivo)
    for i in range(0, len(posiciones_x_muchas[0])):
        for j in range(0, len(posiciones_x_muchas)):
            print(j+1, posiciones_x_muchas[j][i], posiciones_y_muchas[j][i], file = archivo)
    archivo.close()
    return

def pelicula_muchas_bolas(n_bolas, n_pasos, nombre, L, v_max, dt):
    cond_iniciales = posiciones_y_velocidades_iniciales(L, v_max, n_bolas)
    x, y = simular_muchas_bolas(cond_iniciales, dt, L, n_pasos)
    archivo_muchas_bolas(x, y, nombre)
    return