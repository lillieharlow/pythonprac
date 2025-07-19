'''
# Moduels and Packages

# syntax = import moduelname
# when calling = moduelname.functionname
# print(dir(moduelname)) = will list all functions in the moduel

# this is a function inside a moduel (moduel = class_19_July)
def add(a, b): # function name = add | args = a & b
    result = a + b # define variable
    return result # what to do with the variable

# only returning result - still need to print the result

print(add(3, 4)) # you would add moduel name before function to call that function in that moduel

print('--------------------------------------------------')

# Standard library moduels e.g. random, time, date.time

# Example - using math moduel to get value of pi
import math

print('Here is the value of pi: ', round(math.pi, 2))

# above print
# math.pi = value of pi
# rount() rounds pi and the 2 = 2 decimal places

print(f"Pi value formatted: {math.pi:.2f}")

# above print
# create f str and format number in {}
# by using .2f or .3f etc = decimal places we can format/round up any number
# control the variable outcomes

print('--------------------------------------------------')

# Renaming the imports - for shortcuts

import math as m

print(m.pi)

print('--------------------------------------------------')

# Import only pi from math - save on space

from math import pi

print(pi)

print('--------------------------------------------------')
'''
# print(dir(moduelname)) = will list dir in the terminal