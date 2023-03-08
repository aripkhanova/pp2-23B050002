import os
a = [i for i in input().split()]
f = open("C:\\Users\\facto\\Desktop\\KBTU\\pp2\\pp2-23B050002\\tsis6\\dir-and-files\\fileFor5.txt", "w")
for elem in a:
    f.write(elem + " ")
f.close()