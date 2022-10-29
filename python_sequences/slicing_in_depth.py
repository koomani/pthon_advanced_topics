# slicing in Depth [start:stop: step]
	# both start and stop are optional
		# start defaults to 0 and stop defaults to len(seq) when you don’t specify i
	# slices support the third argument, which is the step value. The step value defaults to 1 if you don’t specify i
	# technically, slicing relies on indexing
		# Therefore, slicing only works with sequence types.
	# however, you can use slicing to extract data from immutable sequences but assigning leads into TypeError: 'str' object does not support item assignment

# Extract data 

topic = 'Python Slicing'
print(topic[0:6])                      # Python

s = slice(1, 3)                        # A slice is actually an object of the slice type
print(type(s))                         # <class 'slice'>
print(s.start, s.stop)                 # 1 3

colors = ['red', 'green', 'blue', 'orange']
s = slice(1, 3)                        # you can use it instead the notation colors[1:3]
print(colors[s])                       # ['green', 'blue']

# Both start and stop are optional. The start defaults to 0 and stop defaults to len(seq) when you don’t specify it.
colors = ['red', 'green', 'blue', 'orange']
print(colors[0:100])                             # ['red', 'green', 'blue', 'orange']    # Since the stop bound is 100, Python uses the len(colors) for the stop bound

colors = ['red', 'green', 'blue', 'orange']
print(colors[-2:4])                              # ['blue', 'orange']

# the slice type has the indices() that returns the equivalent range (tuple) (start, stop, step) for any slice of a sequence with a specified length
colors = ['red', 'green', 'blue', 'orange']
s = slice(0, 4, 2)
t = s.indices(len(colors))
for index in range(*t):
    print(colors[index])               # red blue