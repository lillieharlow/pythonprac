'''
# default parameters

def student_name(name='Student'):
    print(f'Hello {name}')
    
student_name('Lillie')

# keywords as arguments

def add(z,y):
    return z+y

print(add(z=1, y=2))

#function with arbitrary arguments

# wap(write a program) to find a sum of multiple numbers
# '*' pass number of arguments (when the number of arg are unknown)
# also called arbitrary arguments

def find_my_sum(*numbers):
    result=0
    
    for num in numbers:
        result += num
        
    print("My sum: ", result)
    
find_my_sum(1, 1, 1, 9, 7)

print('---------------------------------------------------------)

#Local vs Global Variable
# local variable will only work inside a block of code....
# gloabl variable will work throughout the program


global_var = 5 

def test_variable():
    local_var = 10
    print('Local variable I am inside the function: ', local_var)

test_variable()
print('I am from outside the function:', global_var)

print('---------------------------------------------------------)

# Example 2 for Local and Global - fun with bith variables

name = "Lillie"

def welcome_user():
    greet_me = "Hi there!" # greet me is inside the function in local variable
    print(f'{greet_me}, {name}') # name is also inside the function but as a gloabl variable

#calling function to greet user
welcome_user()

# try to print message "Hi there!" from local

print(greet_me) # doesnt work because it isnt a global variable - its local

print('---------------------------------------------------------)

# Class excersize - is my tea hot or cold!

hot = "hot"
warm = "warm"
cold = "cold"

def check_water_temp():
    temp = input("How does the water feel when you stick your finger in it? (hot/warm/cold): ").lower()

    if temp == hot:
        print("Be careful — your tea is hot! 🔥")
    elif temp == warm:
        print("Your tea is comfy! Drink it now. 😊")
    elif temp == cold:
        print("Fuck it's cold AGAIN! Better heat it up! ❄️")
    else:
        print("Sorry, I didn't understand that. Please enter hot, warm, or cold.")

check_water_temp()

print('---------------------------------------------------------)

'''

# Lambda - advanced functions

