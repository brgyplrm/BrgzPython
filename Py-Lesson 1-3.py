# print() - for output print
print("Hello World fuckers")
# '#' - for a single line comment
"""Multi-line comment used print("Python Comments")  : ignores the string literals that are not assigned
to a variable. So, we can use these string literals as Python Comments."""
if 10 > 5:
   # indented by 4 spaces called block
   print("This is true!");print("semi colon")
   #using semi colon '#' for a multiple statement in one line
   print("I am tab indentation")
# pag di naka indent labas nasa block
print("I have no indentation")
# The first two print statements are indented by 4 spaces, so they belong to the if block.
# The third print statement is not indented, so it is outside the if block.

# input - for user input
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")
# pag mag iinsert ng variable sa print gumamit lang ng ","

# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
# .split() - splitting the values entered by user into separate variables by using .split()

# Single variable
s = "Cyd"
print(s)

# Multiple Variables
s = "Cyd"
age = 20
city = "Marigman Antipolo City"
print(s, age, city)

# Conditional Input from user

# Prompting the user for input
age_input = input("Enter your age: ")
# Converting the input to an integer
age = int(age_input)

# Checking conditions based on user input
if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Typecasting - by default input() input user as a string but if the user want to input int or float
#               we're going to use a type cast

# Python program to demonstrate implicit type Casting

# Python automatically converts
# a to int
a = 7
print(a)

# Python automatically converts
# b to float
b = 3.0
print(b)

# Python automatically converts
# c to float as it is a float addition
c = a + b
print(c)
print(type(c))
# the word "type((c)) just to specify kung ano yung data type naka loob sa variable"

# Python automatically converts
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))

# int to float
# int variable
a = 5

# typecast to float
n = float(a)
# initialize what type kung saan variable icoconvert
print(n)

# data types
# int - integer
# str - string
# float - float

# float to int
# int variable
a = 5.9

# typecast to int
n = int(a)

print(n)

# int to string
# int variable
a = 5

# typecast to str
n = str(a)
print(n)

# string variable
a = "5.9"

# typecast to float
n = float(a)
print(n)

# string variable
a = "5"
b = '1'

# typecast to int
n = int(a)

print(n)
print(type(n))

print(int(b))
print(type(b))

# OUTPUT FORMATTING

# string modulo operator(%)

print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))
# % - use for embedding values within the string, the string starts with % and end what type of character
print("Total students : %3d, Boys : %2d" % (240, 120))   # print integer value

print("%7.3o" % (25))   # print octal value

print("%10.3E" % (356.08977))   # print exponential value

# format method - format()
# This method allows for a more flexible way to handle string interpolation
#  by using curly braces {} as placeholders for substituting values into a string.
# Positional formatting with format() method

# Using indexed placeholders for string formatting
print("I love {0} for \"{1}!\"".format("Geeks", "Geeks"))

# {0} is replaced by the first argument 'Geeks'
print("{0} and Portal".format("Geeks"))

# Formatting with placeholders, {0} replaced by 'Geeks'
print("Portal and {0}".format("Geeks"))

# DATA TYPES
a = 5
# int  -They are often called just integers or ints,
#      are positive or negative whole numbers with no decimal point.
# long −Also called longs, they are integers of unlimited size,
#      written like integers and followed by an uppercase or lowercase L.
print(type(a))

b = 5.0
# float - Also called floats, they represent real numbers and are written with a
#         decimal point dividing the integer and fractional parts.
print(type(b))

c = 2 + 4j
# complex - A complex number is represented by a complex class.
#           It is specified as (real part) + (imaginary part)j
print(type(c))

#STRING
s = 'Welcome to the Geeks World'
print(s)

# check data type
print(type(s))

# access string with index
print(s[1])
print(s[2])
print(s[-1])

#LIST - Lists are just like arrays,
#       declared in other languages which is an ordered collection of data.

# Empty list
a = []

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed int and string
b = ["Geeks", "For", "Geeks", 4, 5]
print(b)

# ACCESSING LIST
a = ["0", "1", "2", "3"]
print("Accessing element from the list")
print(a[0])
print(a[2])

print("Accessing element using negative indexing")

# negative indexing means -1 is refers sa starts sa end, -3 refers to the first,
# and -2 refers to to the second to the last item

print(a[-1])
print(a[-3])
print(a[-2])

#TUPLE - is also an ordered collection of Python objects. The only difference between a
#        tuple and a list is that tuples are immutable. Tuples cannot be modified after
#        it is created.

# initiate empty tuple
tup1 = ()

tup2 = ('Geeks', 'For')
print("\nTuple with the use of String: ", tup2)

#ACCESS TUPLE
# to access the tuple items refer to the index number.
# Use the index operator [ ] to access an item in a tuple.

tup1 = tuple([1, 2, 3, 4, 5])

# access tuple items
print(tup1[0])
print(tup1[-1])
print(tup1[-3])

#DICTIONARY -  is a data structure that stores the value in key: value pairs.
# key - 1 -yung nag cocontain ng value
# values: 'Geeks' - yung value na laman ni key
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# create dictionary using { }
d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)

#ACCESSING DICTIONARY
d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])
# we can use by the key[] or using key.get[]
# Access using get()
print(d.get("name"))

#ADDING and UPDATING Dictionary Items
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"

print(d)

#Removing Dictionary Items
# del: Removes an item by key.
# pop(): Removes an item by key and returns its value.
# clear(): Empties the dictionary.
# popitem(): Removes and returns the last key-value pair.
d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# Using del to remove an item
del d["age"]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)

# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d.clear()
print(d)

# iteration through the dictionary
d = {1: 'Geeks', 2: 'For', 'age':22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")

# nested dictionary
d = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
# using the tab means yung key 3 may laman pa ulit like a whole block
print(d)




