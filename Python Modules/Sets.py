# Sets

myset = {"apple", "banana", "cherry"}

# Sets are Unchangeable

# Sets are Unsorted 

# Sets and not allowed to duplicate

# duplicates are ignored

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# True and 1 is same value with set so it can be duplicate

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

# same with False and 0

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

# Lenght of Set

thisset = {"apple", "banana", "cherry", "apple"}

print(len(thisset))

# Data types same with list and tuple 

set1 = {"apple", "banana", "cherry"}
set2 = {1,2,3,4,5,6,7}
set3 = {True, False}

# can also contains diff data types 

thisset = {"apple", "banana", "cherry",1,2,3,4,5,6,7}

#================================================================================================================================================

# Access Items in Set

# Access through loop

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#================================================================================================================================================

# Adding Items in Sets 

# using add() function

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# add another sets to another sets using update() function

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# adding iterable (dict, list, and tuples) to set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#================================================================================================================================================

# removing items in sets using remove() function

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# using discard()

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# using pop - but you need to specify a item cause a random item will going to remove

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# using clear 

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# using del

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#================================================================================================================================================

# Looping in sets 

# for loop

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#================================================================================================================================================

# Join sets 

# using union - joining sets using union to another new set

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# can also use | as union

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# multiple sets using union()

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# multiple using | 

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

# joining tuple to sets using union

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# Update - inserts item to another set

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Intersection - join but sort the only items that present in both sets 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# can also use & for intersection

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# intersection_update() - gets the duplicate item and join in the present set

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

# Difference - returns that items are not present in second set 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

# using - for difference

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

# difference_update() - keeps item that are not present in both set

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set3)

# symmetric_difference - keep only the elements that are NOT present in both sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

# using ^ as symmetric_difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ (set2)
print(set3)

# symmetric_difference_update() - keep all but the duplicates, but it will change 
#                                 the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

