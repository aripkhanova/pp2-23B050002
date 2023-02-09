def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

n=int(input())
l=list()
for i in range(n):
    x=int(input())
    l.append(x)
print(unique_list(l)) 
