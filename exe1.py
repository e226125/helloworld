# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:24:47 2020

@author: Asus
"""
px = 1
py = 2
a = 3
b = 4
c = 5
h = (px*a)+(py*b)+c
while True:
    if h <0:
        h2 = ((a**2)+(b**2))**0.5
        end = (-h)/h2
        print(end)  
        break
    else:
        h2 = ((a**2)+(b**2))**0.5
        end = (h)/h2
        print(end)
        break