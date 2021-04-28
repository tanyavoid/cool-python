"""
"Every object has an identity, a type and a value."
https://docs.python.org/3/reference/datamodel.html

identity - an object’s address in memory
is operator compares the identity of two objects
== operator compares values of objects (the data they hold)
"""

a = [0, 1, 2, 3, 4]
b = [0, 1, 2, 3, 4]
c = a

print(a == b)  # equal values
print(a is b)
print(a == c)
print(a is c)  # equal identities

# equal memory addresses mean the variables point to the same object
print(id(a) == id(b))
print(id(a) == id(c))

# the only common proper case of "is" is checking for None
if a is None:
    pass
