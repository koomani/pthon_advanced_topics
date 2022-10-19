# built-in class bool represents the boolean value True and False
# built-in class bool is just a subclass of int class
	# it means that bool class inherits all int class methods and props
	# plus it has specific behaviors related to boolean operations.
print(int(True), int(False))     # 1 0 (NOTE that True is Not the intger object with value 1) - python just intrepets True as 1
print(issubclass(bool, int))     # True
print(isinstance(True, bool))    # True
print(isinstance(False, bool))   # True

# How Python bool() constructor works under the hood :
    # Boolean constructor bool() accepts an object and returns True or False ->
    # In Python, a class always contains a definition of how its instances evaluate to True and False. In other words, every object can be either True or False.
    # All objects have a boolean value of True, except the following objects:
        # None   (x = True -> True)
        # False
        # 0 (0, 00, ..etc ) ( in any numeric type such as integer, float, and decimal.)
        # Empty sequences e.g., list, tuple, string.
        # Empty mapping types e.g., dictionary, set.
        # Custom classes that implement __bool__() or __len__() methods that return False or 0.

# The __bool__() method
    # during passing an object to the bool() constructor, Python returns the value of the __bool__() method of that object.

def __bool__(self):         # belong to the built class bool with def__init__ and method __bool__(self)
    return self != 0

print(bool(200))            # Python actually executes:  200.__bool__()    # True -- it is not 0    200 != 0 True
print(bool(0))              # False

# The __len__() method
    # If the class(list, set,...etc) of the object doesn’t have the __bool__() method, Python will return the result of __len__() method
    # If the result of the __len__() method is zero, the bool() returns False. Otherwise, it returns True. (Same as __bool__(self))
    # That’s why an empty list (len = 0) is always False while a list with at least one element is True.
	# ** if len(list) = 0 -> __len__(self) = 0, in such case it returns __bool__(self) => = 0 => False