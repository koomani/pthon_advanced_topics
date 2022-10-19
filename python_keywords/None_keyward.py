# None
	# None is a special object of the NoneType class.
	# None is not zero (0, 0.0, …) not False, Not empty string('')
	# comparing None to any value will return False except None itself.
	
x = None
print(type(x), type(None))            # <class 'NoneType'> <class 'NoneType'>
print( 1 == None)                     # False
print(x == None)                      # True

# What is the different between del and None Python?

x = 1
x = None # will free whatever it referenced but keep the name around even though it’s just referencing None (which is a type, NoneType).
print(type(x))                     # <class 'NoneType'>

x = 1
del x    # will completely remove both the name and what it referenced.
print(type(x))                    # NameError: name 'x' is not defined

# Python creates only one None object at runtime. So, if you use the equality (==) or "is" to compare None with None => True

print(None == None)                 # True (reuse the same object id)
print(None is None)                 # True

# It’s a good practice to use the "is" or "is not" operator to compare a value with None. (id memory => identity operator is)
	# The reason is that the user-defined objects may change the equality operator’s behavior by overriding the __eq__()
	
	
class Apple:

    def __eq__(self, other):       # objec self == anything even None
        return True
		
apple = Apple()
print(apple == None)     #True     # Note: you cannot override the "is" behavior like you do with the equality operator (==)
print(apple is None)     # False

# Applications of None object:
		
		# 1. To destroy object refernce:
x = "string"
x = None
print(x)         # NameError exception 

	#2. As an initial value for a variable
	
state = None             # if variable doesn’t have any meaningful initial value, you can assign None
if state is None:
    print("state has no meaningful object")

	#3. To fix the mutable default argument issue
	
	
def func(color: str, colors=[]) -> list:                # GOOD EXAPMPLE WHERE TO USE DEFAULT PARAMETERS
    colors.append(color)
    return colors
	
	
print(func("green"))

hsl = func('hue')                      #['green']
print(hsl)                             #['green', 'hue'] colors=[] has been created just in first func() caller


def func(color: str, colors=None) -> list:
    if colors is None:
        colors = []
        colors.append(color)
    return colors
	
print(func("green"))

hsl = func('hue')                      #['green']          # This override the default parameter colors = None (Now colors = ["green"]
print(hsl)                             #['hue']

	#4. As a return value of a function
	
	
def say(something):
    print(something)
	
result = say('Hello')                    # Hello
print(result)                            # function doesnt return a value --> so returns None