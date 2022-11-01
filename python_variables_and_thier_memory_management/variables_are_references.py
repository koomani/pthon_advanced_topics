# Variables are JUST references:
	# variable is not a value LABEL 
	# variable references the object that holds a value => variables are just references

counter = 100                                 # python creates a new integer object in the memory and binds (links) the counter variable to that memory address
print(counter)            # 100               # while accessing counter variable, Python looks up the object referenced by the counter and returns the value of such object   
print(id(counter))        # 1721946896        # memory address => id(object reference)                                                                                           
print(hex(id(counter)))   # 0x66a2d310        # convert this address to a hexadecimal                                                        

# Object can have one or more references ( == variables)

counter = 100
max = counter
print(max, counter)                    # 100 100                      same inter value
print(id(max), id(counter))            # 1721946896 1721946896        same memory address

# WHEN does python delete object from memory?
	# pnce the object doesn’t have any reference, 
	# python Memory Manager (Garbage Collection) will destroy that object and reclaim the memory
	# accessing 0 refernce object raises NameErroor exception
	
counter = 100
max = counter
del counter                        # counter = None
print(max)                         # 100   object still in the memory 
print(counter)                     # NameError: name 'counter' is not defined

# Difference between lists and integers: (regarding multi-refernces - main difference between mutable and immutable)
	# fixed / flexible memory capacity

x = [10]
z = [10]
X = 10
Z = 10
print(x is z)         # False      # list is mutable - has more size value booked for appending more items - flexible memory capacity
					               # Python Memory Manager doesn’t reuse the existing list but creates a new one in the memory
print(x == z)         # True
print(X is Z)         # True       # int is immutable - fixed memory capacity
print(X == Z)		  # True			

# Object references number
import  ctypes
def ref_count(object_id: int) -> int:
    return ctypes.c_long.from_address(object_id).value

numbers = [1, 2, 3]
numbers_id = id(numbers)
print(ref_count(numbers_id))  # 1
ranks = numbers
print(ref_count(numbers_id))  # 2
ranks = None
print(ref_count(numbers_id))  # 1
numbers = None
print(ref_count(numbers_id))  # 0     # Python Memory Manager (Garbage Collection) destroied object [1, 2, 3] and reclaim the memory