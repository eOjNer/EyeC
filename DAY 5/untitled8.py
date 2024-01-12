# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:18:51 2024

@author: Administrator
"""

def finde_inverses(e, n1):
    for d in range(1, n1):
        if (d * e) % n1 == 1:
            return d
    return None

def from_ascii(ascii_values):
    return ''.join(chr(ascii_value) for ascii_value in ascii_values)


VERSCHLÜSSELT = [387399385, 238703355, 366823568, 33554432, 366823568, 396067253, 120274065, 258265327, 396067253, 33554432, 7017064, 396067253, 91214024, 91214024, 39135393]
n1 = 421418052
e = 5


d = finde_inverses(e, n1)
if d is None:
    print(f"Es gibt keinen inversen Wert für {e} modulo {n1}, Sie müssen alles nochmal versuchen.")
else:
    ENTSCHLÜSSELT = [(ascii_value ** d) % n1 for ascii_value in VERSCHLÜSSELT]
    nachricht = from_ascii(ENTSCHLÜSSELT)
    print(f"Ihre entschlüsselte Nachricht lautet: {nachricht}")
