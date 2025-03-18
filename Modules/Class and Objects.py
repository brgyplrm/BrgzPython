# CREATING CLASS 

class MyClass:
  x = 5

# CREATING OBJECT
p1 = MyClass()
print(p1.x)

# _init_() function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# _str_() function - function controls what should be returned when 
#                    the class object is represented as a string.

# without _str_() 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

# with _str_()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# object methods - Objects can also contain methods. 
#                  Methods in objects are functions that belong to the object.
class Person: 
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# self parameter - doesnt need to name it self but it need to be in the first parameter 
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# MODIFYING OBJECTS

# SET THE VALUE IN OBJECT 
p1.age = 40

# DELETING OBJECT PROPERTIES 
del p1.age

# DELETE THE OBJECT 
del p1

# PASS STATEMENT - THE CLASS CAN'T BE EMPTY SO IF YUNG CLASS AY BLANKO,
#                  PWEDE GAMITIN ANG PASS STATEMENT PARA DI MAG ERROR

class Person:
  pass 