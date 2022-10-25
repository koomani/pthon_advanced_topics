# Identity "is" operator
	# compares two variables and returns True if they reference the same object BECAUSE
	# compares the identity of two variables (id memory address)
	# to check if a and b reference the same object
	# "is" about memory object but "==" about value object
	# (id memory => identity operator is)
	# to negate the is operator, you use the "is not" operator

a = 100
b = a
print(a is b)                         # True
a = 100
b = 100                               # multi_reference object
print(a is b)                         # True

# lists are MUTABLE objects. 
	# Python Memory Manager doesn’t reuse the existing list but creates a new one in the memory
	
ranks = [1, 2, 3]
rates = [1, 2, 3]
print(ranks is rates)                     # False
print(ranks is not rates)                 # True


# Equality operator (==)
	# compares two variables for equality and returns True if they are equal
	# to negate the is operator, you use the "!=" operator

a = 100
b = a
print(a is b)                         # True
print(a == b)                         # True  # Since a and b references the same object, they’re both identical and equality

ranks = [1, 2, 3]
rates = [1, 2, 3]
print(ranks is rates)                 # False
print(ranks == rates)                 # True
print(ranks != rates)                 # False