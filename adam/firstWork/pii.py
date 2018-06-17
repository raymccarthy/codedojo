import decimal

file_object = open("my_file.py", "a+")


def pi():

    decimal.getcontext().prec += 2  
    three = decimal.Decimal(3)    
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        print('lasts ' + str(lasts))
        s += t
       # print('t ' + str(t))
        print('    s ' + str(s))

    decimal.getcontext().prec -= 2
    return +s               
decimal.getcontext().prec = 100

pi = pi()

pi = str(pi)

file_object.write(pi)


lookup = '200405'

with open("my_file.py") as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            print("Found at line:", num)
        else:
            print("Not found")
file_object.close()




