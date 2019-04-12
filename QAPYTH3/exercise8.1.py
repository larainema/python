#!/usr/bin/python3
import os

start_time = 0

def start_timer():
    global start_time
    print(os.times())
    (utime, stime) = os.times()[0:2]
    start_time = utime + stime

def end_timer():
    (utime, stime) = os.times()[0:2]
    end_time = utime + stime
    print("{0:<12}: {1:01.3f} seconds".format("End Time", end_time-start_time))


start_timer()

sum = 0
for i in range(0, 10000):
    sum += i

end_timer()
