'''
# Python is a multi-paradigm language.
# able to use different patterns to solve problems, including Functional Programming
# to write small, simple functions which perform one task

# Callback Functions -  we can write modular code

def add(a, b):
    print(a + b)

def multiply(a, b):
    print(a * b)

def subtract(x, y):
    print(x - y)

def divide(x, y): 
    print(x / y)

def do_math(num1, num2, cb):
    cb(num1, num2)

do_math(5, 4, add)
do_math(9, 7, multiply)
do_math(20, 3, subtract)
do_math(100, 5, divide)

print('------------------------------------------')

# callback functions to return values

def process_input(input, cb): # returns value of whatever callback func is passed to it as long as input is str
    if isinstance(input, str):
       return cb(input)

def greet(name):
    return "Hello " + name

greeting = process_input("Bob", greet) # result of passing "Bob" into greet so we see "hello bob"

print(greeting)

print('------------------------------------------')



# Lambda Function
# anonymous functions / don't have a name
# contained in single expression (no multi-line)
# use lamda in place of def
# don't name or return value

# Immediately invoked function expression - IFFE
# function we evoke directly after defining it

number = int(input("Pick a number"))
double = (lambda x: x*2)(number)
print(f"{number} doubled is {double}")

print('------------------------------------------')

# Passing as a call back -  specifically told a *lambda function to print a value here
# default behavior is to return a value

def do_math(num1, num2, cb):
    cb(num1, num2)

do_math(10, 2, lambda x, y: print((x ** y) - x + y))

print('------------------------------------------')


# Lambda excersize 1 - double number

# Can have multiple arguments but only one expression

double = lambda n: n*2 #n = function parameter :n*2 = return value of the function

print(double(10))

print('------------------------------------------')

# Lambda excersize 2 - print larger number

larger = lambda a,b:a if a>b else b

print(larger(10,47))

print('------------------------------------------')

# Lambda excersize 3 - key to sort a list in a custom way

names = ["Alantis", "Gregor", "Zane", "Jussy", "Tommy", "August"]

names.sort(key = lambda x:len(x))
print(names)

# key = lambda that takes argument (x) and returns the len of the str
# names are now sorted based on their length from shortest to longest instead of alphabetically

print('------------------------------------------')




# Higher order function - takes another function as an argument

# Map function - takes two arguments
# a function and an iterable (list, tuple, etc).
# returns a map object - can be converted back into an iterable - with the function applied on every element of the original

def double(num):
    return num * 2

numbers = (1,2,3,4,5)
doubled_map = map(double, numbers)
doubled = tuple(doubled_map)
print(doubled)

#OR

numbers = (1,2,3,4,5)
doubled_map = map(lambda x: x *2, numbers)
doubled = tuple(doubled_map)
print(doubled)

print('------------------------------------------')


# Filter function - takes two arguments
# 1 = a function that evaluates to True or False
# 2 = iterable

pets = [
    {"name": "Biko", "animal": "dog"},
    {"name": "Marmelade", "animal": "cat"},
    {"name": "Frankie", "animal": "rat"},
    {"name": "Themla", "animal": "parrot"},
    {"name": "Bronte", "animal": "dog"},
    {"name": "Wally", "animal": "cat"},
    {"name": "Cosmo", "animal": "dog"}
]

dogs = list(filter(lambda pet: (pet["animal"] == "dog"), pets))
print(dogs)

print('------------------------------------------')



# Reduce function
#imported from functools module
# takes 3 arguments (a func with 2 parameters, an iterable and an optional inital value)
# returns a single value

from functools import reduce
numbers = [1,2,3,4,5]
sum = reduce(lambda a, b: a + b, numbers)
print(sum)

print('------------------------------------------')


# Closures

# commonly used for creating function factories
# implementing callbacks
# maintaining state in functional programming paradigms.

# Enclosing Function: This is the outer function - defines a nested function within it. Creates a scope in which variables can be accessed by the inner function.
# Inner Function: Nested function - defined within scope of enclosing function. Has access to variables in enclosing scope, even after outer function has executed.
# Closure: When inner function is returned from enclosing function, retains access to variables from its enclosing scope, forms a closure.

# Example 1 - simple closure

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure(5))  # Output: 15

# outer function takes argument (x)
# defines an inner function (y)
# inner function returns x + y
# When outer function is called with argument 10 = returns innner function
# forming closure where x is remembered as 10
# thus calling closure(5) results in 10 + 5 = 15

print('------------------------------------------')

# Example 2 - maintaining state

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter1 = counter()
print(counter1())  # Output: 1
print(counter1())  # Output: 2

counter2 = counter()
print(counter2())  # Output: 1 (starts from 1 again)

# couinter is a function
# returns an inner function - increment
# increment (inner function) 'increments' the count variable each time its called
# each time counter is called it creates a new closure with its own count variable
# allowing multiple independent counters to exist

print('------------------------------------------')

'''



# Lambda challenge 1
# func "filter_students" - takes 2 arguments
# students = dict with keys for name str and grade int
# condition = lambda takes student dict returns True if student meets condition
# filter_students apply condition lambda to students and return ls of dict containing students that meet the condition

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 75},
    {'name': 'Charlie', 'grade': 90},
    {'name': 'David', 'grade': 60}
]

filter_students = list(filter(lambda student: student['grade'] >= 80, students))

print(filter_students)

# solution on ed was =
def filter_students(students, condition):
    return [student for student in students if condition(student)]

condition = lambda student: student['grade'] >= 80