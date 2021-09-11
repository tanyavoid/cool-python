"""
List is a mutable sequence type that stores a collection of items in order.

Items are usually similar (homogeneous), but lists can store any data type.
Lists support a lot of operations, as well as methods to operate on its items.
Here we’ll take a look at common operations.
These operations are also supported by tuple and range objects.
"""

# the simplest way to initiate an empty list
basket = []

# list() is a constructor that allow to create a list
basket = list()  # empty
veggies = list({'tomatoes', 'cucumbers'})  # from other iterable type
fruits = list(('apples', 'bananas'))

# lists can also be created using comprehensions
prices = [(i + 0.99) for i in range(20)]  # [x for x in iterable]

# grocery list example to introduce common operations
groceries = ['cheese', 'eggs', 'bread', 'oats']

# membership tests
assert 'oats' in groceries
assert 'apples' not in groceries
assert 'butter' not in groceries

# concatenation (joining) of lists
groceries = groceries + veggies  # we can do it thanks to operator overloading
groceries += fruits  # augmented assignment does *almost* the same

# accessing items by indexes and slicing
groceries[0]  # first item in a list
groceries[-1]  # last item
groceries[:3]  # first 3 items
groceries[-3:]  # last 3 items
groceries[::2]  # every other item

# length (number of items)
len(groceries)

# smallest and largest items
min(prices)
max(prices)
assert min(groceries) == 'apples'

# getting an index (position) of an item
assert groceries.index('cheese') == 0

# items in lists are not unique, so we can count them
# but in this case each item occurs just once
assert groceries.count('apples') == 1
assert all([groceries.count(i) == 1 for i in groceries])
