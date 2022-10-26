from collections import namedtuple  


# Named Tuples  = tuple + class
	# a subclass of tuple class (just technically) -> issubclass => False
	# allow to create tuples and assign meaningful names to the positions of the tuple’s elements ( benefit -> more readable code)	
	# it is a regular tuple. Therefore, you can apply all tuple operations on a named tuple.

point = (100,200)       # represents a 2D point whose x-coordinate is 100 and y coordinate is 200
x = point[0]
y = point[1]            # this code works fine. However, it’s not so obvious.
						# when you look at the point[0], you need to know its implicitly meaning which doesn’t mention in the code

# To make the code more clear, you might want to use a class Point2D for example


class Point2D:                # The Point2D is a class, which is a subclass of the tuple

    def __init__(self, x, y):
        self.x = x
        self.y = y
a = Point2D(100, 200)
print(a.x)
print(a.y)

# To compare if two points are the same, you need to implement the __eq__ method:


class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        return False

a = Point2D(100, 200)
b = Point2D(100, 200)
print(a is b)             # False
print(a == b)             # True

# The Point2D might work as you expected, but this is a lot of code , solution is to create named tuple classes:

           
Point2D = namedtuple('Point2D',['x','y'])      # namedtuple function => accepts agruments as following as well
#Point2D = namedtuple('Point2D',('x','y'))
#Point2D = namedtuple('Point2D',('x, y'))
#Point2D = namedtuple('Point2D','x y')         # The field names must be valid variable names except that they cannot start with an underscore (_). line _y

# namedtuple function accepts the rename the keyword-only argument that allows you to rename invalid field names
	# however, when you use the rename argument, the namedtuple function automatically renames the _radius to a valid field name

#Circle = namedtuple('Circle', 'center_x, center_y, _radius')               # Error - _radius                        

Circle = namedtuple('Circle', 'center_x, center_y, _radius', rename=True)

print(Circle._fields)                #('center_x', 'center_y', '_2')
t = Circle(3, 4, 1)
print(t.center_x)                    #3

# Additional Python functions of named tuples
a = Point2D(100, 200)    
b = Point2D(100, 200)

print(a == b)  # True             # If you use the class, you need to implement the __eq__ to get this function.

print(a)       # Point2D(x=100, y=200)   # you can get the string representation of a named tuple: if you use the class, you need to implement __rep__ method

# Since a named tuple is a tuple, you can apply any function that is relevant to a regular tuple to a named tuple. For example:
print(max(a))  # 200
print(min(a))  # 100