# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:36:00 2024

@author: Administrator
"""

NACHRICHT_VER1 = input("Die Nachricht, die Sie verschlüsseln möchten: ")
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

ascii_values = to_ascii(NACHRICHT_VER1)

lst = []
Primnumber(lst)
random.shuffle(lst)
a = lst[random.randint(1,9592)]
b = lst[random.randint(1,9592)]
a = 7
b = 17
CODE1 = a * b
n1 = (a - 1)*(b - 1)


def ggT(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def finde_teilerfremden(CODE1):
    for i in range(2, CODE1):
        if ggT(i, CODE1) == 1:
            return i
    return None


ergebnis = finde_teilerfremden(n1)
if ergebnis:
   if ergebnis < n1:
       e = ergebnis
else:
    print(f"Es gibt keinen teilerfremden Wert für {n1}, du musst alles nochmal versuchen.")
    
d = (1 + (a-1)*(b-1)) / e
e1 = (1 + (a-1)*(b-1)) // d
if e != e1:
    print('misscalculation')
CODEÖF = CODE1,e
VERSCHLÜSSELT = [(ascii_value ** e) % n1 for ascii_value in ascii_values]
print(f"Sie sollten ihre Nachricht: {VERSCHLÜSSELT} mit dem öffentlichen Code {CODEÖF} verschicken!")