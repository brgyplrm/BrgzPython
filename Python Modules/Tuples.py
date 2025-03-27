# Tuples

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Index is same with list
 
thistuple = ("apple", "banana", "cherry")
print(thistuple[0])

# The difference to the list tuple is unchangeable

# Allows duplicates 

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple length

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# tuple with one item

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple",)
print(type(thistuple))

# this is not a tuple 
thistuple = ("apple")
print(type(thistuple))

# Tuples can also contains same data type with list 

#================================================================================================================================================

# Access Tuple 

# same with list 

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#================================================================================================================================================

# Updating Tuples

# Because tuple and immutable and unchangeable 
# were going to convert it to list to change 

# Converting Tuples to List

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Append

# convert tuple to list and append
 
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# add tuple to tuple 

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# removing in tuple 

# same with append 

# convert to list 

histuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# or delete the entire tuple 

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)

#================================================================================================================================================
# Unpack Tuples

# Packing a tuple
fruits = ("apple", "banana", "cherry")

# Unpacking a tuple 
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using asterisk

#1
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#2
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic) = fruits

print(green)
print(tropic)

#================================================================================================================================================

# Looping in Tuple 

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Looping thru index

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Looping with while loop 

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#================================================================================================================================================
# Join Tuples
  
# Joining two tuples like in List 

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply tuples 

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#================================================================================================================================================

# Methods 

#count() = Returns the number of times a specified value occurs in a tuple
# index() = Searches the tuple for a specified value and returns the position of where it was found
