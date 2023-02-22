def even_numbers(n):
    for i in range(0, n, 2):
        yield i
for x in even_numbers(int(input())):
    print(x, end = ", ")