def down(n):
    for i in range(n, 0, -1):
        yield i
for x in down(int(input())):
    print(x, end = " ")