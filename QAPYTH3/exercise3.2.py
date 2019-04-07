#!/usr/bin/python3
import getpass

attempt = 1

supplied_pin = getpass.getpass("Enter your PIN:") 

while supplied_pin != 'Pass' and attempt < 3:
   print('Login Failed')
   print('You try', attempt)
   supplied_pin = getpass.getpass("Enter your PIN:")
   attempt += 1

if attempt >= 3:
   print('You try 3 times, your account locked!')
else:
   print('Login success')
