'''
Iterator: 
    # is an object that implements iterator protocol.
    # iterator protocol represents following methods:
        # __iter__ method that returns the object itself
        # __next__ method that returns the next item
    # condition validation:
        # If all the items have been returned, the method raises a StopIteration exception.
    '''


class Square:

    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.length:
            raise StopIteration

        self.current += 1
        return self.current ** 2


square = Square(6)                           # an iterator

print(square.__iter__())                      #<__main__.Square object at 0x0000020FB5B60A58>
print(square.__next__())                      #1

iterator_square = iter(square)
print(iterator_square)                         #<__main__.Square object at 0x000002481FE60AC8>
print(type(iterator_square))                   #<class '__main__.Square'>
print(id(iterator_square))                     #1755445725896

# 1 is already executed
print(next(iterator_square))                   # 4
print(next(iterator_square))                   # 9

# 1 , 4, 9 are already executed
for sq in square:
    print(sq)                                  #16 25 36
