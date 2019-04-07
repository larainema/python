#!/usr/bin/python3

var = input ("Please enter an integer: ")

if var.isdecimal():
    for i in range(int(var), -1, -2):
        print(i)
