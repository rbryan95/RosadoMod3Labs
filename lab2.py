import random
# Create a function called get_random_number()
# This function should have no parameters
# This function should get a bottom and top number from the user
# This function should return a random integer to the user based on the bottom and top numbers
# Call the get_random_number function to get a random number
# Use a while loop and user input to allow the user to guess the random number
# If they are too high or too low, tell the user

def get_random_number():
    bottom = int(input("plesae enter a bottom number: "))
    top = int(input("plesae enter a top number: "))
    random_number = random.randrange(bottom, top + 1)
    return random_number


rand = get_random_number()

guess = int(input("guess the number: "))
while guess != rand:
    if guess > rand:
        print("too high! guess again: ")
    elif guess < rand: 
        print("too low! guess again!")
        guess = int(input("guess the number: "))
    elif guess == rand:
        print("you got it!")
        break
    