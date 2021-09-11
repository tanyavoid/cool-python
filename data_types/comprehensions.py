"""
Comprehensions are an easy and concise way to create iterables.
They're also very readable (if used wisely), sometimes replacing nested loops.

TOC:
* list comprehension
* map() alternative
* filter() alternative
* scoped iteration variable note
* dict comprehension
* set comprehension
* tuple comprehension
* os operation example
* multiplication table example
"""

import os
import string
import types


# comprehension is the best way to initiate a list
years = [i for i in range(1900, 2021)]
assert 1969 in years


# map() function is easily replaced with a comprehension
squares = [i * i for i in range(10)]

values = ['', 'False', 0.001, [], {0: False}]
assert list(map(bool, values)) == [bool(i) for i in values]


# filter() alternative works well too — just add conditions to the end
odds = [i for i in range(100) if i % 2]
falsy_sequences = [i for i in values if not i and isinstance(values, int)]


# multiple conditions can be used, but expression becomes more complicated
names = ['Harry', 'Hermione', 'Draco', 'Albus', 'Minerva', 'Quirinus']
filtered_names = [i for i in names if len(i) >= 5 and i.startswith('H')]
assert filtered_names == ['Harry', 'Hermione']


# comprehensions have their own scope, that's why reusing iteration
# variables is safe comparing to loops
try:
    assert i
except NameError:
    pass  # name 'i' is not defined


# dicts
# example of mapping letters to their ordinal values
ord_values = {i: ord(i) for i in string.ascii_letters}
assert ord_values['U'] == 85

# convert the dict into a list of tuples using, again, comprehensions
ord_pairs = [(k, v) for k, v in ord_values.items()]
assert ord_pairs[0] == ('a', 97)


# sets
quote = 'People say nothing is impossible, but I do nothing every day.'
unique_letters = {i for i in quote.lower() if i.isalpha()}


# generator expression is very similar to list comprehension;
# it's more memory-friendly and simplifies usage of a generator function
years = (i for i in range(1900, 2021))
assert next(years) == 1900
assert isinstance(years, types.GeneratorType)


# tuple comprehension expression requires using the tuple()
points = tuple((x, y) for x in range(10) for y in range(10))
assert points[0] == (0, 0)
assert len(points) == 100


# os operation example on a hypothetical folder "documents"
# may want to split in into more expressions to increase readability
base = 'documents'

try:
    pdf_files = [
        os.path.join(base, i)
        for i in os.listdir(base)
        if i.endswith('.pdf') and os.path.isfile(os.path.join(base, i))
    ]
except FileNotFoundError:
    pass


# multiplication table — a matrix

table = [
    [a * b for a in range(1, 10)]  # row
    for b in range(1, 10)
]
formatted_table = [
    ' | '.join([str(i).rjust(2) for i in line])
    for line in table
]
result = [
    f'{i}\n{"-" * len(i)}'
    for i in formatted_table
]
print('\n'.join(result))
