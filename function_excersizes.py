'''
# command and click on the function e.g. input() takes you to builtin functions.
# - allows us to make our on function. print() i a function sum() is a function.

# Functions
# Group of related statements that preform a specific task
# Divide into smaller chunkks, easier to program and change

def greet():
    print('Hello')
    print('How do you do?')

# To bring this function into action - we need to call it

greet()

# You need to define a function first before you call it

print('--------------------------------')

# Arguments:

def greet(name):
    print(f'Hello, {name}')
    print('How do you do?')

greet('Lillie')

print('--------------------------------')

def add_numbers(n1, n2):
    result = n1 + n2
    print(f'The sum is: {result}')

add_numbers(9, 3)

print('--------------------------------')

# Return statement
# the return statement in the code below will not print "How do you do?"
# the function terminates when it encounters the return statement
# control of the program goes back to the place from where the function was called

def greet(name):
    print(f'Hello, {name}')
    return
    print('How do you do?')

greet('Lillie')

print('--------------------------------')

# Excersize - find average marks and reward a grade

# def function to find out the average of total marks and divide by len of list items (subjects)

def find_mark_average(marks):
    marks_sum = sum(marks)
    total_subjects = len(marks)
    
    average_marks = marks_sum/total_subjects
    
    return average_marks 

# def function to find out the grade using if/else statements

def grade(average_marks):
    if average_marks >= 80:
        final_grade = "A"
    elif average_marks >= 60:
        final_grade = "B"
    elif average_marks >= 50:
        final_grade = "C"
    else:
        final_grade = "F"
        
    return final_grade

# input and call functions

marks = [55, 64, 75, 80, 65]
average_marks = find_mark_average(marks)
final_grade = grade(average_marks)

#output data to user

print(f'Your mark average was {average_marks}')
print(f'Your final grade is {final_grade}')

print('--------------------------------')

# Add and multiply two numbers by creating two functions add_numbers() and multiply_numbers()

def add_numbers(n1, n2):
    sum = n1 + n2

    return sum

def multiply_numbers(n1, n2):
    multi = n1 * n2

    return multi

n1 = 6
n2 = 5

sum = add_numbers(n1, n2)
multi = multiply_numbers(n1, n2)

print(f'The sum of numbers is: {sum}')
print(f'Your numbers multiplied is: {multi}')

print('--------------------------------')
'''

#