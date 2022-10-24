# closure nested function and an extended scope that contains free variables
	# nested function: defined function inside outer function
	# Free variable: declared in the nonlocal scope
# closure is a nested function that references one or more variables (free variables) from its enclosing scope


def say():
    greeting = 'Hello'
    def display():
        print(greeting)
    return display          # this is called returning a closure	

fn = say()					# say() is a function assigned to variable "fn" -> execauted first

fn()                        # Since fn() (is the closure is) a function, you can execute it (after say() finished     #Hello

# say() executes and returns a function. When the fn() executes, the say() already completes.
# in other words, the scope of the say() was gone at the time the fn function executes.
# since the greeting variable belongs to the scope of the say function, it should also be destroyed with the scope of the function.
# however, you still see that fn displays the value of the message variable???

#Python cells and multi-scoped variables
	# The value of the greeting variable is shared between two scopes of:
		# The say function.
		# The closure
	# To achieve this, Python creates an intermediary object called a cell
	# To find the memory address of the cell object, you can use the __closure__ property 
	
print(fn.__closure__)                     #(<cell at 0x0000017184915C40: str object at 0x0000017186A829B0>,)      

# the __closure__ returns a tuple of cells
# memory address of the cell at 0x0000017184915C40 and string object at 0x0000017186A829B0.

# if you display the memory address of the string object in the say function and closure, you should see that they reference the same object in the memory


def say():
    greeting = 'Hello'
    print(hex(id(greeting)))

    def display():
        print(hex(id(greeting)))
        print(greeting)
    return display
	
fn = say()

fn()                       # 0x17186a829b0   0x17186a829b0

# when you access the value of the greeting variable, Python will technically “double-hop” to get the string value.
# this explains why when the say() was out of scope, you still can access the string object referenced by the greeting variable.
# based on this mechanism, you can think of a closure as a 
	#function and an extended scope that contains free variables.
# to find the free variables that a closure contains, you can use the __code__.co_freevars

print(fn.__code__.co_freevars)                # ('greeting',)

# when Python creates the closure:
	# python creates a new scope when a function executes ->>>
	# if that function creates a closure, Python also creates a new closure as well

	
def multiplier(x):
    def multiply(y):
        return x * y
    return multiply
	
m1 = multiplier(1)       # call the multiplier
print(m1(10))            # call the closure  # 10

# Python closures and for loop

multipliers = []
for x in range(1, 4):
    multipliers.append(lambda y: x * y)
m1, m2, m3 = multipliers

print(m1(10))                   #30
print(m2(10))                   #30
print(m3(10))                   #30

 # better approach


def multiplier(x):                 
    def multiply(y):
        return x * y
    return multiply

multipliers = []
for x in range(1, 4):
    multipliers.append(multiplier(x))

m1, m2, m3 = multipliers
print(m1(10))       #10
print(m2(10))       #20
print(m3(10))       #30