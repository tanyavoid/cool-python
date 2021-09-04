"""
Everything in Python is an object. And every one of the objects has a type.
You can check type (class) using the type() builtin.

The common ancestor for the built-in types is "type" itself.
You can create your own types (classes), and then initialize objects
which will have this type.

Type conversion is the process of changing the type of an object.
You can do it explicitly, or Python will do it for you implicitly in cases
where it's possible without causing a TypeError.

But why care to convert? Most operations are possible only on objects of the
same *type*, such as list or string concatenation. Often to make calculations
based on user input requires converting str to int or float and so on.
"""

# demo, avoid type comparisons in real code
assert type(type) is type
assert type(42) is int
assert type(int) is type
assert type(dict) is type
assert isinstance('hey', str)  # recommended way of testing for type
assert isinstance((777), int)


### explicit conversion with built-in functions/classes

prices = ['199.99', '49.99', '209.99']

try:
    sum(prices)
except TypeError as e:
    print('Cannot calculate:', e)
    correct_prices = [float(i) for i in prices]
    assert sum(correct_prices)  # using sum() on objects of a correct type


### these are available to initialize objects or convert types of existing ones
dict()
float()
int()
list()
set()
str()
tuple()
# as well as bool(), bytes(), iter() and more

assert bool('Not True') is True
assert next(iter(prices)) == '199.99'


### implicit conversion is done automatically where it's possible

balance = 1200.04
purchase = 299
balance -= purchase  # operations between int and float
assert type(balance) is float


### more examples

colors = {'cyan': '#00ffff', 'magenta': '#ff00ff', 'yellow': '#ffff00'}
assert list(colors) == list(colors.keys())
assert set(colors) == colors.keys()

price = 199.99
assert int(price) < price  # int() rounds a float value down

falsy = ['', 0, 0.0, {}, []]
assert not any(falsy)  # any() converts each value to bool behind the scenes

converters = ['bool', 'dict', 'float', 'int', 'list', 'set', 'str', 'tuple']
values = [False, {'id': 8}, 9.99, 0, ['el', 'if'], {'unique'}, (1, 'fixed')]

# crazy double-loop

for c in converters:
    for v in values:
        try:
            result = eval(f'{c}({v})')
            print(f'{v} to {c} -> {result}')
        except (TypeError, ValueError) as e:
            print(f'Cannot convert {v} to {c} because', e)
