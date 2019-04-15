#!/usr/bin/env python
input = int(input('Number:'))

for i in range(input):
    for j in range(i):
        print('*', end = "")
    print('\n', end = "")

