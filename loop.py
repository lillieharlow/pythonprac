# While loop excersize:

# Starts with the keyword 'while' followed by the 'test condition' and a :
# boolean expression - true or false?

'''count = 0

while count < 5:
    print("I am inside a loop.")
    print("Looping is interesting.")
    
# Infitine loop!

# Change this by adding new condition - only run 5 times.

count = 0

while count < 5:
    print("I am inside a loop.")
    print("Looping is interesting.")
    count += 1

print("--------------------------------------------")
# this will increase count number by 1 each time the code runs through the loop

count = 5

while count <= 10:
    print(count)
    count += 1

print("--------------------------------------------")
# Create code that outputs the multiplication numbers of user input upto 10.

number = int(input("Please enter a number: "))
             
count = 1
while count <= 12:
    answer = number * count
    print(f"{number} x {count} = {answer}")
    count += 1

print("--------------------------------------------")
# Reverse the output order of the above equation

number = int(input("Please enter a number: "))
             
count = 12
while count >= 1:
    answer = number * count
    print(f"{number} x {count} = {answer}")
    count -= 1

print("--------------------------------------------")
# Breaks in loops

while True:
    number = int(input("Enter a number: "))
    if number < 0:
        print(f"You entered {number}, that's a negative number. Good bye!")
        break
    print ("You entered: ", number)

print("--------------------------------------------")

languages = ["Python", "Java", "Swift", "C", "C++"]

for language in languages:
    if language == "Swift" or language == "C++":
        continue
    print(language)
    
print("--------------------------------------------")
    
# For loop examples:
# Sequence is a collection of items in an order.

# For loop is used to iterate over a sequence, can access individual items of that sequence.

text = "Python"

#for item in sequence:
#    statement(s)

for character in text:
    print(character)
    
# Variable 'character' will have the value 'P'
# Seeing each character in a new line because the print() function adds a new line by default

print("--------------------------------------------")

languages = ["English", "Spanish", "French"]

for language in languages:
    print(language)

# For each language in the languages list, store that variable in language and print it.

print("--------------------------------------------")

# While loop - checking that user input is what the loop is expecting with its condition

user_input = int(input('Please enter your number: '))

while user_input != 0:
    print(f'Your input = {user_input}, try again!')
    user_input = int(input('Please enter another number: '))

print('GAME OVER !!!')

# loop becomes stuck / infinte if int is not defined with user input - because its type would be a str and the loop condition is looking for the int 0.

print("--------------------------------------------")

# Break example with while loop and nested for loop

while True:
    user_input = input('Please enter three colours: ')
    colours = user_input.split()

    for colour in colours:
        if colour.lower() == "purple":
            print('Purple is the winning colour, GOOD BYE!')
            exit()
    else:
        print(f'Your colours are: {user_input}. Try 3 NEW colours!')

print("--------------------------------------------")

# The code below can be changed to a for loop:
count = 1

while count <= 5:
    print(count)
    count += 1

# For loop of code above:

for count in range(1, 6): # prints 1 - 5 not 6 because it goes upto the last number, not inc
    print(count)

number = int(input("Enter a number: "))

for count in range(1, 11):
    product = number * count
    print(number, "x", count, "=", product)
    
print("-------------------------------------------")

# Create a program to find the sum of 1 to 100?
# Result should be equal to: result = 1+ 2+ 3...

total = 0 # Must define the total number first or there will be an error
# Loop through the range of numbers from 1 to 100 and add each number to total

for number in range(1, 101):
    total += number
print(total) # Make sure to remove indent of print line or it will print every time it += the total

print("-------------------------------------------")

'''