# Python is dynamic_typing langauge:

	# statically typed language like c#
'''
	string message = "hi"     # define data type when declare the varible "message" 
	message = "Hello"         # re-declare the string "message" 
	int message = 2           # Error  you can not modify the data type for same object
'''

	# dynamically typed language like Python

message = "hello"      # message is just a refrence to the string object "hello"
message = 100
print(message)         # 100
print(id(message))     # 1721946896           # such reference is linked to another object 
print(id("hello"))     # 1858822980024        # such objects still stored in the memory without reference
print(type(message))   # <class 'int'>

# Difference between del and None keywords:

x = 10
del x
# print(x)                    # del deletes the object and refernce

x = 10 
x = None                      # refernce x is now linked to object class None, and int 10 is still stored in the memory 
print(x)                      # None
print(10)				      # 10          # 10 object still not None in memory (count is just referencence not LABEL)