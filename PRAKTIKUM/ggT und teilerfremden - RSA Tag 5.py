# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 09:49:16 2024

@author: Administrator
"""

def ggT(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def finde_teilerfremden(n1):
    for i in range(2, n1):
        if ggT(i, n1) == 1:
            return i
    return None

n1 = 35
ergebnis = finde_teilerfremden(n1)
if ergebnis:
   ergebnis < n1
   e = ergebnis
else:
    print(f"Es gibt keinen teilerfremden Wert für {n1}, du musst alles nochmal versuchen.")