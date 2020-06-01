
# Numbers

# Boolean
a = True
b = False
print(type(a), type(b))

c = 4 + True
print(c)

d = False
if d == 0:
    print('d is False')

print()


# Integers(int)
print(hex(143))
print(oct(143))
print(bin(143))
print()

print(2 + 3) # Add
print(2 - 3) # Subtract
print(2 * 3) # Multiply
print(3 / 2) # Divide (produces a float)
print(3 // 2) # Floor Divide (produces an integer)
print(3 % 2) # Modulo (remainder)
print(3 ** 2) # Power
print()


print(bin(10))
print(10 << 4) # Bit shift left
print(bin(160))
print(10 >> 2) # Bit shift right
print(bin(2))
print()

print(bin(10))
print(bin(9))
print(10 & 9) # Bit-wise AND
print(10 | 9) # Bit-wise OR
print(10 ^ 9) # Bit-wise XOR
print(~10) # Bit-wise NOT
print(abs(-10)) # Absolute Value
print()


# Floating point(float)
a = 37.45
b = 4e5

'''Floats are represented as double precision using the native CPU representation IEEE 754. This is the same as the double type in the programming language C.

17 digits or precision Exponent from -308 to 308'''

# Floating point numbers are inexact
a = 2.1 + 4.2
print(a == 6.3)
print(a)
print()

# math module
import math
print(math.sqrt(10))
print(math.sin(0))
print(math.cos(0))
print(math.tan(45))
print(math.log(10))
print()

# Comparison operators
print(3 < 2) # Less than
print(3 <= 2) # Less than or equal
print(3 > 2) # Greater than
print(3 >= 2) # Greater than or equal
print(3 == 2) # Equal to
print(3 != 2) # Not equal to
print()

# Logical operators
a,b,c = 10,20,30
if b >= a and b <= c:
    print('b is between a and c')
if not (b < a or b > c):
    print('b is still between a and c')
print()


# Converting Numbers
print(int(3.14159))
print(float('3.14159'))
print()

