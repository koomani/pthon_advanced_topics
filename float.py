from math import isclose, trunc, floor, ceil, copysign


# Python uses float class to represent real numbers
# Python float uses 8 bytes (64 bits) to represent real numbers. Unlike the integer, float type uses a fixed number of bytes
# Technically, Python uses 64 bits as follows:
	# 1 bit for sign (+ or -)
	# 11 bits for exponent 1.5e-5 1.5 x 10**-5 (exponent is -5) the range is [-1022, 1023].
	# 52 bits for significant digits (all digits except leading and trailing zeros)
		#For example, 0.25 has two significant digits, 0.125 has three significant digits, and 12.250 has four significant digits

print(float(1))                 # 1.0
# If you pass an object (obj) to the float(obj), it’ll delegate to the obj.__float__(). (object (=1) method for class Float():)
# If the __float__() is not defined, it’ll fall back to __index__()
# If you don’t pass any argument to the float(), it’ll return 0.0

print(float())                  # 0.0

print(float(0.1))               # 0.1

# Internally, Python can only represent 0.1 approximately.
# To see how Python represents the 0.1 internally, you can use the format() function.

print(format(0.1, '.20f'))                     #0.10000000000000000555           #Note: number of digits is infinite. We just show first 20 digits
# 0.1 is not 0.10000000000000000555 because Python represents some floats approximately, it will cause problems to compare 2 floating-point numbers

# Equality Testing case
x = 0.1 + 0.1 + 0.1
y = 0.3
print(x == y)                                   # False
print(format(x, '.20f'))                        # 0.30000000000000004441
print(format(y, '.20f'))                        # 0.29999999999999998890
print(round(x, 3) == round(y, 3))               # True # The Solution: by rounding (doesn’t work in all cases)

# PEP485( A Function for testing approximate equality) provides a solution that fixes this problem by using relative and absolute tolerances.                    
print(isclose(x, y))                            #True

# Convert Float to Int - math module for converting from a float to an int, including:
    # Truncation, Floor, Ceiling

print(trunc(12.2))                 #12
print(trunc(12.5))                 #12
print(trunc(12.7))                 #12

# same as int class
print(int(12.2))                   #12
print(int(12.5))                   #12
print(int(12.7))                   #12

print(floor(12.2))                 #12
print(floor(12.5))                 #12
print(floor(12.7))                 #12

# negaitvie flooring                       
print(floor(-12.7))           #-13
print(trunc(-12.7))           #-12
print(int(-12.7))             #-12

print(ceil(12.7))             #13
print(ceil(-12.7))            #-12

# rounding
    #The round() function rounds the number to the closest multiple of 10**-ndigits.
print(round(1.25))          # 1.0           # by default is round(var, ndigits = 0 by default) = round(1.25, 0)   10**(-0) = 1
print(round(15.5, -1))      #20.0           # 10**(-1)??
    # When you round a number situated in the middle of two numbers, Python cannot find the closest number. (solution is rounding with ties)
        # In this case, Python uses the IEEE 754 standard for rounding, called the banker’s rounding
        # In the banker’s rounding, a number is rounded to the nearest value, with ties rounded to the nearest value with an even least significant digit
            #Generally, a least significant digit in a number is the right most digit.
print(round(1.25, 1))   #1.2 (between 1.2 and 1.3) 1 = 0.05 => 1.2 or 1.3

    # How to round away from zero by int(x + 0.5)
print(int(1.2 + 0.5))            #1
print(int(1.5 + 0.5))            #2

    #However, it doesn’t work for the negative numbers:    For negative numbers, you should subtract 0.5 instead of adding it.
print(int(-1.2 + 0.5))           #0
print(int(-1.5 + 0.5))           #-1

print(int(-1.2 - 0.5))           #-1
print(int(-1.5 - 0.5))           #-2
    # The following defines a helper function that rounds up a number

def round_up(x):
    if x > 0:
        return int(x + 0.5)
    return int(x - 0.5)

# copysign() function to develop a round_up() function without checking whether x is positive or negative
# math.copysign(x, y) x is the absolute value and y is the sign


def round_up(x):
    return int(x + copysign(0.5, x))
print(round_up(-1.2))                       #-1