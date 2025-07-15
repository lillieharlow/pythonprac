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

print("--------------------------------------------")'''

languages = ["Python", "Java", "Swift", "C", "C++"]

for language in languages:
    if language == "Swift" or language == "C++":
        continue
    print(language)