
#Global Variables
#1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#The global Keyword
#1
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#2
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

