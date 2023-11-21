# Create a function called loop_letters()
# The function should have one parameter for a string
# Loop through the string and print each letter
# Create a function called loop_numbers()
# The function should have two parameters for start and end integers
# Loop through the range of numbers and print each number
# Create a function called loop_list()
# The function should accept a list
# Loop through the list and print each item
# Call all three functions with appropriate arguments

#collections are multiple values in one variable 
#for loop 
#   1. for keyboard
#   2. variable that represents the current item in the colleciton. 
#   3. 


def loop_letters(string):
    for letter in string: 
        print(letter)
def loop_numbers(start, end):
    for number in range(start, end+1):
        print(number)
def loop_list(lst):
    for item in lst:
        print(item)

loop_letters("hello")
loop_numbers(1,10)
loop_list([1, 2, 3, 4, 5])