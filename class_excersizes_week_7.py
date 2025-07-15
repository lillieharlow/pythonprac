# Program that takes 5 numbers from the user, stores them in a list, and prints the total sum.

numbers = []
for x in range(5):
    num = int(input(f"Please enter number {x+1}: "))
    numbers.append(num)

print(f"Your lucky numbers: {numbers}")
print(f"Total = {sum(numbers)}")

print("-------------------------------------------")

# Sum To End - function that repeatedly asks for an integer, adding that number to a total each time, until the user gives the input "end". When the user tells the function to end, it should return the sum of all the numbers the user entered.

# += operator is used to add the input to the total. E.g. below it will take the total and add the user in put to create a new total.

def sum_of_inputs():
    total = 0
    user_input = input("Please enter a number (or type 'end' to finish): ")

    while user_input != "end":
        total += int(user_input)
        user_input = input("Please enter another number (or type 'end' to finish): ")
        
    return total

print("-------------------------------------------")

# Loop through a dictionary of students and their marks. Print each student’s name and marks.

students = {
    "Puku": 96,
    "Pirate": 34,
    "Harlow": 100
}

for x, y in students.items():
    print(f"{x} scored {y} marks!")

print("-------------------------------------------")

# Take a list of numbers and print only the even ones using a loop.

user_input = input("Please enter 5 numbers: ")
numbers = list(map(int, user_input.split(', ')))

if numbers:
    print("You entered these even numbers in the list:")
    for number in numbers:
        if number % 2 == 0:
            print(number)
else:
    print("No numbers were entered.")

print("-------------------------------------------")

# Use a set of letters and count how many are vowels.

text = input("Please enter 5 letters: ")

def count_vowels(text):
    count = 0
    for x in text:
        count += x in "aeiouAEIOU" 
    return count

vowel_count = count_vowels(text)
print(f"You entered {vowel_count} vowels.")

print("-------------------------------------------")


# Ask the user for 3 student names and their scores, store them in a dictionary, then print a formatted report using a loop.

student_marks = {}

for x in range(3):
    key = input(f"Please enter student name: ")
    value = input(f"Please enter their score: ")
    student_marks [key] = value

print("Final Report:")
for name, score in student_marks.items():
    print(f"Student: {name} | Score: {score}")

print


'''Create your own simple text-based game that:

Uses at least one function

Includes a loop (for , while or both)

Has conditional logic (if, else, elif)

Use break and continue where suitable

Uses user input and responds accordingly

Shows some creative theme or twist (ideas...... fantasy, mystery, sci-fi, animals, trivia, survival, etc.)

Note: You have the freedom to be creative

Some Game Ideas
Number Guessing Game
Simple Quiz Game
Treasure Hunt Game'''