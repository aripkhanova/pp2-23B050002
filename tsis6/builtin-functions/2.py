str = input()
a, b = 0, 0
for letter in str:
    if letter.islower():
        a += 1
    elif letter.isupper():
        b += 1
print("Number of uppercase letters:" ,b)
print("Number of lowercase letters" , a)