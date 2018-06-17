file_object = open("my_file.py", "w+")

f1 = 1
f2 = 1
f3 = f1 + f2

for x in range(0, 2):
    g1 = f2
    g2 = f3
    g3 = g2 + g1

    f4 = g2
    f5 = g3
    f6 = f4 + f5

    

f1 = str(f1)
f2 = str(f2)
f3 = str(f3) 
g3 = str(g3)
f6 = str(f6)  
file_object.write(f1)
file_object.write(f2)
file_object.write(f3)
file_object.write(g3)
file_object.write(f6)












