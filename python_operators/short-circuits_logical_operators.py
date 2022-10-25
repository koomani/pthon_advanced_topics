# and operator
	# "and"is a LOGICAL operator, used to operate on Boolean values and return a Boolean value
		# returns True if both operands evaluate to True. Otherwise, False
#short-circuits: 
	# if the first operand is False, "and" will not evaluate the second operand.
	# because the conclusion of outcome is already False
	
# or operators
	# "or"is a LOGICAL operator, used to operate on Boolean values and return a Boolean value
		# returns True if one operand evaluate to True. Otherwise, False
#lazy evaluation: 
	# if the first operand is True, "or" will not evaluate the second operand.
	# because the conclusion of outcome is already True
	
a = 10
b = 0
#c = a / b
#print(c)    

# since b is zero, the a / b definitely causes the division by zero exception
# however the following code doesnt cause such error

a = 10
b = 0
c = b and a/b            # False (0 = false) and doent evalute the second operand a /b because it is already false and c = 0
print(c)                 # 0  => print(int(False))

a = 10
b = 5
c = b and a/b            # True and evaluate the second operand
print(c)                 # 2.0

# above example shows that "and" can operate with non-Boolean values and returns a non-value boolean value.
# in general, you can use the and operator for the objects and you don’t need to use the bool() constructor:
    # object1 and object2 -> In this case, the and opeartor returns the object1 if it’s falsy. Otherwise, it returns the object2. (Ternary conditional operator)

#applications:

 
def avg(*numbers):

    total = sum(numbers)
    n = len(numbers)
    if n > 0:
        return total / n
    return 0 
print(avg(1, 2, 3))                             #2.0


def avg(*numbers):
    total = sum(numbers)
    n = len(numbers)
    return n and total / n      # return (n = False) and True  (Ternary conditional operator) # you can use and instead of if statement
print(avg(1, 2, 3))                             #2.0


# "or" application => set a default value : var = value or default

lang = input("Enter your favorite lang: ") or "Python"
print(lang)