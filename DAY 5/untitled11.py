# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:23:12 2024

@author: Administrator
"""

def erweiterter_euklidischer(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = erweiterter_euklidischer(b % a, a)
        return g, y - (b // a) * x, x

def finde_inverses(e, n1):
    g, x, _ = erweiterter_euklidischer(e, n1)
    if g == 1:
        return x % n1
    return None

def from_ascii(ascii_values):
    return ''.join(chr(ascii_value) for ascii_value in ascii_values)

def power_mod(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


VERSCHLÜSSELT = [438976, 1030301, 1331000, 1331000]
n = 1150446259
e = 3

d = finde_inverses(e, n)
if d is None:
    print(f"Es gibt keinen inversen Wert für {e} modulo {n}, Sie müssen alles nochmal versuchen.")
else:
    ENTSCHLÜSSELT = [power_mod(ascii_value, d, n) for ascii_value in VERSCHLÜSSELT]
    nachricht = from_ascii(ENTSCHLÜSSELT)
    print(f"Ihre entschlüsselte Nachricht lautet: {nachricht}")
