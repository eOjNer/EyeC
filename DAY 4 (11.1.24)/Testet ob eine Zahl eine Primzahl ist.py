# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 10:39:12 2024

@author: Administrator
"""
import math
x = 0
def Primnumber():
    while x != 100000:
        x+1
        def is_prime(x):
            for i in range(2,int(math.sqrt(x))+1):
                if(x%i) == 0:
                    return False
            return True
        is_prime()
        if is_prime(x):
            print(f'Die Zahl {x} ist eine Primzahl')
        else:
            print(f'Die Zahl {x} ist keine Primzahl')
    