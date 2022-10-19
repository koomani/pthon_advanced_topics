# Computers can not store integers directly.
	# only can store binary numbers(0, 1) to represent the integer objects
		# For example, to store 5 computers need to represent it using a BASE-2 number: 5 = 1 x 2**2 + 0 x 2**1 + 1 x 2**0 (3 bits)
		# 255= 1x 2**7 + 1 x 2**6 + 1 x 2**5 + 1x 2**4 + 1 x 2**3 + 1 x 2**2 + 1x 2**1 + 1 x 2**0  (8 bits)
	# storing both negative/positve integers and zero,it is needed to book 1 bit for storing the sign(+/-). so, with 8 bits:
    # the largest integer that the computers can represent is 2**7 = 127 ( at range of 8 Bits) and
    # computers can store all integers in the range (-127, 127)
#Because the number zero doesn’t have a sign, the computers can squeeze out an extra number. so, 8 bits can store all integers from -128 to 127. 8-bits = [-2**7, 2**7 – 1]
# 16-bits ~ [-2**15, 2**15 – 1] = [-32,768, 32,767]
# 32-bits ~ [-2**31, 2**31 – 1] = [-2,147,483,648, 2,147,483,647]
# 64-bits ~ [-2**63, 2**63 – 1] = [-9,223,372,036,854,775,808, 9,223,372,036,854,775,807]

# How Python represents integers?:
    # other programming languages like C# use a fixed number of bits to store integers
		# for example, C# has the int type that uses 32-bits and the long type that uses 64 bits to represent integers
    # Python, however, doesn’t use a fixed number of bit to store integers. Instead, Python uses a variable number of bits to store integers
        # For example, 8 bits, 16 bits, 32 bits, 64 bits, 128 bits, and so on. (Python is dynamically - tying langauge)
    # maximum integer number that Python can represent depends on the memory available
    # integers are objects that Python needs an extra fixed number of bytes as an overhead for each integer.(Python integer overhead)
    #It’s important to note that the bigger the integer numbers are, the slower the calculations such as +, -, … will be.


from sys import getsizeof

counter = 0
print(type(counter), getsizeof(counter))       #<class 'int'> 24

# python uses 24 bytes to store zero (needs only 1 bit)
	# 1 byte == 8 bits.
	# so, Python uses 24 bytes as an overhead for storing an integer object

print(type(100), getsizeof(100))               #<class 'int'> 28  # 24 bytes is an overhead, Python uses 4 bytes to represent the number 100.