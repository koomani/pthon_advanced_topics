from functools import wraps		 
		 
		 
# decorator:
		# is a function that takes another function(decorated function) as an argument and extends its (decorator) behavior without changing the original function (decorated) explicitly
		# and it returns another function (closure)


def currency(fn):                          # decorator        # fn = free variable for the clousre
    def wrapper(*args, **kwargs):                             # closure typically accepts any combination of positional and keyword-only arguments
        fn(*args, **kwargs)                # decorated        # these parameters allow you to call any fn() with any combination of positional and keyword-only arguments.

    return wrapper                                            # return another function (closure)

                                        
def net_price(price, tax):
    return price * (1 + tax)

net_price = currency(net_price)           # currency(net_price) =  def currency(fn)  net_price = fn parameter (x = func(x))
print(net_price(100, 0.05))               #$105.0

# with @ symbole


def currency(fn):                          # decorator        # fn = free variable for the clousre
    def wrapper(*args, **kwargs):                             # closure typically accepts any combination of positional and keyword-only arguments
        fn(*args, **kwargs)                # decorated        # these parameters allow you to call any fn() with any combination of positional and keyword-only arguments.

    return wrapper                                            # return another function (closure)


@currency
def net_price(price, tax):
    return price * (1 + tax)

print(net_price(100, 0.05))            #$105.0


# Introspecting decorated functions   
	# when you decorate a function, you’ll lose the original function signature and documentation.


def currency(fn):                       
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)    
        return f'${result}'
    return wrapper

def net_price(price, tax):
    "return net price"
    return price * (1 + tax)

net_price = currency(net_price)
print(net_price(100, 0.05))

help(net_price)                     #Help on function wrapper in module __main__:   returns the closre
print(net_price.__doc__)
print(net_price.__name__) 

'''                                 
wrapper(*args, **kwargs)       #closure
None
wrapper
'''
         
# To fix this use wraps() from functools standard modulus which is actually a decorator


def currency(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'${result}'
    return wrapper


@currency
def net_price(price, tax):
    "return net price"
    return price * (1 + tax)

help(net_price)
print(net_price.__name__)

'''
net_price(price, tax)
return net price 
'''

# decorator with arguments


def repeat(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for _ in range(5):
            result = fn(*args, **kwargs)
        return result
		
    return wrapper

@repeat
def say(message):
    print(message)
	
say('Hello')                          # 5 * Hello

# if you want to call say() as many as you need without hard coding
	# Note that the new repeat function isn’t a decorator. It’s a decorator factory that returns a decorator.


def repeat(times):                                     # decorator factory                            

    def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = fn(*args, **kwargs)
            return result
        return wrapper
    return decorate


@repeat(5)
def say(message):
    print(message)

say('Hello')               # # 5 * Hello

# Class decorators
	# class instance can be a callable(returns a vlaue or statment) when it implements the __call__ method
		# therefore, we can make the __call__ method as a decorator
			# so we can use callable classes (class with __call__(self, func)) to decorate functions

def star(n):
    def decorate(fn):                       # decorator factory  
        def wrapper(*args, **kwargs):
            print(n*'*')
            result = fn(*args, **kwargs)
            print(result)
            print(n*'*')
            return result
        return wrapper
    return decorate



@star(5)
def add(a, b):
    return a + b

add(10, 20)                                   # *****30*****


class Star:

    def __init__(self, n):
        self.n = n

    def __call__(self, fn):                  # def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(self.n*'*')
            print(fn(*args, **kwargs))
            print(self.n*'*')
            #return result
			
        return wrapper          

@Star(5)
def add(a, b):
    return a + b                              # *****30*****

add(10, 20)  	