import os, string
if not os.path.exists("letters"):
    os.makedirs("C:\\Users\\facto\\Desktop\\KBTU\\pp2\\pp2-23B050002\\tsis6\\dir-and-files\\letters")
for letter in string.ascii_uppercase:
    with open("C:\\Users\\facto\\Desktop\\KBTU\\pp2\\pp2-23B050002\\tsis6\\dir-and-files\\letters\\ " + letter + ".txt", "w") as f:
        f.writelines(letter)