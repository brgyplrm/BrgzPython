"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""

#str
x = "Hello World"
x = str("Hello World")

# int	
x = 20
x = int(20)	

#examples
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


#float
x = 20.5
x = float(20.5)

#examples 
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#float can also use scientific 
# numbers with an "e" to indicate the power of 10 

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(z)
print(type(y))
print(type(z))

#complex	
x = 1j
x = complex(1j)	

#examples
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#list
x = ["apple", "banana", "cherry"]
x = list(("apple", "banana", "cherry"))

#tuple
x = ("apple", "banana", "cherry")
x = tuple(("apple", "banana", "cherry"))

#range
x = range(6)		

#dict
x = {"name" : "John", "age" : 36}
x = dict(name="John", age=36)	

#set
x = {"apple", "banana", "cherry"}
x = set(("apple", "banana", "cherry"))

#frozenset
x = frozenset({"apple", "banana", "cherry"})
x = frozenset(("apple", "banana", "cherry"))

#bool
x = True
x = False
x = bool(5)

#bytes
x = b"Hello"
x = bytes(5)

#bytearray
x = bytearray(5)

#memoryview
x = memoryview(bytes(5))

#NoneType
x = None	



