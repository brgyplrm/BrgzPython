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

#String Concatenation

#merging a and b to c
a = "Hello"
b = "World"
c = a + b
print(c)

#add space between a and b
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String formatting 

#fstring = f"{variable}"

# putting the f string in the variable
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# or using the print f string method 
price = 59
age = 36
print(f"The price is {price} dollars")
print(f"My name is John, I am {age}")

# place holder and modifiers 

#add decimal points or specific decimal 
price = 59
print(f"The price is {price:.2f} dollars ")

#perform math operation
print(f"The price is {20*10:.2f} dollars") 

#ESCAPE CHARACTERS

print("We are the so-called \"Vikings\" from the north.")


# Escape Characters:

# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value


#String Methods 

# capitalize()	Converts the first character to upper case 
print("Hello, And Welcome To My World!".capitalize())

# casefold()	Converts string into lower case
print("Hello, And Welcome To My World!".casefold())

# center()	Returns a centered string
print("Banana".center(23))

# count()	Returns the number of times a specified value occurs in a string
print("Banana".count("a"))

# encode()	Returns an encoded version of the string
print("Bånånå".encode())

# endswith()	Returns true if the string ends with the specified value
print("Hello, And Welcome To My World!.".endswith("."))
print("Hello, And Welcome To My World!".endswith("."))

# expandtabs()	Sets the tab size of the string
print("H\te\tl\tl\to".expandtabs(2))

# find()	Searches the string for a specified value and returns the position of where it was found
print("Hello, And Welcome To My World!".find("Welcome"))

# format()	Formats specified values in a string
print("{} World!".format("Hello"))

# format_map()	Formats specified values in a string
print("{greeting} World!".format_map({"greeting": "Hello"}))

# index()	Searches the string for a specified value and returns the position of where it was found
print("Hello, And Welcome To My World!".index("Welcome"))

print("Hello, And Welcome To My World!"[11])

# isalnum()	Returns True if all characters in the string are alphanumeric
print("Hello, And Welcome To My World!".isalnum())

# isalpha()	Returns True if all characters in the string are in the alphabet
print("Hello And Welcome To My World".isalpha())

# isascii()	Returns True if all characters in the string are ascii characters
print("Hello, And Welcome To My World!".isascii())

# isdecimal()	Returns True if all characters in the string are decimals
print("Hello, And Welcome To My World!".isdecimal())

# isdigit()	Returns True if all characters in the string are digits
print("Hello, And Welcome To My World!".isdigit()) 

# isidentifier()	Returns True if the string is an identifier
print("Hello, And Welcome To My World!".isidentifier())

# islower()	Returns True if all characters in the string are lower case
print("Hello, And Welcome To My World!".islower()) 

# isnumeric()	Returns True if all characters in the string are numeric
print("Hello, And Welcome To My World!".isnumeric())

# isprintable()	Returns True if all characters in the string are printable
print("Hello, And Welcome To My World!".isprintable())

# isspace()	Returns True if all characters in the string are whitespaces
print("Hello, And Welcome To My World!".isspace())

# istitle()	Returns True if the string follows the rules of a title
print("Hello, And Welcome To My World!".istitle())

# isupper()	Returns True if all characters in the string are upper case
print("Hello, And Welcome To My World!".isupper())

# join()	Joins the elements of an iterable to the end of the stringljust()	Returns a left justified version of the string
print("-".join(["Hello", "World"]))

# lower()	Converts a string into lower case
print("Hello, And Welcome To My World!".lower())

# lstrip()	Returns a left trim version of the string
print("   Hello, And Welcome To My World!".lstrip())

# maketrans()	Returns a translation table to be used in translations
trans_table = str.maketrans("aeiou", "12345")
print("Hello, And Welcome To My World!".translate(trans_table))

# partition()	Returns a tuple where the string is parted into three parts
print("Hello, And Welcome To My World!".partition("To"))

# replace()	Returns a string where a specified value is replaced with a specified value
print("Hello, And Welcome To My World!".replace("World", "Universe"))

# rfind()	Searches the string for a specified value and returns the last position of where it was found
print("Hello, And Welcome To My World!".rfind("p"))

# rindex()	Searches the string for a specified value and returns the last position of where it was found
print("Hello, And Welcome To My World!".rindex("o"))
print("Hello, And Welcome To My World!"[-27])

# rjust()	Returns a right justified version of the string
print("Hello".rjust(10, "-"))

# rpartition()	Returns a tuple where the string is parted into three parts
print("Hello, And Welcome To My World!".rpartition("To"))

# rsplit()	Splits the string at the specified separator, and returns a list
print("Hello, And Welcome To My World!".rsplit(" ", 2))

# rstrip()	Returns a right trim version of the string
print("Hello, And Welcome To My World!   ".rstrip()) 

# split()	Splits the string at the specified separator, and returns a list
print("Hello, And Welcome To My World!".split(" "))

# splitlines()	Splits the string at line breaks and returns a list
print("Hello\nAnd Welcome\nTo My World!".splitlines())

# startswith()	Returns true if the string starts with the specified value
print("Hello, And Welcome To My World!".startswith("Hello"))

# strip()	Returns a trimmed version of the string
print("   Hello, And Welcome To My World!   ".strip())

# swapcase()	Swaps cases, lower case becomes upper case and vice versa
print("Hello, And Welcome To My World!".swapcase())

# title()	Converts the first character of each word to upper case
print("hello, and welcome to my world!".title()) 

# translate()	Returns a translated string
trans_table = str.maketrans("aeiou", "12345")
print("Hello, And Welcome To My World!".translate(trans_table))

# upper()	Converts a string into upper case
print("Hello, And Welcome To My World!".upper())

# zfill()	Fills the string with a specified number of 0 values at the beginning
print("42".zfill(5)) 


