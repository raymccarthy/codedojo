import random 
for count in range(0,10000):
    if random.randint(1,100) == 10:
        print("{}\nOops I meant to say".format(count + 132))
    if count%3 == 0 and count%5 == 0:
        print("FizzBuzz")
    elif count%3 == 0:
        print("Fizz")
    elif count%5 == 0:
        print("Buzz")
    else:
        print(count)
           