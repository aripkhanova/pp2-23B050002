import os
first = open("C:\\Users\\facto\\Desktop\\KBTU\\pp2\\pp2-23B050002\\tsis6\\dir-and-files\\stroki.txt", "r")
second = open("C:\\Users\\facto\\Desktop\\KBTU\\pp2\\pp2-23B050002\\tsis6\\dir-and-files\\copy7.txt", "a")
for lines in first:
    second.write(lines)
