num = int(input("Choose a number from 1-10: "))
n = 0
file_object = open("my_file.py", "w+")
f2 = 1
f1 = 1


for x in range(0,10000):
    f = f1 + f2
    f2 = f1
    f1 = f
    n = n + 1
    if f > num:
        n = n + 1
        print("The next fibonacci number is {}, the previous fibonacci number is {} and it took {} times to calculate that".format(f,f2,n))
        break
    if num == f:
        print("The number {} is a fibonacci number".format(f))
        break
   