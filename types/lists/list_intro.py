"""
Lists are one sequential data types — they store a collection of items in order.

It supports a lot of operations, as well as methods to operate on its items.
"""

# the simplest way to initiate an empty list
basket = []

# list with some items
groseries = ['tomatoes', 'cheese', 'bread']

# list() is a constructor that allow to create a list
basket = list()  # empty
veggies = list({'tomato', 'cucumber'})  # from other iterable type

# lists can also be created using comprehensions
prices = [(i + 0.99) for i in range(20)]  # [x for x in iterable]
