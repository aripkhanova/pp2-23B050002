# + 
x = 5
y = 3
print(x + y) 

# - 
x = 5
y = 3
print(x - y) 

# * 
x = 5
y = 3
print(x * y) 

# / 
x = 12
y = 3
print(x / y) 

# % 
x = 5
y = 2
print(x % y) 

# ** 
x = 2
y = 5
print(x ** y) 

# // 
x = 15
y = 2
print(x // y) 

# Python Assignment Operators
# =
x = 5
print(x)

# +=
x = 5
x += 3
print(x)

# -=
x = 5
x -= 3
print(x)

# *=
x = 5
x *= 3
print(x)

# /=
x = 5
x /= 3
print(x) 

# %=
x = 5
x%=3
print(x) 

# //=
x = 5
x//=3
print(x) 

# &=
x = 5
x &= 3
print(x)

# |=
x = 5
x |= 3
print(x)

# ^=
x = 5
x ^= 3
print(x)

# >>=
x = 5
x >>= 3
print(x)

# <<=
x = 5
x <<= 3
print(x)

#Python Comparison Operators
x = 5
y = 3
print(x == y)

x = 5
y = 3
print(x != y)

x = 5
y = 3
print(x > y)

x = 5
y = 3
print(x < y) 

x = 5
y = 3
print(x >= y) 

x = 5
y = 3
print(x <= y)

#Python Logical Operators
x = 5
print(x > 3 and x < 10) 

x = 5
print(x > 3 or x < 4)

x = 5
print(not(x > 3 and x < 10))

# Python Identity Operators
# is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #returns True because z is the same object as x
print(x is y) #returns False because x is not the same object as y, even if they have the same content
print(x == y) #to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
 
# is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z) #returns False because z is the same object as x
print(x is not y) #returns True because x is not the same object as y, even if they have the same content
print(x != y) #to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

# Python Membership Operators
# is
x = ["apple", "banana"]
print("banana" in x)

# is not
x = ["apple", "banana"]
print("pineapple" not in x)