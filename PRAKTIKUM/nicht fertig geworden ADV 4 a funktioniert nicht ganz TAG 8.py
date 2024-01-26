# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:06:17 2024

@author: Administrator
"""

import re

cards = []
with open("textdatei.txt") as f:
    for line in f:
        line.replace('Card', '')
        line.replace(':', '')
        numbers = re.findall("\d", line)
        line.replace(numbers[0], '')
        cards.append(line.strip())
                 
def Punkte_Rechner(cards):
    Punkte1 = 0
    for card in cards:
        GewN, VerlN = card.split('|')
        GewN = set(map(int, GewN.split()))
        VerlN = set(map(int, VerlN.split()))
        spiel = GewN & VerlN
        Punkte = 2**(len(spiel) - 1) if spiel else 0
        Punkte1 += Punkte
    return Punkte1

cards = [
    "41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

print(Punkte_Rechner(cards))
