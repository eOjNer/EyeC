# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:21:15 2024

@author: Administrator
"""

import math   
n = int(input())
def zerlege(n):
    for c in range(2, int(math.sqrt(n)) + 1):
        if n % c == 0:
            return c, n // c
            
p,q = zerlege(n)
zerlege(n)

def ggT(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def finde_teilerfremden(n):
    for e in range(2, n):
        if ggT(e, n) == 1:
            return e
    return None
e = finde_teilerfremden(n)
d = (1 + (p-1)*(q-1)) / e
print(f'Der persönliche Code ist {p,q,d}')
