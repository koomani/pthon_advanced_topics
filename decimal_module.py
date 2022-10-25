from decimal import Decimal
import decimal

# module that provides support for fast correctly-rounded decimal floating-point arithmetic
# Many decimal numbers don’t have exact representations in binary floating-point such as 0.1.
# When using these numbers in arithmetic operations, you’ll get a result that you would not expect. For example:

x, y, z = 0.1, 0.1, 0.1
s = x + y + z
print(s)                 # 0.30000000000000004 but not 0.3

x, y, z = Decimal('0.1'), Decimal('0.1'), Decimal('0.1')
s = x + y + z
print(s)                 #0.3     #The output is as expected.

# Decimal context
    # Decimal always associates with a context that controls the following aspects:
        # Precision during an arithmetic operation
        # Rounding algorithm
    # The global context is the default context. But, you can set a temporary context that will take effect locally without affecting the global contex

print(decimal.getcontext())
'''
Context(prec=28, rounding=ROUND_HALF_EVEN,
Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], 
traps=[InvalidOperation, DivisionByZero, Overflow])
'''
# To create a new context copied from another context, you use the localcontext() function:
    # decimal.localcontext(ctx=None)
    # The localcontext() returns a new context copied from the context ctx if specified.
    # 'ROUND_HALF_EVEN'. Note floats also use this rounding mechanism.
    # SEE Python_Round_Machansims

ctx = decimal.getcontext()
print(ctx.prec)                 # 28
print(ctx.rounding)             # ROUND_HALF_EVEN

x = Decimal('2.25')
y = Decimal('3.35')
print(round(x, 1))              #2.2   #'ROUND_HALF_EVEN'
print(round(y, 1))              #3.4

ctx = decimal.getcontext()
ctx.rounding = decimal.ROUND_HALF_UP
print(round(x, 1))              #2.3    #ROUND_HALF_UP
print(round(y, 1))              #3.4

with decimal.localcontext() as ctx:
    print('Local context:')
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1), round(y, 1))  
print('Global context:')
print(round(x, 1), round(y, 1))
#Notice that local context doesn’t affect global context. After "with" block, Python uses the default rounding mechanism
#Local context:
#2.3 3.4
#Global context:
#2.3 3.4

# Decimal constructor: 
	# You can create new decimal object based on a value
    # Decimal(value='0', context=None)  # Decimal(4.2)  # Decimal('4.2')
    # value=  integer, string, tuple, float, or another Decimal object.Defaults = '0'
    # If value = tuple, it should have three components:
        # a sign (0 for positive or 1 for negative), a tuple of digits, and an integer exponent:
        # (sign, (digit1,digit2, digit3,...), exponent)
        # For example: 3.14 = 314 x 10^-2
        # the tuple has three elements as sign (0) , digitals (3.14), exponent (-2)
x = Decimal((0, (3, 1, 4), -2))
print(x)                                               # 3.14

# When you use a float that doesn’t have an exact binary float representation, 
# the Decimal constructor cannot create an accurate decimal representation
# In practice, you’ll use a string or a tuple to construct a Decimal.
print(Decimal(0.1))                 # .1000000000000000055511151231257827021181583404541015625
print(Decimal('0.1'))               # 0.1
print(Decimal((0, (0,1), -1)))      # 0.1

# Decimal arithmetic operations:
	# Some arithmetic operators don’t work the same as floats or integers, such as div (//) and mod (%).
	# For decimal numbers, the // operator performs a truncated division: x // y = trunc( x / y)
	#Decimal class provides some mathematical operations such as sqrt and log. However, 
		#it doesn’t have all the functions defined in the math module.
    #When you use functions from the math module for decimal numbers, Python will cast the Decimal objects to floats 
		# before carrying arithmetic operations. This results in losing the precision built in the decimal objects