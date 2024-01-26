# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:39:14 2024

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

        if max(ergebnisse) > 12 or max(ergebnisse1) > 13 or max(ergebnisse2) > 14:
            x += 1
       
        else:    
            numbers = re.findall("\d+", zeile)
            first = numbers[0]
            print(first, zeile)
            liste1.append(int(first))

listsum = sum(liste1)
    
print(f'The sum of the IDs is -> {listsum}')
print(x)

