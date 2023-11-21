'''
Create a while loop that uses and indexing value called i
Initialize i as 0
Count to 4
Create a while loop that runs until a user enters "end"
Create a while loop that increments or decrements a number based on user selection

Notes:



'''
# count to 4 
from ast import Str


i = 0 
while 1 < 6: 
    print(i)
    if i == 4:
        break
    i += 1

# Create a while loop that runs until a user enters "end"
test_loop = " "
while test_loop != "end":
    test_loop = input("Type 'end' to exit loop: ")
print("")
print("")



#Create a while loop that increments or decrements a number based on user selection
menu_option = 0
current_number = 5
while menu_option != 3:
    print(f"the current number is: {current_number}")
    print("select option: ")
    print(f"\t1: Increment by 1 ")
    print(f"\t2: Substract by 1 ")
    print(f"\t3: End program ")
    menu_option = int(input(f"\tSelection: "))
    print("")
    if menu_option == 1:
        current_number += 1
    elif menu_option == 2:
        current_number -= 1
    elif menu_option == 3:
        print("program ended")
        break
    else:
        print ("choose a current option: (1, 2, 3)")
    #print(f"the current number is: {current_number}")