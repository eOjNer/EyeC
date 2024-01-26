# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time



mcodes = {'a' : [1,2],
        'b' : [2,1,1,1],
        'c' : [2,1,2,1],
        'd' : [2,1,1],
        'e' : [1],
        'f' : [1,1,2,1],
        'g' : [2,2,1],
        'h' : [1,1,1,1],
        'i' : [1,1],
        'j' : [1,2,2,2],
        'k' : [2,1,2],
        'l' : [1,2,2,2],
        'm' : [2,2],
        'n' : [2,1],
        'o' : [2,2,2],
        'p' : [1,2,2,1],
        'q' : [2,2,1,2],
        'r' : [1,2,1],
        's' : [1,1,1],
        't' : [2],
        'u' : [1,1,2],
        'v' : [1,1,1,2],
        'w' : [1,2,2],
        'x' : [2,1,1,2],
        'y' : [2,1,2,2],
        'z' : [2,2,1,1],}

print("was soll man machen") 
Morsebuchstaben = "AÄÜÖ"
Morsebuchstaben = Morsebuchstaben.replace('ä', 'ae')
Morsebuchstaben = Morsebuchstaben.replace('ü', 'ue')
Morsebuchstaben = Morsebuchstaben.replace('ö', 'oe')
Morsebuchstaben = Morsebuchstaben.lower()       
for buchstabe in Morsebuchstaben:
    a = mcodes[buchstabe]
    def blink(t):
        print("...led on.")
        time.sleep(t)
        print("...led off.")
        time.sleep(1)
        for t in a:
            blink(t)
            
