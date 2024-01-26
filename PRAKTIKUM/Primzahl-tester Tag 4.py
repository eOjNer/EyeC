# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 09:25:01 2024

@author: Administrator
"""

import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i) == 0:
            return False
    return True

while True:
    s = input("Geben sie eine Mögliche Primzahl ein: ")
    n = int(s)
    if is_prime(n):
        print(f'Die Zahl {n} ist eine Primzahl')
    else:
        print(f'Die Zahl {n} ist keine Primzahl')