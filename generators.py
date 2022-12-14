from sys import getsizeof


# Generator function
	# python executes the function from top to bottom based on the run-to-completion model
	# it means tha python cannot pause the function midway and then resumes it after that
	# python function generally ends with print() display statment, return, or yield
	# generator is such function that contains at least one yield statement
		# to pause a function midway and resume from where the function was paused
		# when you call a generator function, it returns a new generator object
		# when python meets the yield statement, it returns the value specified in the yield. In addition, it pauses the execution of the function
		# If we “call” the same function again, python will resume from where the previous yield statement was encountered, ..and go on till the last "yield"
	# Generator objects (or generators) implement the iterator protocol. In fact, generators are "lazy iterators"
		#Therefore, to execute a generator function, you call the next().
	
def func():              
    print('start')
    yield 1
    print('midway')
    yield 2
    print('finish')
    yield 3

for i in func():           
    print(i)

'''
start
1
midway
2
finish
3
'''

message = func()
result = next(message)
print(result)               # func() pauses at the yield

'''
start
1
'''

result = next(message)    # after calling execaute again   .. till the last yield and then if you call it -> StopIteration error
print(result)

'''
How are you?
2
'''

# Using Python generators to create iterators


class Squares:
    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current ** 2
        self.current += 1
        if self.current > self.length:
            raise StopIteration
        return result

square = Squares(5)
for s in square:
    print(s)                   # 0, 1, 4, 9, 16

# above code works as we expected. But it has one issue that there’s a lot of boilerplate-> rewrites the Squares iterator as a generator function


def squares(length):
    for n in range(length):
        yield n ** 2

for s in Squares(5):           
    print(s)                   # 0, 1, 4, 9, 16


# Generator Expression 
	# such expression that returns a generator object
	# it is like a list comprehension in terms of syntax. For example, a generator expression also supports complex syntaxes including:
		# if statements
		# nested loops
		# nested comprehensions
		
	# Memory: generator object is more efficient than list becasue
		# the list comprehension returns a list while a generator expression returns a generator object
		# it means that the list comprehension returns a complete list of elements upfront. However, the generator expression returns a list of elements, one at a time, based on request
		# the list comprehension is eager while the generator expression is lazy
		# in other words, the list comprehension creates all elements right away and loads all of them into the memory
		# conversely the generator expression creates a single element based on request. It loads only one single element to the memory
		
	# Iterable vs iterator:
		# A list comprehension returns an iterable. It means that you can iterate over the result of a list comprehension again and again
		# However, a generator expression returns an iterator, specifically a lazy iterator. It becomes exhausted when you complete iterating over it
	

square_list = [n** 2 for n in range(5)]                # list comprehension []
print(getsizeof((square_list)))                        # 128
print(square_list)                                     # [0, 1, 4, 9, 16]

square_generator = (n** 2 for n in range(5))	       # generator expression ()
print(getsizeof((square_generator)))                   # 88
print(square_generator)                                # <generator object <genexpr> at 0x0000025CC5FC2030>
for i in square_generator:
    print(i)                                           # 0, 1, 4, 9, 16