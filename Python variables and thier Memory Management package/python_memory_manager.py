import gc
import ctypes			  


# Python garbage collection (Python Memory Manager):
	# interacting with the garbage collector via the BUILT_IN gc MODULE.
	# in Python, you don’t have to manage the memory yourself because Python does it for you automatically by the garbage collection
	# python Memory Manager keeps track of references of objects. The Memory Manager destroys the object and reclaims the memory once the reference count of that object reaches 0.
	# sometimes, reference counting doesn’t work as expected
		# for example, (1)when you have an object that references itself (2) two objects reference each other.
		# this creates CIRCUILAR REFERNCES.
		# when the Python Memory Manager cannot remove objects with circular references, it causes a memory LEAK
		# but, garbage collector fixes circular references


def ref_count(address: int) -> int:
    "Find the refences count"
    return ctypes.c_long.from_address(address).value

def object_exists(object_id: int) -> bool:
    "Check wether the object exists in the memory"
    for object in gc.get_objects():
        if id(object) == object_id:
            return True
    return False


class A:
    def __init__(self):
        self.b = B(self)                           # class A creates a B object which is self.a = a => a object
        print(f'A: {hex(id(self))}, B: {hex(id(self.b))}')
		

class B:
    def __init__(self, a):
        self.a = a            
        print(f'B: {hex(id(self))}, A: {hex(id(self.a))}')


gc.disable()                                       # For testing purpose otherwise the Gc is fixed such issue

a = A()                                            # isntance a creates b objects which automaticlly creates a object
'''
B: 0x1d89a958080, A: 0x1d89a94ef98
A: 0x1d89a94ef98, B: 0x1d89a958080
'''
a_id = id(a)
b_id = id(a.b)
print(ref_count(a_id))                              # 2
print(ref_count(b_id))                              # 1
print(object_exists(a_id))                          # True
print(object_exists(b_id))                          # True

a = None                                            # Destroy the object a

print(ref_count(a_id))                              # 1                           Memory leak
print(ref_count(b_id))                              # 1
print(object_exists(a_id))                          # True
print(object_exists(b_id))                          # True

gc.collect()                                        # to detect the circular reference, destroy the objects, and reclaim the memory

print(ref_count(a_id))                              # 0
print(ref_count(b_id))                              # 0
print(object_exists(a_id))                          # False
print(object_exists(b_id))                          # False