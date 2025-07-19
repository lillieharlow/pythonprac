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

# Random moduel

import random

number = random.randint(1, 10) # random int
print('I am random number:', number)

fruits = ['apple', 'orange', 'mango', 'blueberry']
choice = random.choice(fruits) # pick a random item from a list
print('I am a random fruit:', choice)

# shuffle in random
random.shuffle(fruits)
print('I am a shuffled list:', fruits)

print('--------------------------------------------------')

# Time moduel

import time

print('Please wait 3 seconds...')
time.sleep(3) # pause program for 3 sec
print('Ok done!')

# current time example
print('What is the time now?', time.time())

# time for humans
current_time = time.ctime() # current time
print('Time:', current_time)

print('--------------------------------------------------')

# Class ex - excersize to import moduel and run a func
import random, time

def random_draw():
    cards = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A', 'Joker']
    card = random.choice(cards)
    print('Your random card is.....')
    time.sleep(2)
    return card


print('--------------------------------------------------')    

# PACKAGES!

# You can choose to use specific versions of python
# versions to be installed
# suppose: we are developing a game
# game (this is the main package)
# sub-packages - sound, image, levels (1 __init__.py in each of the files)

# GAME (Dir) should contain this file --> __init__.py
# this helps python consider it a package
# generally we place initialization code for the package in this file


# Example - square
def square(x):
    return x * x

# Math tools
def mathtools(text):
    return text.upper() + '!!!'
    
print('--------------------------------------------------')    
'''

# Creating a virtual environment


# syntax = python3 -m venv virtualenvironment
# create it and activate it inorder to run it
# activate = virtualenvironment/bin/activate
# add your things in here

# once your environemnt is activated - (virtualenvironment) lillielillielillie@Chunky-Boy pythonprac % 
# pip install cowsay
import cowsay

cowsay.cow('Good mooooooorning') # keywords are the functions e.g. cow or pig
cowsay.pig("Hello") # write text to be printed

# list the packages involved and the verisons
# pip freeze > requirements.txt

# NumPy package
# numpy.org/news/

# use this to install each package all at once
# pip install -r requirements.txt

# list packages in terminal
# pip list

# delete v environment
# deactivate

