"""
"Every object has an identity, a type and a value."
https://docs.python.org/3/reference/datamodel.html

Identity — an object’s address in memory;
is operator compares the identity of two objects,
== operator compares values of objects (the data they hold).
"""

a = [0, 1, 2, 3, 4]
b = [0, 1, 2, 3, 4]
c = a

a is c  # equal identities
a == b  # equal values

assert a is c
assert a is not b
assert a == c
assert a == b

# equal memory addresses mean the variables point to the same object
id(a) == id(c)  # True, the same object in memory
id(a) == id(b)  # False

# the only common proper case of "is" is checking for None
if a is None:
    pass
