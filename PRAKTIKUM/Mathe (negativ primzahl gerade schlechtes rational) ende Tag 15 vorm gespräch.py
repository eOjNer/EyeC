# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:10:15 2024

@author: Administrator
"""

import math

negativ = 'negativ'
negativ = False
gerade = 'gerade'
gerade = False
rational = 'rational'
rational = False
Primzahl = 'Primzahl'
Primzahl = False

def negativ(x):
    if x < x * (-1):
        negativ = True
    return negativ

def gerade(x):
    if x % 2 == 0:
        gerade = True

def rational(x):
    if ',' in x:
        rational = True

def Primzahl(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            Primzahl = False
        else:
            Primzahl = True

x = int(input('Nummer: ')) 

input1 = input('Nach was testen: ')
input1 = input1.split(' ')

if negativ in input1:
    negativ(x)
if gerade in input1:
    gerade(x)
if rational in input1:
    rational(x)
if Primzahl in input1:
    Primzahl(x)

if negativ == True:
    print(negativ)