# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:56:39 2024

@author: Administrator
"""

liste = [list(zeile) for zeile in s.split("\\n")]

def benachbarte_buchstaben(buchstabe, x, y):
  anzahl = 0
  richtungen = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  for dx, dy in richtungen:
    nx = x + dx
    ny = y + dy
    if 0 <= nx < len(liste) and 0 <= ny < len(liste[0]):
      if liste[nx][ny] == buchstabe:
         anzahl += 1 
  return anzahl

buchstabe = "h"
x = 1
y = 1

benachbart = benachbarte_buchstaben(buchstabe, x, y)

haufigkeit = s.count(buchstabe)

print(f"Der Buchstabe {buchstabe} an der Position ({x}, {y}) hat {benachbart} gleiche Buchstaben um sich herum.")
print(f"Der Buchstabe {buchstabe} kommt {haufigkeit} Mal in der Zeichenfolge vor.")