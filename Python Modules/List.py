# LIST

# Create a list

thislist = ["apple", "banana", "cherry"]
print(thislist)

# List indexing

print(thislist[0:1])
# means the index 0 is the apple or the first 
# and the 1 is the banana but it non included in slicing

print(thislist[-2:-1])

# the -1 is the last in the list 
# and -2 is the second to the last

# List allowed duplicates 

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Get the list length using 'len()'

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List can hold a data type like: boolean, string, and int/float

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# can also contains one list with different data types 

list1 = ["abc", 34, True, 40, "male"]

# list constructor

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) 

# to specify that na list yun

#================================================================================================================================================
# Accessing LIST

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# negative indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# range indexing 

# parang string slicing lang 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# getting the first to the range of index
 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# getting the first index range to the last 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# negative indexing 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# if the item is exist in the list 
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# if the item is duplicated and you want to sort
thislist = ["d", "b", "a", "c","d","a","b"]

newlist = []
for item in thislist:
    if item not in newlist:
        newlist.append(item)
        newlist.sort()

print(newlist)

# changing the item in the list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# changing the items by the certain range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# if you want to add many items in a certaing index
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# replacing many items by a single item
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Inserting items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Append items 
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend list = means extending another list to one list using extend()

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Extend tuple, sets, dictionary to list 

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#================================================================================================================================================
# Removing certain item in the list
# remove()

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# removing one or many item 
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# removing item using pop with certain index 
# pop()

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# if no index it will remove the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# using index we can also use the del
# del

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# delete the entire list usign del
thislist = ["apple", "banana", "cherry"]
del thislist

# clearing the items in the list but the list is still but without items 
# clear ()

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#================================================================================================================================================
# Looping in List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Looping thru indexs
# range()
# len()

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# While loops 

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Using list comprehension

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# without list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#================================================================================================================================================

# list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Syntax of List Comprehension

#newlist = [expression for item in iterable if condition == True]

# only accept are not apple

newlist = [x for x in fruits if x != "apple"]

# with range function

newlist = [x for x in range(10) if x < 5]

# without if statement
newlist = [x for x in range(10)]

# Expression

newlist = [x.upper() for x in fruits]

# set the outcume what u want

newlist = ['hello' for x in fruits]

# returns 

newlist = [x if x != "banana" else "orange" for x in fruits]

#================================================================================================================================================
# Sorting 

# ascending 

# sort alphabeticaly
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# numerical

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# descending 

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Customized sort function

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# sorting methods 

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse order

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#================================================================================================================================================
# COPY LIST

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# Using List methods
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Using slice method 
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#================================================================================================================================================

# Join List 

# joining two list 

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# using append 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# using extend 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#================================================================================================================================================

# METHODS 

# append() - Adds an element at the end of the list
# clear() - Removes all the elements from the list
# copy() - Returns a copy of the list
# count() - Returns the number of elements with the specified value
# extend() - Adds the elements of a list (or any iterable) to the end of the current list
# index() - Returns the index of the first element with the specified value
# insert() - Adds an element at the specified position
# pop() - Removes the element at the specified position
# remove() - Removes the item with the specified value
# reverse() - Reverses the order of the list
# sort() - Sorts the list

