# Operators

print(10 + 5)

#Arithmetic Operators
# Addition (+) - Adds two numbers together
print(10 + 10) 

# Subtraction (-) - Subtracts the second number from the first
print(20 - 10) 

# Multiplication (*) - Multiplies two numbers
print(10 * 10)  

# Division (/) - Divides the first number by the second (returns a float)
print(10 / 3)  

# Modulus (%) - Returns the remainder of division
print(10 % 3)  

# Exponentiation (**) - Raises the first number to the power of the second
print("exponent")
print(2 ** 3)

# Floor division (//) - Divides and rounds down to the nearest whole number
print(10 // 3)  


#Assignment Operators
# = (Assignment) - Assigns a value to a variable
x = 5
print(x)  # Output: 5

# += (Addition Assignment) - Adds a value to the variable and assigns the result
x += 3  # Equivalent to x = x + 3
print(x)  # Output: 8

# -= (Subtraction Assignment) - Subtracts a value from the variable and assigns the result
x -= 3  # Equivalent to x = x - 3
print(x)  # Output: 5

# *= (Multiplication Assignment) - Multiplies the variable by a value and assigns the result
x *= 3  # Equivalent to x = x * 3
print(x)  # Output: 15

# /= (Division Assignment) - Divides the variable by a value and assigns the result (float)
x /= 3  # Equivalent to x = x / 3
print(x)  # Output: 5.0

# %= (Modulus Assignment) - Computes the modulus of the variable and assigns the result
x %= 3  # Equivalent to x = x % 3
print(x)  # Output: 2.0

# //= (Floor Division Assignment) - Performs floor division and assigns the result
x = 10
x //= 3  # Equivalent to x = x // 3
print(x)  # Output: 3

# **= (Exponentiation Assignment) - Raises the variable to a power and assigns the result
x **= 3  # Equivalent to x = x ** 3
print(x)  # Output: 27

# &= (Bitwise AND Assignment) - Performs bitwise AND and assigns the result
x = 5  # Binary: 0101
x &= 3  # Binary: 0011 (Result: 0001)
print(x)  # Output: 1

# |= (Bitwise OR Assignment) - Performs bitwise OR and assigns the result
x = 5  # Binary: 0101
x |= 3  # Binary: 0011 (Result: 0111)
print(x)  # Output: 7

# ^= (Bitwise XOR Assignment) - Performs bitwise XOR and assigns the result
x = 5  # Binary: 0101
x ^= 3  # Binary: 0011 (Result: 0110)
print(x)  # Output: 6

# >>= (Right Shift Assignment) - Shifts bits to the right and assigns the result
x = 8  # Binary: 1000
x >>= 2  # Shift right by 2 (Result: 0010)
print(x)  # Output: 2

# <<= (Left Shift Assignment) - Shifts bits to the left and assigns the result
x = 2  # Binary: 0010
x <<= 2  # Shift left by 2 (Result: 1000)
print(x)  # Output: 8

# := (Walrus Operator) - Assigns a value to a variable as part of an expression
print(x := 3)  # Output: 3 (x is assigned 3 and printed)
print(x)  # Output: 3

#Comparison Operators
# == (Equal) - Checks if two values are equal
print(10 == 10)  # Output: True
print(10 == 20)  # Output: False

# != (Not Equal) - Checks if two values are not equal
print(10 != 10)  # Output: False
print(10 != 20)  # Output: True

# > (Greater Than) - Checks if the left value is greater than the right value
print(10 > 5)  # Output: True
print(10 > 20)  # Output: False

# < (Less Than) - Checks if the left value is less than the right value
print(10 < 20)  # Output: True
print(10 < 5)  # Output: False

# >= (Greater Than or Equal To) - Checks if the left value is greater than or equal to the right value
print(10 >= 10)  # Output: True
print(10 >= 20)  # Output: False

# <= (Less Than or Equal To) - Checks if the left value is less than or equal to the right value
print(10 <= 10)  # Output: True
print(10 <= 5)  # Output: False

#Logical Operators

#AND 
x = 3

# Both conditions are true
print(x < 5 and x < 10)  # Output: True

# One condition is false
print(x < 5 and x > 10)  # Output: False

#OR
x = 3

# At least one condition is true
print(x < 5 or x > 10)  # Output: True

# Both conditions are false
print(x > 5 or x > 10)  # Output: False

#NOT
x = 3

# Original condition is true, but `not` reverses it
print(not(x < 5))  # Output: False

# Original condition is false, but `not` reverses it
print(not(x > 10))  # Output: True

x = 3
y = 7

#COMBINING LOGICAL OPERATORS
# Combining `and` and `or`
print(x < 5 and y > 5)  # Output: True
print(x < 5 or y > 10)  # Output: True

# Combining `not` with other operators
print(not(x < 5 and y > 5))  # Output: False
print(not(x > 5 or y > 10))  # Output: True

#IDENTITY OPERATORS

#IS
x = [1, 2, 3]
y = x  # y refers to the same object as x

# Check if x and y are the same object
print(x is y)  # Output: True

# Create a new list with the same values
z = [1, 2, 3]

# Check if x and z are the same object
print(x is z)  # Output: False (even though they have the same values, they are different objects)

# DIFFERENCE OF IS AND ==
x = [1, 2, 3]
y = [1, 2, 3]

# Check for equality
print(x == y)  # Output: True (values are the same)

# Check for identity
print(x is y)  # Output: False (different objects in memory)

#IS NOT
#x = [1, 2, 3]
y = [1, 2, 3]  # y is a different object with the same values

# Check if x and y are not the same object
print(x is not y)  # Output: True

# Assign y to x
y = x

# Check if x and y are not the same object
print(x is not y)  # Output: False (they are the same object)

#MEMBERSHIP OPERATORS

#IN
# Check if a value is in a list
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # Output: True

# Check if a substring is in a string
text = "Hello, World!"
print("World" in text)  # Output: True

# Check if a key is in a dictionary
person = {"name": "Alice", "age": 25}
print("name" in person)  # Output: True

#NOT IN 
# Check if a value is not in a list
numbers = [1, 2, 3, 4, 5]
print(6 not in numbers)  # Output: True

# Check if a substring is not in a string
text = "Hello, World!"
print("Python" not in text)  # Output: True

# Check if a key is not in a dictionary
person = {"name": "Alice", "age": 25}
print("address" not in person)  # Output: True

#BITWISE OPERATORS
x = 5  # Binary: 0101
y = 3  # Binary: 0011

# & - AND
print(x & y)  # Output: 1 (Binary: 0001)

# | - OR
print(x | y)  # Output: 7 (Binary: 0111)

# ^ - NOR
print(x ^ y)  # Output: 6 (Binary: 0110)

# ~ - NOT 
print(~x)  # Output: -6 (Binary: 1010 in two's complement)

# << - ZERO FILL LEFT SHIFT
print(x << 2)  # Output: 20 (Binary: 10100)

# >> - ZERO FILL RIGHT SHIFT 
print(x << 2)  # Output: 20 (Binary: 10100)

# Operator Precedence Ranking (from highest to lowest):

# 1. () - Parentheses (highest precedence)
# 2. ** - Exponentiation
# 3. +x, -x, ~x - Unary plus, unary minus, and bitwise NOT
# 4. *, /, //, % - Multiplication, division, floor division, and modulus
# 5. +, - - Addition and subtraction
# 6. <<, >> - Bitwise left and right shifts
# 7. & - Bitwise AND
# 8. ^ - Bitwise XOR
# 9. | - Bitwise OR
# 10. ==, !=, >, >=, <, <=, is, is not, in, not in - Comparisons, identity, and membership operators
# 11. not - Logical NOT
# 12. and - Logical AND
# 13. or - Logical OR (lowest precedence)