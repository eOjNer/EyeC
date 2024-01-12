# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:01:50 2024

@author: Administrator
"""
n = 100000
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
lst = []
Primnumber(lst)
random.shuffle(lst)
a = lst[random.randint(1,9592)]
b = lst[random.randint(1,9592)]
CODE1 = a * b
e = (a-1)*(b-1)
