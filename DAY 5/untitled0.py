# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 08:43:55 2024

@author: Administrator
"""
def to_ascii(text):
    ascii_values = [ord(character) for character in text]
    return ascii_values


text = input("Enter a string: ")
print(to_ascii(text))

