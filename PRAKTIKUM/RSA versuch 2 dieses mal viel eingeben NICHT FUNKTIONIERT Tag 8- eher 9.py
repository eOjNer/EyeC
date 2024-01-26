# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:14:16 2024

@author: Administrator
"""

import random
import math

def createList(lst, x):
    lst.append(x)
    return lst

def Primnumber(lst):
    global x
    x = 2
    while x <= 10000:
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

def ggT(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def finde_teilerfremden(CODE1):
    for i in range(2, CODE1):
        if ggT(i, CODE1) == 1:
            return i
    return None

NACHRICHT_VER1 = input("Die Nachricht, die Sie verschlüsseln möchten: ")
ascii_values = to_ascii(NACHRICHT_VER1)
lst = []
Primnumber(lst)
random.shuffle(lst)
a = lst[random.randint(0,len(lst))]
b = lst[random.randint(0,len(lst))]
CODE1 = a * b
n1 = (a - 1)*(b - 1)

ergebnis = finde_teilerfremden(n1)
if ergebnis:
   if ergebnis < n1:
       e = ergebnis
else:
    print(f"Es gibt keinen teilerfremden Wert für {n1}, du musst alles nochmal versuchen.")
d = pow(e, -1, (a-1)*(b-1) )
e1 = pow(d, -1, (a-1)*(b-1) )
if e != e1:
    print('misscalculation')
CODEÖF = CODE1,e
VERSCHLÜSSELT = [(ascii_value ** e) % CODE1 for ascii_value in ascii_values]
print(f"Sie sollten ihre Nachricht: {VERSCHLÜSSELT} mit dem öffentlichen Code {CODEÖF} verschicken!")

m = input(f'Wenn den Code ganz entschlüsselt wollen schreiben sie bitte JA, sonst schreiben sie bitte NEIN: ')
if m.lower() == 'ja':
    user_input = input("Die Nachricht, die Sie entschlüsseln möchten: ")
    user_input = user_input.split(', ')
    user_input_ints = [int(s) for s in user_input]
    CODE2 = input('Was ist n: ')
    k = input('Ich brauche p,q und e, IN DIESER REIHNFOLGE UND MIT KOMMA UND LEER getrennt: ')
    k1 = k.split(', ')
    po = [int(pf) for pf in k1]
    a = po[0]
    b = po[1]
    e = po[2]
    d = pow(e, -1, (a-1)*(b-1) )
    DECRYPTED = [str(pow(chr(value ** d % CODE2))) for value in user_input_ints]
    print(f"Ihre entschlüsselte Nachricht lautet: {''.join(DECRYPTED)}")
else: 
    print('Einen schönen Tag noch!')