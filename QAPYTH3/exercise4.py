#!/usr/bin/python3

str = 'Belgium,12,Beijing,100000'

hyphens = '-' * len(str)

print(hyphens)

items = str.split(',')

print(':'.join(items))

print(int(items[1]) + int(items[3]))


