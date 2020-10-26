# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:19:08 2020

@author: bobby
"""
import numpy as np

with open('mission1_input2.txt', 'r') as infile:
    modules = infile.readlines()

modules = [int(m) for m in modules]
modules = np.array(modules)

fuel_requirements = (modules//3) - 2 


total_fuel = np.sum(fuel_requirements)
print(total_fuel)

# part2
fuel_extra = []
for m in modules:
    current_fuel = (m//3)-2
    current_total = 0
    while current_fuel >0 :
        current_total += current_fuel
        current_fuel = (current_fuel//3)-2 
    fuel_extra.append(current_total)
    
fuel_extra = np.array(fuel_extra)
print(np.sum(fuel_extra))
        



    
