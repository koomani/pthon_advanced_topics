# Iterator: is an object that implements
	# __iter__ method that returns the object itself
    # __next__ method that returns the next item
	# Note: such methods are known as the "iterator protocol"
	# if all the items have been returned, __next__ method raises a StopIteration exception
	# python allows to use iterators in "for" loops, comprehensions, and other built-in functions including "map", "filter", "reduce", and "zip"
	
class Square:                                # iterator class that returns the square numbers
    def __init__(self, length):
        self.length = length                 # length  and current are method attributes
        self.current = 0                     # "current" attribute keeps track of the current integer
											 # ** such attribute will be defined within the class methods and can be accessed via created object

    def __iter__(self):                      # THIS IS what makes class square an iterator => returns the self object
        return self

    def __next__(self):                      # THIS IS what makes class square an iterator => returns the next square object
        if self.current >= self.length:
            raise StopIteration              # If the number of square objects have been returned is greater than the length, the __next__ method raises the StopIteration exception
        self.current += 1
        return self.current ** 2

square = Square(5)                          # use of an iterator object

for sq in square:
    print(sq)                               # 1 4 9 16 25