#Come back to guess game

import random 



guess = input("Pick a number from one to ten: ")


random = str(random.randint(0,10))
if guess == random:
    print("correct")
    exit()
elif guess == 10 and guess != random:
    print("lower")
elif guess > random:
    print("lower")
elif guess < random:
    print("higher")

    
gguess = input("Try once more:  ")

if gguess == random:
    print("correct")
    exit()
elif gguess > random:
    print("lower")
elif gguess < random:
    print("higher")
elif gguess == 10 and gguess != random:
    print("lower")


ggguess = input("Try once more:  ")

if ggguess == random:
    print("correct")
    exit()
elif ggguess > random:
    print("lower")
elif ggguess < random:
    print("higher")
elif ggguess == 10 and ggguess != random:
    print("lower")


gggguess = input("Try once more:  ")

if gguess == random:
    print("correct")
else:
    exit()

# import random
# print(random.randint(0,9))
# from random import randint
# print(randint(0,9))
# import random
# random_number = random.randint(0,999)
# success = False
# guess_2 = input()
# guess_2 = input()
# while not success: 
#     print("Try again")
#     if guess_2 > random_number:
#         print("Lower")
#     elif guess_2 < random_number:
#         print("Higher")
