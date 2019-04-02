#!/usr/bin/python3

var = input("Please enter a value: ")

print(var.upper())

print(len(var))

print(var.isdecimal())

from math import pi, tan, cos

y0 = 1
x = 0.5
deg = 80
v0 = 44

theta = deg * pi/180

y = y0 + x*tan(theta) - (9.81*x**2)/(2*(v0*cos(theta))**2) 

print('Height:', y, 'm')
