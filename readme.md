## Declaring variables and values

### Declaring variable and setting their values
cyborgs = 10
robots = 2
droids = 5

#### Setting values for variables in a single line
cyborgs, robots, droids = 10, 2, 5

#### Declaring with type annotation
cyborgs: int = 10
robots: int = 2
droids: int = 5

<hr>

## Variables with expression values

### Declaring new variables for sum and product and setting their values to expressions
add = robots + droids
multi = robots * droids

<hr>

## Empty function

### Define a function without arguments
def func():
    pass
### Fill the function body with placeholder
def func():
    return None

<hr>

## Take and return an argument

### Define a function without arguments
def func(arg):
    pass
### Fill the function body with placeholder
def func(arg):
    return arg

<hr>

## Multiply 

### Multiplication of two numbers
def mult_two(a: int, b: int):
    return a*b

// Doesn't need to have : int part

 -> int: is used as a type hint/known as a function annotation.
 arrow signifies the return type
 int: specifies the function is expected to return an int value

 ### Rectangle Perimeter

 def rectangle_perimeter(length: int, width: int) -> int:
    return (length + width)*2

print("Example:")
print(rectangle_perimeter(3, 2))

### Is Even
% Modulo operator = gives the REMAINDER when one number is divided by another


def is_even(num: int) -> bool:
    return num % 2 == 0

### Is positive or negative / Integer Sign Determination

def determine_sign(num: int) -> str:
    if num < 0: return "negative"
    elif num > 0: return "positive"
    else: return "zero"

### Find Remainder

def find_remainder(dividend: int, divisor: int) -> int:
    return dividend % divisor

### Backwards string

def backward_string(val: str) -> str:
    return val[::-1]

by using the negative step - 1 and string splicing . The :: allow the code to run backwards from -1 position of string

### If a number is divisible by 3 return str word, otherwise return the number
def checkio(num: int) -> str:
    if not num % 3: return "Fizz"
    else: return str(num)

if not = makes the statement False so here num % 3 is not going to reuturn a number if the num is 6 because 6 is divisible by 3 so if num was 6 then it would return the word Fizz. because there is nothing left over form the division.

### First Word (simplified)
def first_word(text: str) -> str:
    words = text.split()
    return words[0]

### Number Length
def number_length(value: int) -> int:
    return len(str(value))

### Count Vowels
def count_vowels(text: str) -> int:
    count = 0
    for char in text:
        count += char in "aeiouAEIOU"  
    return count

### Sum of integers
Calculate sum of integers from 1 to given N (including).

If N = 5, range(1, 6) is [1, 2, 3, 4, 5], and sum([1, 2, 3, 4, 5]) returns 15.

def sum_upto_n(N: int) -> int:
    return sum(range(1, N + 1))

### Convert To Title Case

def to_title_case(sentence: str) -> str:
    return sentence.title()

