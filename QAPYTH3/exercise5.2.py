#!/usr/bin/python3

from math import pi, tan, cos

g = 9.81
v0 = 44
theta = 80 * pi/180
x = 0.5
y0 = 1

y = y0
x = 0.0
x_axis = []
y_axis = []

while y > 0:
    x = x + 0.1
    y = y0 - x*tan(theta) - (g*x**2)/(2*((v0*cos(theta))**2))

    print('x = %.1f m, y = %.1f m' % (x,y))

    x_axis.append(x)
    y_axis.append(y)

import matplotlib.pyplot as pyplot

pyplot.ylabel('Height m')
pyplot.xlabel('Distance m')

pyplot.ylim(-1,max(max(x_axis),max(y_axis)))

pyplot.plot(x_axis, y_axis)

pyplot.show()
