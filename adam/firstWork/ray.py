# pylint: disable=C0103

import datetime

name = input("Enter your name: ")


time = datetime.datetime.now().time()

print("Hello {} the time is right now is {}".format(name, time))



waiting_for_age = True

while waiting_for_age:
    age = input("What is your age: ")

    if age.isdigit():
        age = int(age)
        waiting_for_age = False


ageNextYear = int(age) + 1
print("You will be", ageNextYear, "in a year")


myage = 14

# print(type(myage))

if age > myage and age < 100:
    print("You are older than me")
elif age >= 100 and age < 1000:
    print("You should be dead")
elif age < myage:
    print("You are younger than me")
elif age >= 1000:
    print("Unless you are superhuman that was a lie")
else:
    print("What a coincidence we are the same age")

future_job = input("What do you want to work as when you are older: ")


if future_job.lower() == "accountant":
    print("That isn`t very fun")
elif future_job.lower() == "policeman":
    print("Sounds exiting\nGood luck ")
elif future_job.lower() == "fireman":
    print("Wow hope it works out for you")
elif future_job.lower() == "footballer":
    print("I´ve heard they make a lot of money")
elif future_job.lower() == "engineer":
    print("Me too!!!!")
elif future_job.lower() == "doctor" or future_job.lower() == "nurse":
    print("That is a very cool job, \nbecause you get to help people")
elif future_job.lower() == "traindriver":
    print("Cool, I travel by train nearly every day")
else:
    print("Whatever")
piano_play = input("Do you play piano : ")

if piano_play.lower() == "yes":
    print("That is cool so do I")

elif piano_play.lower() == "no":
    print("You should try it out")
else:
    print("+++++")

print("(-(-)-----(-)-)\nHere is a question for you:\nSo long and thanks for all the fish")

book = input("Which book is this quote from?:")

if book.lower() == "life the universe and everything" or book.lower() == "life, the universe and everything":
    print("Correct")
else:
    print("Wrong")
# /\ CMD 7






























