'''
# Sum to 100

def sum_to_hundred():
    count = 0
    result = 0
    while count < 101:
        result += count # result has to be called first or you get wrong total
        count += 1
    return result

print(f'With a while loop: {sum_to_hundred()}')

def for_loop_sum_to_hundred():
    total = 0
    for x in range(0, 101):
        total += x
    return total

print(f'With a for loop: {for_loop_sum_to_hundred()}')

def sum_easy():
    return sum(range (101))

print(f'One line with sum(): {for_loop_sum_to_hundred()}')


# Sum for evens

def sum_of_evens(input_list):
    result = 0 # Initialize a variable to store the running total. Without it, Python wouldn't know what result is!

    for x in input_list:
        if x % 2 == 0:
            result += x
    return result

print(sum_of_evens([6, 8, 23]))

'''
# Search through list

LIST_OF_WORDS = [
    "serendipity",
    "petrichor",
    "supine", 
    "solitude",
    "aurora",
    "idyllic",
    "clinomania",
    "pluviophile",
    "euphoria",
    "sequoia"
]

def filter_list(some_string): # func name with argument - input called some_string - this is where the search letters will go
    output_list = [] # creates an empty list to store the results
    
    for word in LIST_OF_WORDS: # goes through each word on the list
        if some_string in word: # substring check - checking if argument is inside word inside list
            output_list.append(word) # if true .append() adds the word to the output_list

    return output_list

print(filter_list("hor"))

# Extension Challenge: Enumerate Statement

def threeven(some_list):
    
    for index, number in enumerate(some_list):
        if number % 3 == 0:
            return index

    return None