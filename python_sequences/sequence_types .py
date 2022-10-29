# the sequence
	# is a positionally ordered collection of items. And you can refer to any item in the sequence by using its index number e.g., s[0] and s[1]
		# if the sequence s has n items, the last item is s[n-1]
	# python has the following built-in sequence types: lists, bytearrays, strings, tuples, range()(slicing), and bytes
	# sequence types are mutable and immutable
	# can be homogeneous or heterogeneous. In a homogeneous sequence, all elements have the same type. For example, strings are homogeneous sequences where each element is of the same typ
	# lists, however, are heterogeneous sequences where you can store elements of different types including integer, strings, objects, etc.
	# in general, homogeneous sequence types are more efficient than heterogeneous in terms of storage and operations

# the iterable
	# is a collection of objects where you can get each element one by one. Therefore, any sequence is iterable. For example, a list is iterable
	# however, the iterable may not be a sequence type. For example, a set is iterable but it’s not a sequence
	# generally speaking, iterables are more general than sequence types

# Checking if an item exists  

cities = ['San Francisco', 'New York', 'Washington DC']
print('New York' in cities)                                    # True

numbers = [1, 4, 5, 3, 5, 7, 8, 5]
print(numbers.index(5, 3))               					   # 4    # returns the index of the first occurrence of the number 5 after the third index
					
numbers = [1, 4, 5, 3, 5, 7, 8, 5]						
print(numbers.index(5, 3, 5))            					   # 4 index(item, after, before)
					
# Slicing:						
numbers = [1, 4, 5, 3, 5, 7, 8, 5]						
print(numbers[2:6:2])                    					   #[5, 5]   # step of 2