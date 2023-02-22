def squares(n):
    for i in range (n):
        yield i**2
num = int(input())
for x in squares(num):
    print(x)