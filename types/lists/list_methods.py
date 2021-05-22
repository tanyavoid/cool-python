"""
Lists are mutable, and they have a lot of methods to operate on their items.
"""

# initializing a list with items
fellowship = ['Frodo', 'Gandalf', 'Aragorn']

# adding item to the end of the list
fellowship.append('Legolas')  # you have my bow
fellowship.append('Gimli')  # and my axe

# extending list - adding items from other
fellowship.extend(['Sam', 'Merry', 'Pippin'])

# insert item to a particula position (index)
fellowship.insert(5, 'Boromir')

# create a shallow copy of a list
members = fellowship.copy()

# get index of an item
gandalf_idx = fellowship.index('Gandalf')

# remove item by its value
fellowship.remove('Boromir')

# remove item by its index, return the value
fellowship.pop(gandalf_idx)

fellowship.insert(1, 'Gandalf')
to_mordor = [fellowship.pop(0), fellowship.pop(-3)]

# sort list items in place
fellowship.sort()  # strings are sorted alphabetically

# reverse items in place
fellowship.reverse()

# clear a list - remove all items
fellowship.clear()

print(members)
