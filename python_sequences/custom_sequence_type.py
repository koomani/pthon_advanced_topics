from functools import lru_cache


# custom Sequence type in Python (Python Fibonacci Sequence)
	# HOW to define a custom immutable sequence type
		# Basically, an immutable sequence type should support two main functions:
			# Return the number of elements of the sequence. Technically, this requirement is not necessary.    length
			# Return an element at a given index or raise an IndexError if the index is out of bounds.          Indexing
		#If an object can fullfil the above requirements, then you can:
			# Use the square brackets [] syntax to retrieve an element by an index.                             Indexing
			# Iterate over the elements of the sequence using the for loop, comprehension, etc.                 Looping
		# Technically, a custom sequence type needs to implement the following methods:
			# __getitem__ – returns an element at a given index.                                                Indexing                                   
			# __len__ – returns the length of the sequence.                                                     Length
				#1) __getitem__
					# has index argument(integer)
					# should return an element from the sequence based on the specified index
					# range of the index should be from "zero" to "length - 1"
					# If the index is out of bounds, __getitem__ should raise an IndexError
					# should support slicing
				#2) __len__
					# If a custom sequence has the __len__, you can use the built-in len()"length function" to get the number of elements from the sequence.

# Fibonacci sequence :it is sequence, each number is the sum of two numbers that precede it.
	# To calculate a Fibonacci number in Python, you define a recursive function

def fib(n):
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)
print(fib(5))          #8

def fib(n):
    print(f'Calculate Fibonacci of {n}')         # statement at the beginning of the fib() for the logging debugging purpose:
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)
fib(5)
'''
Calculate Fibonacci of 3
Calculate Fibonacci of 1
Calculate Fibonacci of 2
Calculate Fibonacci of 0
Calculate Fibonacci of 1
'''

# it has to calculate the Fibonacci of many times. This is not efficient. To solve this, Python provides a decorator called "lru_cache" from the functools module.
# lru_cache allows you to cache the result of a function.
# When you pass the same argument to the function, the function just gets the result from the cache instead of recalculating it


@lru_cache
def fib(n):
    print(f'Calculate the Fibonacci of {n}')
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)
fib(3)
'''
Calculate the Fibonacci of 3
Calculate the Fibonacci of 1
Calculate the Fibonacci of 2
Calculate the Fibonacci of 0
'''	

# Python Fibonacci sequence example -> You can save it as fibonacci.py module and use it in a new script.
from functools import lru_cache

class Fibonacci:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index > self.n - 1:
                raise IndexError
            return Fibonacci.fib(index)

    @staticmethod                                #define a static method that calculates a Fibonacci number of an integer
    @lru_cache(2**16)
    def fib(n):
        if n < 2:
            return 1
        return Fibonacci.fib(n-2) + Fibonacci.fib(n-1)
		
# Using fibonacci.py
#from fibonacci import Fibonacci
fibonacci = Fibonacci(10)

# access elements via indices
print('Accessing Fibonacci sequence using []:')
print(fibonacci[0])
print(fibonacci[1])
print(fibonacci[2])

print('Accessing Fibonacci sequence using for loop:')
# using for loop
for f in fibonacci:
    print(f)	
'''
Accessing Fibonacci sequence using []:
1
1
2
Accessing Fibonacci sequence using for loop:
1
1
2
3
5
8
13
21
34
55
'''
		
#Adding slicing support:

class Fibonacci:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index > self.n - 1:
                raise IndexError
            return Fibonacci.fib(index)
        else:
            indices = index.indices(self.n)
            return [Fibonacci.fib(k) for k in range(*indices)]

    @staticmethod
    @lru_cache
    def fib(n):
        if n < 2:
            return 1
        return Fibonacci.fib(n-2) + Fibonacci.fib(n-1)
		

fibonacci = Fibonacci(10)
print(fibonacci[1:5])                          # [1, 2, 3, 5]