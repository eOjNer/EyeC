# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:48:34 2024

@author: Administrator
"""



import re

wort = "red"
wort1 = 'green'
wort2 = 'blue'
x = 0
y = 0

def finde_zahlen_vor_wort(datei, wort):
     muster = r'(\d+)\s*' + wort
     ergebnisse = re.findall(muster, datei)
     return [int(e) for e in ergebnisse]

with open("textdatei.txt", "r") as datei:
    liste1 = []
    for zeile in datei:
        ergebnisse = finde_zahlen_vor_wort(zeile, wort)
        ergebnisse1 = finde_zahlen_vor_wort(zeile, wort1)
        ergebnisse2 = finde_zahlen_vor_wort(zeile, wort2)

        f = max(ergebnisse) * max(ergebnisse1) * max(ergebnisse2)
        liste1.append(f)

listsum = sum(liste1)
    
print(f'The sum of the IDs is -> {listsum}')
print(x)