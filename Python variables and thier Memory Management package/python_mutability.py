# Mutable and immuable (fixed memory capacity) in Python
	# mutable object (list, set, dic) = object whose internal state can be changed and versa verse for
	# immutable (numbers(int, float),bool , string, tuple, frozen set)
	# user-defined classes can be mutable or immutable, depending on whether their internal state can be changed or no (private, public, protected ? )
	
counter = 100
print(id(counter))   # 1721946896
counter =200					    # Python creates a new integer object with the value 200 and reassigns the counter variable
print(id(counter))   # 1721950096   #The reassignment doesn’t change the value of the first integer object. It just reassigns the reference					            
print(id(100))       # 1721946896   # 100 object still not None in memory (count is just referencence not LABEL)

# immutable objects are not something frozen or absolutely constant

low = [1, 2, 3]
high = [4, 5]
rankings = (low, high)        # immutable tuple
high.append(6)
print(rankings)               #([1, 2, 3], [4, 5, 6])