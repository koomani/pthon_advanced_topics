# floor of a real number is the largest integer less than or equal to the number

print(101 / 4)               # 25.25            # true division (int / int -> could be even float)
print(101 // 4)              # 25               # Floor division (return just int)
print(101 % 4)               # 1                # remainer -  modulus opeator (25 * 4 +1)

from math import floor
a = -10
b = 3
print(a//b)                                     # -4   positively is 3
print(floor(a/b))                               # -4   positively is 3

# Practical Python modulo operator (%)

	# 1. to check if a number is even
	
	
def func(x):
    if x % 2 == 0:
        print("this is even")

func(2)                                        # this is even

	#2. to convert seconds to days, hours, minutes, and seconds
	
from math import floor


def get_time(total_seconds):
    return {
        'days': floor(total_seconds / 60 / 60 / 24),
        'hours': floor(total_seconds / 60 / 60) % 24,
        'minutes': floor(total_seconds / 60) % 60,
        'seconds': total_seconds % 60,
         }
		 
print(get_time(93750))                             #{'days': 1, 'hours': 2, 'minutes': 2, 'seconds': 30}