# 'is' vs ' == ' in Python

# In Python, is and == are both comparison operators that
# can be used to check if two values are equal. However,
# there are some important differences between the two
# that you should be aware of.

# The is operator compares the identity of two objects, while
# the == operator compares the values of the objects. This
# means that is will only return True if the objects being
# compared are the exact same object in memory, while ==
# will return True if the objects have the same value.


a=[1,2,3,4]
b=[1,2,3,4]
print(a==b)
print(a is b)

# in case of a and b both are same in terms of value however they are different in terms of memory location or address 
# is :- exact location of oblect in the memory
# == checks the value is same or not