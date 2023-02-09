def swap(c, i, j):
    temp = c[i]
    c[i] = c[j]
    c[j] = temp

def permutations(c, c_index=0):
    if c_index == len(c) - 1:
        print(''.join(c))
    for i in range(c_index, len(c)):
        swap(c, c_index, i)
        permutations(c, c_index + 1)
        swap(c, c_index, i)

s = input()
permutations(list(s))