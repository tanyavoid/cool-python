"""
For common tasks Python offers a number of ready-to-use functions (and types
that look very similar to functions). They're always available, and it's
important to remember they exist.

Also, it's crucial not to give your functions names of the built-ins to avoid
unexpected behaviors.
"""

import builtins
import types

# list all the built-in functions (or simply open the docs)
builtin_function_names = [
    name
    for name, obj in vars(builtins).items()
    if isinstance(obj, types.BuiltinFunctionType)
]

assert 'hex' in builtin_function_names
assert 'open' in builtin_function_names

print(builtin_function_names)  # everyone's favorite function :)
dir()  # wants to be everyone's favorite

# a good portion of the builtins is devoted to type conversion
# or initializing empty values of these types (just assign variables to them)
dict()
list()
tuple()
str()
float()
int()
set()
frozenset()


# let's try some of the functions on simple examples
veggies = ['carrot', 'pepper', 'radish', 'pea', 'potato']
numbers = 2, 4, 15, 150, 10, 0

bool(veggies)  # True; making truth testing: our list is not empty
len(numbers)  # length of a iterable

# checking for type
assert type(veggies) is list
assert isinstance(numbers, tuple)

# sorting and enumerating iterables
for i, v in enumerate(sorted(veggies), start=1):
    print(f'{i}. {v}')

# saving memory
veggies_iter = iter(veggies)
numbers_iter = reversed(numbers)

assert next(veggies_iter) == 'carrot'
assert next(numbers_iter) != 2

assert all(numbers) is False  # we have 0 there
assert any(['', False, 0.0]) is False  # no True values at all

assert max(numbers) == 150
assert min(numbers) == 0

sum(numbers)  # type-specific operations
round(3.141592, 2)

# some functions, such as pow() or divmod(), are easily replaced with
# operators; others, such as map() or filter() — with comprehensions.

# making a dict, using three built-in functions
stock = dict(zip(veggies, range(10, 100, 10)))
