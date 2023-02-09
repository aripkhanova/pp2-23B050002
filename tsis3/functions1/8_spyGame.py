def spygame(lst):
    for i in range(len(lst)-2):
        if lst[i]==lst[i+1]==0 and lst[i+2]==7:
            return True
    return False

n=int(input())
l=list()
for i in range(n):
    x=int(input())
    l.append(x)
print(spygame(l))