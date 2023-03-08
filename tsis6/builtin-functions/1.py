def multiply(num):  
    total = 1
    for x in num:
        total *= x  
    return total  

num = [int(s) for s in input().split()]
print(multiply(num))
