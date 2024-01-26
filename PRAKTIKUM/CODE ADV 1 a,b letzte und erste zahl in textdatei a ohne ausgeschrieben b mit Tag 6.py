# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:32:19 2024

@author: Administrator
"""

import re

num2words = {
    1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
    6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}

with open("textdatei.txt", "r") as datei:
    liste = []
    for zeile in datei:
        zeile = zeile.replace('one', 'one1one')
        zeile = zeile.replace('two', 'two2two')
        zeile = zeile.replace('three', 'three3three')
        zeile = zeile.replace('four', 'four4four')
        zeile = zeile.replace('five', 'five5five')
        zeile = zeile.replace('six', 'six6six')
        zeile = zeile.replace('seven', 'seven7seven')
        zeile = zeile.replace('eight', 'eight8eight')
        zeile = zeile.replace('nine', 'nine9nine')

        numbers = re.findall("\d", zeile)
        first = numbers[0]
        last = numbers[-1]
        liste.append(int(first + last))

listsum = sum(liste)
print(f'The sum of the numbers is -> {listsum}')
