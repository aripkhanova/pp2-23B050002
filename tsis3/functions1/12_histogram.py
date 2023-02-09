def histogram(items):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
            output += '*'
            times = times - 1
        print(output)

n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)

print(histogram(l))