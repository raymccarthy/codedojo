import random 
import os
answer = ''
for count in range(0,10000):

    if count%3 == 0 and count%5 == 0:
        answer = 'fizzbuzz'
        different = "fizz"
    elif count%3 == 0:
        answer = 'fizz'
        different = "buzz"
    elif count%5 == 0:
        answer = 'buzz'
        different = "fizzbuzz"
    else:
        answer = count

    if random.randint(1,100) == 10:
        print(different)
        print("Oops I meant to say {}".format(answer))
        break
    else:
        print(answer)
           