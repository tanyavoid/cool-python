"""
Comprehensions are easy and neat way to create lists (dicts and sets as well).
They're also very readable (if used wisely), sometimes replacing nested loops.
"""

import string

# comprehension is the best way to initiate a list
years = [i for i in range(1900, 2021)]

# map() function is easily replaced with comprension
squares = [i * i for i in range(10)]

# filter() alternative works well too - just add condition at the end
odds = [i for i in range(100) if i % 2]

# multiple conditions can be used, but expression becomes more complicated
names = ['Harry', 'Hermione', 'Draco', 'Albus', 'Minerva', 'Quirinus']
filtered_names = [i for i in names if len(i) >= 5 and i.startswith('H')]
print(filtered_names)

# dicts
# example of mapping letters to their ordinal values
d = {i: ord(i) for i in string.ascii_letters}
print(d['U'])

# sets
quote = 'People say nothing is impossible, but I do nothing every day.'
unique_letters = {i for i in quote.lower() if i.isalpha()}

# generator expression is very similar to list comprehension;
# it's more memory-friendly and simplifies usage of a generator function
years = (i for i in range(1900, 2021))
print(next(years))
