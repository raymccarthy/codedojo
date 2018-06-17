calculator = "Calculator:"
print(calculator)
one = input("Enter a number: ")
two = input("Enter another number: ")
three = input("Would you like to add another number?: ")

if three == "yes" or three == "Yes":
    thre = input("What would you like that number to be: ")
    answer = float(one) + float(two) + float(thre)
    print("The answer to you sum is" , answer,)
else:
    answer = float(one) + float(two)
    print("The answer to you sum is" , answer,)

