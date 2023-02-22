def squares(a, b):
    for i in range (a, b+1):
        yield i**2
a, b = [int(s) for s in input().split()]
for x in squares(a, b):
    print(x)