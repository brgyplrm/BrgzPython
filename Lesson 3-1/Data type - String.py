# string 
print("Hello")
print('Hello')

# qoute inside qoute
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# accessing the string 
a = "Hello"
print(a)

#multi line string: you can use three qoute or single line qoute
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#string are arrays
a = "Hello, World!"
print(a[1])

#looping in string
for x in "banana":
  print(x)

#get the length of string
a = "Hello, World!"
print(len(a))

#to check the certain word is present in string we can use "in"
txt = "The best things in life are free!"
print("free" in txt)

# 'in' in if else 
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# check if the word is not in the string use "not"
txt = "The best things in life are free!"
print("expensive" not in txt)

# 'not' in if else 
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Slicing string

b = "Hello, World!"
#means we're getting the letter in the string starting in index 2 to 5
print(b[2:6])
#slicing from the start 
b = "Hello, World!"
print(b[:5])
# slicing to end 
print(b[2:])

#negative indexing
b = "Hello, World!"
print(b[-5:-2])

#Modifying String

#upper case
a = "Hello, World!"
print(a.upper())

#lowercase
a = "Hello, World!"
print(a.lower())

#remove whitespaces
a = " Hello, World! "
print(a.strip())

#replace string
a = "Hello, World!"
#replacing H by J
print(a.replace("H", "J"))

#splitting 
a = "Hello, World!"
print(a.split(","))

