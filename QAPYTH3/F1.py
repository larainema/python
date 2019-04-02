#!/usr/bin/python3

ful = 2.25

laps = 45

FuelRequirement = ful * laps

print("Fuel Requirement:", FuelRequirement)

print("Fuel load:", FuelRequirement * 1.5)

lap_time = 80.45

t_time = lap_time - (0.35/10) * 5

lap_one_time = t_time + ((FuelRequirement * 1.5/10) * 0.35)

print("Lap one time:", lap_one_time)
