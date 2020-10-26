# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 17:55:44 2020

@author: bobby
"""

input_1 = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]
input_copy = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]

test = [2,4,4,5,99,0]

def opcode(opcode):
    result = [] + opcode  
    for i in range(0,len(result),4):
        if result[i] == 1:
            result[result[i+3]] = result[result[i+1]] + result[result[i+2]]
        elif result[i] == 2:
            result[result[i+3]] = result[result[i+1]] * result[result[i+2]]
        elif result[i] == 99:
            break
    return result[0]


def opcode_tester(data):
    for i in range(100):
        for j in range(100):
            final = [] + data
            final[1] = i 
            final[2] = j
            if opcode(final) == 19690720:
                return i, j
print(opcode(input_1))        
print(opcode_tester(input_copy))
