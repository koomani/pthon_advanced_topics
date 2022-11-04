from time import perf_counter
import decimal
from decimal import Decimal
	
	
# context manager
	# such object that defines a runtime context executing within the "with" statement

f = open('data.txt', 'r')
data = f.readlines()              # returns list of strings
print(data)
f.close()                         # ['100']

f = open('data.txt', 'r')
data = f.readlines()
print(int(data[0]))
f.close()                         # 100

# if the data.txt contains the string '100' instead of the integer 100, you’ll get the following error:
    # ValueError: invalid literal for int() with base 10: "'100'"
    # because of this exception, python may not close the file properly -> to fix it use try except finally statements

try:
    f = open('data.txt')
    data = f.readlines()
    print(int(data[0]))           # 100
except ValueError as error:
    print(error)
finally:
    f.close()

# above solution is quite verbose(long), so python provides you better automatic way to close the file after processing
    # context managers
    # after with block -> python will close the file automatically -> why use context mamager is better :)

with open('data.txt') as f:
    data = f.readlines()
    print(int(data[0]))              #100
print(f.closed)                      # True

# context manager protocol
    # python context managers work based on the context manager protocol
    # The context manager protocol has the following dunder methods
        # __enter__() – setup the context and optionally return some object
        # __exit__() – cleanup the object.	
		# If you want a class to support the context manager protocol, you need to implement these two methods.(General rule for all  iterable, generator ...all protocols)
	
# let us suppose that contextmanager is a class
	# with ContexManager as f -> with statmenet, python implicity creates instance for the class ContextManager and automatically call __enter__ method on this instance
	# __enter__ returns an object and python assigns this object to the "f"
	# Note: "f" references the object returns the __enter__ not the class ContextManager
	# "with" block always will call __exit__  even in case an exception occures

# The __exit__(): -> bool
	# method accepts three arguments: exception type, exception value, and traceback object. All of these arguments will be None if no exception occurs
		# def __exit__(self, ex_type, ex_value, ex_traceback):
	# returns a boolean value, either True or False
	# If the return value is True, Python will make any exception silent. Otherwise, it doesn’t silence the exception.

# Functionally, with statement = try, finally statments (another option to if you want to avoid context manager to handle close file properly)

# ContexManager applications:
	# 1. open - close: files /resource automatically like socket
	# 2. Lock – release: Python Concurrency 
	# 3. Start – stop:  start a timer and stop it automatically
	# 4. Change – reset

'''
For example, your application needs to connect to multiple data sources. And it has a default connection.
To connect to another data source:
    First, use a context manager to change the default connection to a new one.
    Second, work with the new connection
    Third, reset it back to the default connection once you complete working with the new connection.
'''

# Implementing Python context manager protocol   (1. open - close)


class File:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print(f'Opening the file {self.filename}.')
        self.__file = open(self.filename, self.mode)
        return self.__file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f'Closing the file {self.filename}.')
        if not self.__file.closed:
            self.__file.close()
        return False

with File('data.txt', 'r') as f:
    print(int(next(f)))


# Using Python context manager to implement the start and stop pattern (3. Start – stop)


class Timer:

    def __init__(self):
        self.elapsed = 0

    def __enter__(self):                       #start the timer
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop = perf_counter()              # stop the timer
        self.elapsed = self.stop - self.start
        return False

def fibonacci(n):
    f1 = 1
    f2 = 1
    for i in range(n-1):
        f1, f2 = f2, f1 + f2
    return f1

with Timer() as timer:
    for _ in range(1, 1000000):
        fibonacci(1000)
	
print(timer.elapsed)

	
# Decimal module
x = Decimal('2.25')
y = Decimal('3.35')
with decimal.localcontext() as ctx:
    print('Local context:')
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1), round(y, 1))  
print('Global context:')
print(round(x, 1), round(y, 1))

# Note: local context doesn’t affect global context. After "with" block, Python uses the default rounding mechanism

#Local context:
#2.3 3.4
#Global context:
#2.3 3.4