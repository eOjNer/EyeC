# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 09:51:43 2024

@author: Administrator
"""

n = 100000
NACHRICHT_VER1 = input("Die Nachricht die, sie verschlüsseln wollen: ")
import random
import math

def createList(lst, x):
    lst.append(x)
    return lst

def Primnumber(lst):
    global x
    x = 2
    while x <= 100000:
        is_prime = True
        for i in range(2, int(math.sqrt(x)) + 1):
            if (x % i) == 0:
                is_prime = False
                break
        if is_prime:
            createList(lst, x)
        
        x += 1

def to_ascii(NACHRICHT_VER1):
    ascii_values = [ord(character) for character in NACHRICHT_VER1]
    return ascii_values

to_ascii(NACHRICHT_VER1)

NACHRICHT = NACHRICHT_VER1 

lst = []
Primnumber(lst)
random.shuffle(lst)
a = lst[random.randint(1,9592)]
b = lst[random.randint(1,9592)]
CODE1 = a * b
n1 = (a - 1)*(b - 1)


def ggT(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def finde_teilerfremden(n1):
    for i in range(2, n1):
        if ggT(i, n1) == 1:
            return i
    return None


ergebnis = finde_teilerfremden(n1)
if ergebnis:
   if ergebnis < n1:
       e = ergebnis
else:
    print(f"Es gibt keinen teilerfremden Wert für {n1}, du musst alles nochmal versuchen.")
    
CODEÖF = n1,e
VERSCHLÜSSELT = (NACHRICHT ** e) % n
print(f"Sie sollten ihre Nachricht: {VERSCHLÜSSELT} mit dem öffentlivhen code {CODEÖF} verschicken!")