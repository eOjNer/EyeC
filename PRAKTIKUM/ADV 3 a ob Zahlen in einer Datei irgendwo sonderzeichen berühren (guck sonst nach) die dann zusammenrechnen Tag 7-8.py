# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:07:17 2024

@author: Administrator
"""
import re

l = ['467..114..',
'...*......',
'..35..633.',
'......#...',
'617*......',
'.....+.58.',
'..592.....',
'......755.',
'...$.*....',
'.664.598..']


l= []
with open("textdatei.txt") as f:
    for line in f:
        l.append(line.strip())


breite = len(l[0])
hoehe = len(l)

numPoss = []

for y,zeile in enumerate(l):
    for m in re.finditer(r"\d+",zeile):
        print(f'{y}','%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
        numPoss.append((y,m.start(),m.end(),int(m.group(0))))
        
numPoss1 = []
for y, xStart, xEnd, num in numPoss:
    xStart = max(0, xStart-1)
    xEnd = min(breite, xEnd+1)
    print(xStart)
    print(xEnd)
    
    if y > 0 :
        line = re.sub("\d|\."," ",l[y-1])
        if line[xStart:xEnd].strip()!="":
            numPoss1.append(num)
            continue
    
    line = re.sub("\d|\."," ",l[y])
    if line[xStart:xEnd].strip()!="":
        numPoss1.append(num)
        continue
        
    if y < hoehe-1:
        line = re.sub("\d|\."," ",l[y+1])
        if line[xStart:xEnd].strip()!="":
            numPoss1.append(num)
            continue
        
j = sum(numPoss1)
print(j)
    