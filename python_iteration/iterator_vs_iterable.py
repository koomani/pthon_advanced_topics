# iterator:
	# object that implements the iterator protocol
		#__iter__ returns the iterator object itself
		#__next__ returns the next element
# iterable
	# object that you can iterate over
	# the object is iterable when it implements the __iter__ method, and its __iter__ method returns a new iterator

# examining the built-in list and list iterator
	# list is an ordered collection of items. It’s also an iterable because a list object has the __iter__ method that returns an iterator

numbers = [1, 2, 3]
number_iterator = numbers.__iter__()     # __iter__ method returns an iterator with the type list_iterator
print(type(number_iterator))             # <class 'list_iterator'>

# because the list_iterator implements the __iter__ method, you can use the iter built-in function to get the iterator object

numbers = [1, 2, 3]
number_iterator = iter(numbers)
print(number_iterator)                 # <list_iterator object at 0x000001B7FF2B9080>

# since the list_iterator also implements the __next__ method, you can use the built-in function next to iterate over the list

numbers = [1, 2, 3]
number_iterator = iter(numbers)
print(next(number_iterator))     #1
print(next(number_iterator))     #2
print(next(number_iterator))     #3    # If you call the next function once more, you’ll get a StopIteration exception(the list iterator has been exhausted)


class Colors:                # Colors class plays two roles: iterable( implements the __iter__ method that returns an object itself, which is an iterator) and iterator (implements both __iter__ and __next__)
    def __init__(self):
        self.rgb = ['red', 'green', 'blue']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.rgb):
            raise StopIteration
        color = self.rgb[self.index]
        self.index += 1
        return color
colors = Colors()
for color in colors:
    print(color)                      # To iterate again, you need to create a new colors object with the rgb attribute. This is inefficient

# Separating an iterator from an iterable


class Colors:
    def __init__(self):
        self.rgb = ['red', 'green', 'blue']

    def __len__(self):
        return len(self.rgb)


class ColorIterator:
    def __init__(self, colors):
        self.__colors = colors
        self.__index = 0

    def __iter__(self):
        return self                 

    def __next__(self):
        if self.__index >= len(self.__colors):
            raise StopIteration
        color = self.__colors.rgb[self.__index]
        self.__index += 1
        return color

colors = Colors()
color_iterator = ColorIterator(colors)

for color in color_iterator:            
    print(color)

	
# When you want to iterate the Colors object, you need to manually create a new ColorIterator object. And you also need to remember the iterator name ColorIterator.
# It would be great if you can automate this. To do it, you can make the Colors class iterable by implementing the __iter__ method

class Colors:
    def __init__(self):
        self.rgb = ['red', 'green', 'blue']

    def __len__(self):
        return len(self.rgb)

    def __iter__(self):
        return ColorIterator(self)           #  method returns a new instance of the ColorIterator class

#Now, you can iterate the Colors object without explicitly creating the ColorIterator object

colors = Colors()
for color in colors:
    print(color)
	
# The following places the ColorIterator class inside the Colors class to encapsulate them into a single class	

class Colors:
    def __init__(self):
        self.rgb = ['red', 'green', 'blue']

    def __len__(self):
        return len(self.rgb)

    def __iter__(self):
        return self.ColorIterator(self)

    class ColorIterator:
        def __init__(self, colors):
            self.__colors = colors
            self.__index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.__index >= len(self.__colors):
                raise StopIteration

            # return the next color
            color = self.__colors.rgb[self.__index]
            self.__index += 1
            return color