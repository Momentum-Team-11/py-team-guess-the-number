



import random
count = 3
random_number = 5
number = int(input("Pick a number 1-20! "))
while number != random_number:
    count = count - 1
    if number < random_number:
        print("Too low...", count, "guesses left")
        number = int(input("Pick a number 1-20! "))
    if number > random_number:
        print("Too High...", count, "guess left")
        number = int(input("Pick a number 1-20! "))
    else: 
        number == random_number
        print("yay")
# print(number)
# import random interger from 1-20
# make a range from 1-20 
# learn to prompt through input
