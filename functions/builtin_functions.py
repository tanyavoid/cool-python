"""
For common tasks Python offers a number of ready-to-use functions (and types 
that look very similar to functions). They're always available, and it's
important to remember they exist.

Also, it's crucial not to give your functions names of the built-ins to avoid
unexpected behaviours.
"""

import builtins
import types

# list all the built-in functions (or simply open the docs)
builtin_function_names = [
    name
    for name, obj in vars(builtins).items()
    if isinstance(obj, types.BuiltinFunctionType)
]

assert 'id' in builtin_function_names
assert 'abs' in builtin_function_names


# a good portion of these builtins devoted to type conversion
# or allow to initialize empty values
dict()
list()
tuple()
str()
float()
int()
set()
frozenset()
# memoryview()
# iter()

# making truth testing (converting a given value to True or False)
bool()

# and checking for type
type()
isinstance()

