from sys import getsizeof
from timeit import timeit

# Tuple vs. List: (over-allocating)

# the list is mutable. It means that you can add more elements to it (tuple TypeError)
# the storage efficiency of a tuple is greater than a list (tuple is faster than list) WHY?
	# because list is mutable. It means that you can add more elements to it, so Python needs to allocate more memory than needed to the list. This is called over-allocating. 
	# the over-allocation improves performance when a list is expanded.
	# Mmanwhile, a tuple is immutable therefore its element count is fixed. So Python just needs to allocate enough memory to store the initial elements.


	
fruits = ['apple', 'orange', 'banana']
print(f'The size of the list is {getsizeof(fruits)} bytes.')         # The size of the list is 80 bytes. []
fruits = ('apple', 'orange', 'banana')                          
# size of the tuple is 64 bytes.
print(f'The size of the tuple is {getsizeof(fruits)} bytes.')        # The size of the list is 72 bytes. ()
	
# copying a tuple is faster than a list
	# because copying a list, python creates a new list
	# when copying a tuple, Python just reuses an existing tuple. It doesn’t create a new tuple because tuples are immutable. Therefore, copying a tuple always slightly faster than a list
		# ** Copying tuple = adding new refernce to same object

fruit_list = ['apple', 'orange', 'banana']
fruit_list2 = list(fruit_list)
print(id(fruit_list) == id(fruit_list2))                             # False

fruit_tuple = ('apple', 'orange', 'banana')
fruit_tuple2 = tuple(fruit_tuple)
print(id(fruit_tuple) == id(fruit_tuple2))                           # True

# The following compares the time that needs to copy a list and a tuple 1 million times

times = 1_000_000
t1 = timeit("list(['apple', 'orange', 'banana'])", number=times)          # Time to copy a list 1000000 times: 0.2182912
print(f'Time to copy a list {times} times: {t1}')
t2 = timeit("tuple(('apple', 'orange', 'banana'))", number=times)         # Time to copy a tuple 1000000 times: 0.1376488
print(f'Time to copy a tuple {times} times: {t2}')
diff = "{:.0%}".format((t2 - t1)/t1)
print(f'difference: {diff}')                                              # difference: -37%