'''
import math

num1 = math.ceil(2.1)
num2 = math.floor(2.9)

print(num1)
print(num2)

# ceil() - rounds up
# floor() - rounds down

import random

num = random.random()

print(num)

# random float between 0 and 1.

random_number = math.ceil(random.random() * 10)

print(random_number)

# random item from a sequence

alphabet = "abcdefghijklmnopqrstuvwxyz"

random_letter = random.choice(alphabet)

print(random_letter)

# Ed Lesson 1 - importing

# functions.py =
def sum(x, y):
    return x + y
# main.py
import functions

def average(x, y):
    total = functions.sum(x, y)
    return total / 2

average_num = average(4, 10)
print(average_num)

# Ed Lesson 2 - birthday day of the week.

import datetime
import calendar 

month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

birthdate = datetime.date(2023, month, day)

weekday = birthdate.weekday()

day_of_week = calendar.day_name[weekday]

print(f'Your birthday falls on a {day_of_week} in 2023!')

# Ed Lesson 3 - How old are you in days?

import datetime

def birthday():
    day = int(input('Enter the day: '))
    month = int(input('Enter the month: '))
    year = int(input('Enter the year: '))
    return datetime.datetime(year, month, day)

today = datetime.datetime.now()
birthdate = birthday()

days_old = (today - birthdate).days
print(f'You are {days_old} days old!')

# .days in days_old var = otherwise it would return a timedelta
# i.e. seconds, microseconds. It pulls just the int number of days.
'''

# Ed Lesson 4 - 10s challenge

import time

print("Try to guess when 10 seconds have passed.")
input("Press Enter to start...")

start_time = time.time()

input("Press Enter again when you think 10 seconds have passed...")

end_time = time.time()

elapsed = end_time - start_time

print(f"You waited {elapsed:.2f} seconds.")