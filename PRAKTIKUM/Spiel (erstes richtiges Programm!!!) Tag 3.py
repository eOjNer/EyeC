# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 09:16:12 2024

@author: Administrator
"""
O = 'O'
d = 'd'
x = 0
s = (f'\nSchade, beim nächsten mal schaffst du mehr als 0! Dein Rank ist {O}!')
import time
import random

def timeAndInput():
    start = time.time()
    inp = input()
    end = time.time()
    return inp, end-start

Words = {1 : 'Hallo',
         2 : 'Bach',
         3 : 'Flugzeug',
         4 : 'Haus',
         5 : 'Rotebeete'}

while True:
    RANDOM = random.randint(1,5)
    print(Words[RANDOM])
    input1, d = timeAndInput()
    if input1 != Words[RANDOM] or d > len(Words[RANDOM]):
        print(s)
        break
    else:
        x = x + 1
         
    if x == 0:
        O = 'F'
    if x < 3 and x > 0:
        O = 'D'
    if O == 'D':
        s = f'\nMit {x} Punkten und einem Rank {O}, schon mal mein guter anfang ;D!'
    if x < 5 and x > 3:
        O = 'C'
    if O == 'C':
        s = f'\nRank {O}, schon mit {x}? Fasst schon Rank B und dann ist es nur noch ein Katzensprung bis Rank A!'
    if x < 8 and x > 5:
        O = 'B'
    if O == 'B':
        s = f'\n{x} Punkte??? Es sind ja nur noch {10 - x} Punkte von deinem Rank B zum unglaublichen Rank A!!!'
    if x >= 10:
        O = 'S'
    if O == 'S':
        s = f'\nWOW!! Rank {O}!! Jetzt beginnt der Weg zu Welt Rekord! Das sind 561796327157 Punkte!! Du brauchst also nur noch {561796327157-x} Punkte, du hast ja {x}!!!!!!'
         
         