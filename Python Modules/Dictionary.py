# Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

# print certain item

# print brand
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


# Duplicate is not allowed, and if it duplicate it will over write existing values 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#================================================================================================================================================

# Access in Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# Using get method 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")

# Using keys 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys("model")

# Using values()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values("model")

# Using items()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items("model")

# Checking if key exist using 'in'

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values("model")

#================================================================================================================================================

# Changing the values 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# using update()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#================================================================================================================================================

# Adding items 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# update()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#================================================================================================================================================

# Removing items in Dict

# Using pop()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# Using pop()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# del

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# clear 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#================================================================================================================================================

# Loop in Dict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# using for loop 

# print dict one by one 
for x in thisdict:
  print(x)

# print all the values in dict 
for x in thisdict:
  print(thisdict[x])

# print all values in keys 
for x in thisdict.values():
  print(x)

# keys()
for x in thisdict.keys():
  print(x)

# using items()

for x, y in thisdict.items():
  print(x, y)

#================================================================================================================================================

# Copy dict

# copy()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# copying a dict to another dict using dict()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict) 

#================================================================================================================================================

# Nested Dictionary

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Or create three dictionary with same keys 

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# Loop Through Nested Dictionaries

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

#================================================================================================================================================

# Method          Description
# clear()         - Removes all the elements from the dictionary
# copy()          - Returns a copy of the dictionary
# fromkeys()      - Returns a dictionary with the specified keys and value
# get()           - Returns the value of the specified key
# items()         - Returns a list containing a tuple for each key-value pair
# keys()          - Returns a list containing the dictionary's keys
# pop()           - Removes the element with the specified key
# popitem()       - Removes the last inserted key-value pair
# setdefault()    - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()        - Updates the dictionary with the specified key-value pairs
# values()        - Returns a list of all the values in the dictionary

