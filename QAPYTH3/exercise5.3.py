#!/usr/bin/python3

import time, random

SharePrices = {'Global Motors':50,
    'Big Blue Inc.':50,
    'Gates Software':50,
    'Banana Computers':50}

while True:
   for key,value in SharePrices.items():
       SharePrices[key] = max(1.0, value * ( 1 + ((random.random() - 0.5)/0.5) * 0.05))
       print("{:<18s} ${:05.2f}".format(key,SharePrices[key]))
       print()
       time.sleep(2)
