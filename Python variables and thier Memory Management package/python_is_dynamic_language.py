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
print(message)         #100
print(id(message))     #1721946896
print(id("hello"))     #1858822980024
print(type(message))   #<class 'int'>