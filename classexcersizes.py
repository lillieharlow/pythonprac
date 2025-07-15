#Exercise 1: Even or Odd Number
#Task: Write a Python program that takes an integer input from the user and checks if the number is even or odd.

while True:
    str_number = input('What is your number? ')
    if str_number.isdigit():
        number = int(str_number)
        if number % 2 == 0:
            print(f'{number} is an even number.')
        else:
            print(f'{number} is an odd number.')
        break
    else:
        print('Naughty! Please enter a whole number.')


#Exercise 2: Simple Calculator (Addition)
#Task: Create a simple calculator that adds two numbers entered by the user.

while True:
    num1 = input('Please enter your first number: ')
    num2 = input('Please enter your second number: ')
    try:
        n1 = float(num1)
        n2 = float(num2)
        print(f'{n1} + {n2} = {n1 + n2}')
        break
    except ValueError:
        print('Naughty! Please enter valid numbers only.')

#Exercise 3: Age Group Categorisation
#Task: Write a program that asks the user for their age and prints out their age group. The categories are:

while True:
    age = input('Please enter your age: ')
    if age.isdigit():
        age_num = int(age)
        if age_num <= 12:
            print('Your age group: Child')
        elif age_num > 12 and age_num <= 19:
            print('Your age group: Teenager')
        elif age_num > 19 and age_num <= 59:
            print('Your age group: Adult')
        else:
            print('Your age group: Senior')
        break
    else:
        print('Naughty! Please enter your age as a whole number')
    
#Excersise 4: Turn the pseudocode given below into sensible programming code.

'''IF the current day is Wednesday print the message "It's Wednesday!"

ELSE print the message "What day is it?" and store the user input.

IF the user input doesn't end in "y", repeat until they enter a day that ends in "y" 

IF the user input is "wednesday", print "Haha, you're a funny one! See ya!" and exit the program.

print a message that uses the user input to say something like "Thankyou for letting me know that today is {user input}! See ya!"'''

while True:
    current_day = input('What day is it? ')
    if current_day == 'Wednesday':
        print("It's Wednesday!")
        break
    elif current_day == 'wednesday':
        print("Haha, you're a funny one! See ya!")
        break
    elif current_day[-1] == 'y':
        print(f"Thankyou for letting me know that today is {current_day}! See ya!")
        break
    else:
        print(current_day)
        
#Exercise 5: Turning A Problem Into Pseudocode

'''Alex needs to make a meatlovers pizza - a pizza with a variety of meats and at least one type of cheese. He usually likes to have beef, chicken, steak, cabanossi, and pepperoni - but it's not the end of the world if some of those toppings are missing. If they're available, he'll use them. If there's more than 3 of those toppings available or if there's not a lot of toppings available but more than one type of cheese on the pizza, he needs to use a thick pizza base. If the pizza is using a thin base, it will cook in the oven for a short amount of time - thicker pizza bases should cook for longer. Alex likes to check on the pizza every 5 minutes, and will take the pizza out of the oven when it's done.'''

#Meatlovers pizza - variety of meats, at least 1 cheese

meat = ["beef", "chicken", "steak", "cabanossi", "pepperoni"]
cheese = ["single", "double"]

#input from user

print(f"Meat toppings list: {meat}")
pizza_toppings = input('What toppings would you like? (comma separated): ')
chosen_meats = [m.strip() for m in pizza_toppings.split(',') if m.strip() in meat]

print(f"Cheese toppings list: {cheese}")
cheese_amount = input('How much cheese do you want? (single/double): ')

#What base is needed and cooking time

if len(chosen_meats) > 3 or cheese_amount == "double":
    print('thick base - longer cooking time')
else:
    print('thin base - shorter cooking time')

print("Check your pizza every 5 minutes and take it out when done.")
