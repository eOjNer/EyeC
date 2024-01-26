# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:59:17 2024

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

def benachbarte_buchstaben(liste, x, y):
    anzahl = 0
    richtungen = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in richtungen:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < len(liste) and 0 <= ny < len(liste[0]):
            if liste[nx][ny] == 1:
                anzahl += 1 
    return anzahl

def spielzug(liste):
    neue_liste = liste.copy()
    for x in range(len(liste)):
        for y in range(len(liste[0])):
            anzahl = benachbarte_buchstaben(liste, x, y)
            if (anzahl < 2 or anzahl > 3) and liste[x,y] == 1:
                neue_liste[x,y] = 0
            if anzahl == 3 and liste[x,y] == 0:
                neue_liste[x,y] = 1
    return neue_liste

def spielen():
    liste = np.zeros((50,50))
    liste[11,11] = 1
    liste[11,10] = 1
    liste[11,12] = 1
    liste[10,11] = 1
    liste[12,12] = 1
    print(liste)
    
    for i in range(500):
        plt.figure(figsize=(50,50))
        plt.imshow(liste, cmap='gray')
        plt.show()
        liste = spielzug(liste)
        print(liste)

spielen()
