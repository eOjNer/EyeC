# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:06:40 2024

@author: Administrator
"""
import decimal
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
d = pow(e, -1, (p-1)*(q-1))
print(f'Der persönliche Code ist {p,q,d}')

user_input = input("enter text: ")
user_input = user_input.split(', ')
user_input_ints = [int(s) for s in user_input]

n = p*q

T = user_input_ints
for i in T:
    print(pow(int(i), int(d), int(n)))
    

    
    