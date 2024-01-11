# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 10:59:19 2024

@author: Administrator
"""

import math
import time
def Primnumber():
    global x
    x = 2
    while x <= 100000:
        is_prime = True
        for i in range(2, int(math.sqrt(x)) + 1):
            if (x % i) == 0:
                is_prime = False
                break
        if is_prime:
            print(f'Die Zahl {x} ist eine Primzahl')
        x += 1
        time.sleep(0.2)

Primnumber()
