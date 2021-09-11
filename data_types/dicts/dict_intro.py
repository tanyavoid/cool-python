"""
Dictionaries are mapping objects: they allow to map keys to values.
They are mutable (can change) and allow to store any number of items.

A dict is created from key:value pairs separated by a comma.
Keys — labels for data stored in a dict, they're unique and hashable (immutable).
Values — the data that can be accessed using keys, they can be of any type.
"""

d1 = {}  # the simplest way to create an empty dict
d2 = dict(shape='circle', color='orange')  # another way — using a constructor

# dict representation of a pencil case
pencil_case = {
    'blue pen': 1,
    'black pen': 2,
    'lead pencil': 2,
    'colored pencil': 6,
    'eraser': 1,
    'sharpener': 1,
}

# what is in the pencil case? — get all keys
list(pencil_case)
pencil_case.keys()

# is there a marker? — let's check if a key 'marker' is in dict
'marker' in pencil_case  # False
'marker' in pencil_case.keys()  # same result

# we lost eraser — need to delete it from our pencil case
del pencil_case['eraser']
assert 'eraser' not in pencil_case

# how many items we have in the pencil case? — get a sum of all the values
assert sum(pencil_case.values()) == 12

# how many *kinds* of items we have? — number of dict keys (which are unique)
assert len(pencil_case) == len(pencil_case.keys())

# we got a new item, so need to add it in our dict case
pencil_case['ruler'] = 1

# actually we have more colored pencils, so let's change their count
pencil_case['colored pencil'] += 2

# there's still no marker, so use a default value to avoid an error
pencil_case.get('marker', 'No such thing!')
