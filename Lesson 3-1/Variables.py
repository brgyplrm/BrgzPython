# Variables 

x = 5 # this is type int
y = "John" # this is type str

# Casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get the type of data type

x = 5
y = "John"
print(type(x))
print(type(y))

# Case sensitive
a = 4
A = "Sally"
#A will not overwrite a

#Legal Variables names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal Variable names 
""" 
    2myvar = "John"
    my-var = "John"
    my var = "John" 
"""
# many values in multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# one value in multiple variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

# unpacking collection = (collection of values in a  list and tuples) allows to extract values into variables 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Global Variables 

x = "awesome" 

def myfunc():
  print("Python is " + x)

myfunc() 
#Going to print the global 

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#Still going to print the global

#Keyword

def myfunc():
  #to make the variable global within the code
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



